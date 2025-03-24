#!/usr/bin/env python
"""
Script to populate the single cell transcriptomics schema from AnnData (h5ad) files.
"""

import argparse
import logging
import os
import uuid
from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple, Any, Union

import anndata
import numpy as np
import pandas as pd
import scanpy as sc
from linkml_runtime import SchemaView
from linkml_runtime.utils.formatutils import camelcase
from linkml_runtime.dumpers import json_dumper, yaml_dumper


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_anndata(file_path: str) -> anndata.AnnData:
    """
    Load an AnnData object from an h5ad file.
    
    Args:
        file_path: Path to the h5ad file.
        
    Returns:
        An AnnData object.
    """
    logger.info(f"Loading AnnData from {file_path}")
    try:
        adata = sc.read_h5ad(file_path)
        logger.info(f"Loaded AnnData with {adata.n_obs} cells and {adata.n_vars} genes")
        return adata
    except Exception as e:
        logger.error(f"Error loading AnnData: {e}")
        raise


def create_ontology_term_id(term_id: str, prefix: str) -> str:
    """
    Create a properly formatted ontology term ID.
    
    Args:
        term_id: The original term ID.
        prefix: The ontology prefix.
        
    Returns:
        A properly formatted ontology term ID.
    """
    # Strip the prefix if it's already there
    if term_id.startswith(f"{prefix}:"):
        term_id = term_id[len(f"{prefix}:"):]
    elif term_id.startswith(f"{prefix}_"):
        term_id = term_id[len(f"{prefix}_"):]
        
    # Format the ID properly
    return f"{prefix}:{term_id}"


def get_cell_sets_from_anndata(
    adata: anndata.AnnData,
    cell_type_columns: List[str],
    tissue_column: str,
    disease_column: str,
    dev_stage_column: str,
    assay_column: str,
) -> Tuple[Dict, Dict, Dict, Dict, Dict, Dict]:
    """
    Extract cell sets and their relationships from an AnnData object.
    
    Args:
        adata: The AnnData object.
        cell_type_columns: List of column names in adata.obs that contain cell type annotations.
        tissue_column: Column name in adata.obs that contains tissue annotations.
        disease_column: Column name in adata.obs that contains disease annotations.
        dev_stage_column: Column name in adata.obs that contains developmental stage annotations.
        assay_column: Column name in adata.obs that contains assay annotations.
        
    Returns:
        Tuple of dictionaries: (cell_sets, cell_types, tissues, diseases, dev_stages, assays)
    """
    logger.info("Extracting cell sets and relationships from AnnData")
    
    # Initialize dictionaries to store entities
    cell_sets = {}
    cell_types = {}
    tissues = {}
    diseases = {}
    dev_stages = {}
    assays = {}
    
    # Process each cell type column to create cell sets
    for col in cell_type_columns:
        if col not in adata.obs.columns:
            logger.warning(f"Column {col} not found in AnnData.obs")
            continue
            
        logger.info(f"Processing cell type column: {col}")
        
        # Get unique values in this column
        unique_values = adata.obs[col].unique()
        
        for value in unique_values:
            if pd.isna(value):
                continue
                
            # Create a unique ID for this cell set
            cell_set_id = f"schema:CellSet_{camelcase(col)}_{uuid.uuid4().hex[:8]}"
            
            # Get cells with this annotation
            mask = adata.obs[col] == value
            cell_count = mask.sum()
            
            # Create cell set
            cell_sets[cell_set_id] = {
                "id": cell_set_id,
                "name": f"{value} cells from {col}",
                "description": f"Cells annotated as {value} in the {col} column",
                "obs_column": col,
                "cell_count": int(cell_count),
            }
            
            # Check if this value corresponds to a Cell Ontology term
            if isinstance(value, str) and value.startswith(("CL:", "CL_")):
                # Create cell type entity
                cell_type_id = create_ontology_term_id(value, "CL")
                
                if cell_type_id not in cell_types:
                    cell_types[cell_type_id] = {
                        "id": cell_type_id,
                        "name": value,
                        "description": f"Cell type: {value}",
                        "source_uri": cell_type_id,
                        "predominantly_in": []
                    }
                
                # Link cell set to cell type
                cell_sets[cell_set_id]["predominantly_consists_of"] = cell_type_id
                cell_types[cell_type_id]["predominantly_in"].append(cell_set_id)
    
    # Process subset relationships between cell sets
    # We assume that a cell set is a subset of another if its cells are a proper subset
    for cs1_id, cs1 in cell_sets.items():
        cs1_mask = adata.obs[cs1["obs_column"]] == cs1["name"].split()[0]  # Extract the value part
        
        for cs2_id, cs2 in cell_sets.items():
            if cs1_id == cs2_id:
                continue
                
            cs2_mask = adata.obs[cs2["obs_column"]] == cs2["name"].split()[0]  # Extract the value part
            
            # Check if cs1 is a subset of cs2
            if np.all(cs1_mask & cs2_mask == cs1_mask) and np.any(cs2_mask & ~cs1_mask):
                if "subset_of" not in cs1:
                    cs1["subset_of"] = []
                cs1["subset_of"].append(cs2_id)
    
    # Process metadata columns to create metadata associations
    metadata_columns = {
        "tissue": (tissue_column, tissues, "UBERON", "has_tissue"),
        "disease": (disease_column, diseases, "MONDO", "has_disease"),
        "dev_stage": (dev_stage_column, dev_stages, "HsapDv", "has_developmental_stage"),
        "assay": (assay_column, assays, "EFO", "has_assay")
    }
    
    for metadata_type, (col_name, term_dict, prefix, assoc_slot) in metadata_columns.items():
        if col_name not in adata.obs.columns:
            logger.warning(f"{metadata_type.capitalize()} column {col_name} not found in AnnData.obs")
            continue
            
        logger.info(f"Processing {metadata_type} metadata from column: {col_name}")
        
        # Get unique values in this column
        unique_values = adata.obs[col_name].unique()
        
        for value in unique_values:
            if pd.isna(value):
                continue
                
            # Check if this value corresponds to an ontology term
            if isinstance(value, str) and value.startswith((f"{prefix}:", f"{prefix}_")):
                # Create ontology term entity
                term_id = create_ontology_term_id(value, prefix)
                
                if term_id not in term_dict:
                    term_dict[term_id] = {
                        "id": term_id,
                        "name": value,
                        "description": f"{metadata_type.capitalize()}: {value}",
                        "source_uri": term_id,
                        "present_in_cell_sets": []
                    }
                
                # For each cell set, count cells with this metadata
                for cs_id, cs in cell_sets.items():
                    cs_mask = adata.obs[cs["obs_column"]] == cs["name"].split()[0]
                    metadata_mask = adata.obs[col_name] == value
                    cell_count = (cs_mask & metadata_mask).sum()
                    
                    if cell_count > 0:
                        if assoc_slot not in cs:
                            cs[assoc_slot] = []
                            
                        cs[assoc_slot].append({
                            "term": term_id,
                            "count": int(cell_count)
                        })
                        
                        term_dict[term_id]["present_in_cell_sets"].append(cs_id)
    
    return cell_sets, cell_types, tissues, diseases, dev_stages, assays


def create_dataset(
    adata: anndata.AnnData,
    cell_sets: Dict,
    cell_types: Dict,
    tissues: Dict,
    diseases: Dict,
    dev_stages: Dict,
    assays: Dict,
    dataset_name: str,
) -> Dict:
    """
    Create a dataset object that contains all the entities.
    
    Args:
        adata: The AnnData object.
        cell_sets: Dictionary of cell sets.
        cell_types: Dictionary of cell types.
        tissues: Dictionary of tissues.
        diseases: Dictionary of diseases.
        dev_stages: Dictionary of developmental stages.
        assays: Dictionary of assays.
        dataset_name: Name of the dataset.
        
    Returns:
        A dictionary representing the dataset.
    """
    logger.info("Creating dataset object")
    
    dataset_id = f"schema:Dataset_{uuid.uuid4().hex[:8]}"
    
    # Combine all ontology terms
    ontology_terms = list(cell_types.keys()) + list(tissues.keys()) + list(diseases.keys()) + list(dev_stages.keys()) + list(assays.keys())
    
    dataset = {
        "id": dataset_id,
        "name": dataset_name,
        "description": f"Single cell transcriptomics dataset with {adata.n_obs} cells",
        "cell_sets": list(cell_sets.keys()),
        "ontology_terms": ontology_terms,
    }
    
    return dataset


def save_objects(
    output_file: str,
    dataset: Dict,
    cell_sets: Dict,
    cell_types: Dict,
    tissues: Dict,
    diseases: Dict,
    dev_stages: Dict,
    assays: Dict,
    format: str = "json",
) -> None:
    """
    Save all objects to a file.
    
    Args:
        output_file: Path to the output file.
        dataset: The dataset object.
        cell_sets: Dictionary of cell sets.
        cell_types: Dictionary of cell types.
        tissues: Dictionary of tissues.
        diseases: Dictionary of diseases.
        dev_stages: Dictionary of developmental stages.
        assays: Dictionary of assays.
        format: Output format ("json" or "yaml").
    """
    logger.info(f"Saving objects to {output_file} in {format} format")
    
    # Combine all objects
    objects = {
        "dataset": dataset,
        "cell_sets": list(cell_sets.values()),
        "cell_types": list(cell_types.values()),
        "tissues": list(tissues.values()),
        "diseases": list(diseases.values()),
        "developmental_stages": list(dev_stages.values()),
        "assays": list(assays.values()),
    }
    
    # Save to file
    try:
        if format.lower() == "json":
            # Use standard json module since LinkML's dumper doesn't support indent
            with open(output_file, "w") as f:
                import json
                json.dump(objects, f, indent=2)
        elif format.lower() == "yaml":
            yaml_dumper.dump(objects, output_file)
        else:
            logger.error(f"Unsupported format: {format}")
            raise ValueError(f"Unsupported format: {format}")
            
        logger.info(f"Successfully saved data to {output_file}")
    except Exception as e:
        logger.error(f"Error saving data: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(description="Populate single cell transcriptomics schema from AnnData (h5ad) files")
    parser.add_argument("input_file", help="Path to the input h5ad file")
    parser.add_argument("--output", "-o", default="dataset.json", help="Path to the output file (default: dataset.json)")
    parser.add_argument("--format", "-f", choices=["json", "yaml"], default="json", help="Output format (default: json)")
    parser.add_argument("--dataset-name", default=None, help="Name of the dataset (default: derived from input filename)")
    parser.add_argument("--cell-type-columns", nargs="+", default=["cell_type", "cell_ontology_term"], 
                        help="Column names in AnnData.obs that contain cell type annotations (default: ['cell_type', 'cell_ontology_term'])")
    parser.add_argument("--tissue-column", default="tissue", 
                        help="Column name in AnnData.obs that contains tissue annotations (default: 'tissue')")
    parser.add_argument("--disease-column", default="disease", 
                        help="Column name in AnnData.obs that contains disease annotations (default: 'disease')")
    parser.add_argument("--dev-stage-column", default="development_stage", 
                        help="Column name in AnnData.obs that contains developmental stage annotations (default: 'development_stage')")
    parser.add_argument("--assay-column", default="assay", 
                        help="Column name in AnnData.obs that contains assay annotations (default: 'assay')")
    
    args = parser.parse_args()
    
    # Set dataset name if not provided
    if args.dataset_name is None:
        args.dataset_name = os.path.splitext(os.path.basename(args.input_file))[0]
    
    # Load the AnnData object
    adata = load_anndata(args.input_file)
    
    # Extract cell sets and relationships
    cell_sets, cell_types, tissues, diseases, dev_stages, assays = get_cell_sets_from_anndata(
        adata=adata,
        cell_type_columns=args.cell_type_columns,
        tissue_column=args.tissue_column,
        disease_column=args.disease_column,
        dev_stage_column=args.dev_stage_column,
        assay_column=args.assay_column,
    )
    
    # Create dataset object
    dataset = create_dataset(
        adata=adata,
        cell_sets=cell_sets,
        cell_types=cell_types,
        tissues=tissues,
        diseases=diseases,
        dev_stages=dev_stages,
        assays=assays,
        dataset_name=args.dataset_name,
    )
    
    # Save all objects
    save_objects(
        output_file=args.output,
        dataset=dataset,
        cell_sets=cell_sets,
        cell_types=cell_types,
        tissues=tissues,
        diseases=diseases,
        dev_stages=dev_stages,
        assays=assays,
        format=args.format,
    )
    
    logger.info("Done!")


if __name__ == "__main__":
    main()