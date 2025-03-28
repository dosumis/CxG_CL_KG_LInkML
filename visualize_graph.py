#!/usr/bin/env python
"""
Visualize the knowledge graph from single cell transcriptomics data.
"""

import argparse
import json
import logging
import os
import sys
import yaml
from typing import Dict, Any, List, Tuple, Optional, Set

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.colors import TABLEAU_COLORS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define colors for different node types
NODE_COLORS = {
    'CellSet': 'tab:blue',
    'CellType': 'tab:red',
    'Tissue': 'tab:green',
    'Disease': 'tab:purple',
    'DevelopmentalStage': 'tab:orange',
    'Assay': 'tab:cyan',
}

# Define edge colors for different relationship types
EDGE_COLORS = {
    'subset_of': 'tab:blue',
    'predominantly_consists_of': 'tab:red',
    'has_tissue': 'tab:green',
    'has_disease': 'tab:purple',
    'has_developmental_stage': 'tab:orange',
    'has_assay': 'tab:cyan',
}


def load_data(file_path: str) -> Dict[str, Any]:
    """
    Load data from a JSON or YAML file.
    
    Args:
        file_path: Path to the data file.
        
    Returns:
        A dictionary containing the loaded data.
    """
    logger.info(f"Loading data from {file_path}")
    
    try:
        if file_path.endswith('.json'):
            with open(file_path, 'r') as f:
                data = json.load(f)
        elif file_path.endswith(('.yaml', '.yml')):
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
        else:
            raise ValueError(f"Unsupported file format: {file_path}. Must be JSON or YAML.")
        
        return data
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise


def get_node_type(node_id: str) -> str:
    """
    Determine the type of a node based on its ID.
    
    Args:
        node_id: The ID of the node.
        
    Returns:
        The type of the node.
    """
    if node_id.startswith(('CL:', 'CL_')):
        return 'CellType'
    elif node_id.startswith(('UBERON:', 'UBERON_')):
        return 'Tissue'
    elif node_id.startswith(('MONDO:', 'MONDO_')):
        return 'Disease'
    elif node_id.startswith(('HsapDv:', 'HsapDv_', 'MmusDv:', 'MmusDv_')):
        return 'DevelopmentalStage'
    elif node_id.startswith(('EFO:', 'EFO_')):
        return 'Assay'
    elif 'CellSet' in node_id:
        return 'CellSet'
    else:
        return 'Unknown'


def get_short_label(node_id: str, node_data: Dict) -> str:
    """
    Get a short label for a node.
    
    Args:
        node_id: The ID of the node.
        node_data: The data associated with the node.
        
    Returns:
        A short label for the node.
    """
    if 'name' in node_data:
        # Extract the first part of the name (before any spaces)
        name_parts = node_data['name'].split()
        if len(name_parts) > 1 and get_node_type(node_id) == 'CellSet':
            return name_parts[0]  # Just return the value part
        else:
            return node_data['name']
    else:
        # Use the last part of the ID
        return node_id.split(':')[-1]


def build_graph(data: Dict[str, Any], include_metadata: bool = True, max_nodes: Optional[int] = None) -> nx.DiGraph:
    """
    Build a NetworkX graph from the data.
    
    Args:
        data: The data to visualize.
        include_metadata: Whether to include metadata nodes (tissues, diseases, etc.).
        max_nodes: Maximum number of nodes to include in the graph.
        
    Returns:
        A NetworkX DiGraph.
    """
    logger.info("Building graph")
    
    G = nx.DiGraph()
    
    # Track the number of nodes added
    node_count = 0
    
    # Dictionary to store node attributes
    node_attrs = {}
    
    # Add cell sets as nodes
    if 'cell_sets' in data:
        for cs in data['cell_sets']:
            if max_nodes is not None and node_count >= max_nodes:
                break
                
            # Add the node
            G.add_node(cs['id'])
            node_attrs[cs['id']] = {
                'type': 'CellSet',
                'label': get_short_label(cs['id'], cs),
                'count': cs.get('cell_count', 0),
            }
            node_count += 1
            
            # Add subset relationships
            if 'subset_of' in cs:
                for parent_id in cs['subset_of']:
                    G.add_edge(cs['id'], parent_id, type='subset_of')
            
            # Add cell type relationships
            if 'predominantly_consists_of' in cs:
                ct_id = cs['predominantly_consists_of']
                G.add_edge(cs['id'], ct_id, type='predominantly_consists_of')
                
                # Add the cell type node if not already present
                if ct_id not in G:
                    G.add_node(ct_id)
                    # Try to find this cell type in the data
                    ct_data = next((ct for ct in data.get('cell_types', []) if ct['id'] == ct_id), {'id': ct_id})
                    node_attrs[ct_id] = {
                        'type': 'CellType',
                        'label': get_short_label(ct_id, ct_data),
                    }
                    node_count += 1
            
            # Add metadata relationships
            if include_metadata:
                for metadata_type, rel_key in [
                    ('Tissue', 'has_tissue'),
                    ('Disease', 'has_disease'),
                    ('DevelopmentalStage', 'has_developmental_stage'),
                    ('Assay', 'has_assay'),
                ]:
                    if rel_key in cs:
                        for assoc in cs[rel_key]:
                            term_id = assoc['term']
                            
                            # Add the metadata node if not already present
                            if term_id not in G and (max_nodes is None or node_count < max_nodes):
                                G.add_node(term_id)
                                
                                # Find the metadata object
                                metadata_key = {
                                    'Tissue': 'tissues',
                                    'Disease': 'diseases',
                                    'DevelopmentalStage': 'developmental_stages',
                                    'Assay': 'assays',
                                }[metadata_type]
                                
                                term_data = next((t for t in data.get(metadata_key, []) if t['id'] == term_id), {'id': term_id})
                                
                                node_attrs[term_id] = {
                                    'type': metadata_type,
                                    'label': get_short_label(term_id, term_data),
                                }
                                node_count += 1
                            
                            # Add the edge
                            if term_id in G:
                                G.add_edge(cs['id'], term_id, type=rel_key, count=assoc['count'])
    
    # Set node attributes
    nx.set_node_attributes(G, node_attrs)
    
    logger.info(f"Built graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    
    return G


def visualize_graph(G: nx.DiGraph, output_file: str, title: str = "Single Cell Transcriptomics Knowledge Graph"):
    """
    Visualize the graph.
    
    Args:
        G: The NetworkX graph to visualize.
        output_file: Path to the output file.
        title: Title for the plot.
    """
    logger.info(f"Visualizing graph to {output_file}")
    
    plt.figure(figsize=(16, 12))
    
    # Use different layouts based on graph size
    if G.number_of_nodes() < 50:
        pos = nx.spring_layout(G, seed=42)
    else:
        pos = nx.kamada_kawai_layout(G)
    
    # Draw nodes by type
    for node_type, color in NODE_COLORS.items():
        nodes = [n for n, attrs in G.nodes(data=True) if attrs.get('type') == node_type]
        
        if nodes:
            # Scale node sizes based on count if available
            sizes = [300 + min(3000, G.nodes[n].get('count', 0)) for n in nodes]
            
            nx.draw_networkx_nodes(
                G, pos,
                nodelist=nodes,
                node_color=color,
                node_size=sizes,
                alpha=0.8,
                label=node_type
            )
    
    # Draw edges by type
    for edge_type, color in EDGE_COLORS.items():
        edges = [(u, v) for u, v, attrs in G.edges(data=True) if attrs.get('type') == edge_type]
        
        if edges:
            nx.draw_networkx_edges(
                G, pos,
                edgelist=edges,
                edge_color=color,
                width=1.5,
                alpha=0.6,
                arrowsize=15,
                label=edge_type
            )
    
    # Draw labels
    labels = {}
    for n, attrs in G.nodes(data=True):
        if 'label' in attrs:
            labels[n] = attrs['label']
        elif 'name' in attrs:
            labels[n] = attrs['name']
        else:
            # Use node ID as fallback
            labels[n] = n.split(':')[-1]
    
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, font_weight='bold')
    
    plt.title(title, fontsize=16)
    plt.axis('off')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    # Save the figure
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    logger.info(f"Saved visualization to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Visualize the knowledge graph from single cell transcriptomics data")
    parser.add_argument("data_file", help="Path to the data file (JSON or YAML)")
    parser.add_argument("--output", "-o", default="knowledge_graph.png", 
                        help="Path to the output image file (default: knowledge_graph.png)")
    parser.add_argument("--title", "-t", default="Single Cell Transcriptomics Knowledge Graph",
                        help="Title for the plot (default: 'Single Cell Transcriptomics Knowledge Graph')")
    parser.add_argument("--no-metadata", action="store_true", 
                        help="Do not include metadata nodes (tissues, diseases, etc.)")
    parser.add_argument("--max-nodes", type=int, default=None,
                        help="Maximum number of nodes to include in the graph")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Check if the data file exists
    if not os.path.exists(args.data_file):
        logger.error(f"Data file not found: {args.data_file}")
        sys.exit(1)
    
    # Load the data
    try:
        data = load_data(args.data_file)
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        sys.exit(1)
    
    # Build the graph
    try:
        G = build_graph(data, include_metadata=not args.no_metadata, max_nodes=args.max_nodes)
    except Exception as e:
        logger.error(f"Failed to build graph: {e}")
        sys.exit(1)
    
    # Visualize the graph
    try:
        visualize_graph(G, args.output, title=args.title)
    except Exception as e:
        logger.error(f"Failed to visualize graph: {e}")
        sys.exit(1)
    
    print(f"✅ Knowledge graph visualization saved to {args.output}")


if __name__ == "__main__":
    main()