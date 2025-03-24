#!/usr/bin/env python
"""
End-to-end example demonstrating the full workflow:
1. Generate sample AnnData
2. Populate the LinkML schema
3. Display some basic statistics about the generated knowledge graph
"""

import os
import json
import logging

from generate_sample_data import generate_sample_data
from populate_schema import load_anndata, get_cell_sets_from_anndata, create_dataset, save_objects

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define file paths
SAMPLE_DATA_FILE = "sample_data.h5ad"
OUTPUT_JSON_FILE = "sample_dataset.json"

def run_example():
    """Run the full example workflow."""
    print("\n" + "="*80)
    print("SINGLE CELL TRANSCRIPTOMICS SCHEMA EXAMPLE")
    print("="*80)
    
    # Step 1: Generate sample AnnData file
    print("\n1. Generating sample AnnData data")
    print("-"*50)
    
    if os.path.exists(SAMPLE_DATA_FILE):
        print(f"Using existing sample data file: {SAMPLE_DATA_FILE}")
    else:
        print(f"Generating new sample data file: {SAMPLE_DATA_FILE}")
        generate_sample_data(
            n_cells=1000,
            n_genes=200,
            output_file=SAMPLE_DATA_FILE
        )
    
    # Step 2: Populate the LinkML schema
    print("\n2. Populating the LinkML schema")
    print("-"*50)
    
    # Load the AnnData object
    adata = load_anndata(SAMPLE_DATA_FILE)
    
    # Extract cell sets and relationships
    cell_sets, cell_types, tissues, diseases, dev_stages, assays = get_cell_sets_from_anndata(
        adata=adata,
        cell_type_columns=["cell_type_l1", "cell_type"],
        tissue_column="tissue",
        disease_column="disease",
        dev_stage_column="development_stage",
        assay_column="assay",
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
        dataset_name="Sample Dataset",
    )
    
    # Save all objects
    save_objects(
        output_file=OUTPUT_JSON_FILE,
        dataset=dataset,
        cell_sets=cell_sets,
        cell_types=cell_types,
        tissues=tissues,
        diseases=diseases,
        dev_stages=dev_stages,
        assays=assays,
        format="json",
    )
    
    # Step 3: Display schema statistics
    print("\n3. Knowledge Graph Statistics")
    print("-"*50)
    
    # Load the generated JSON file
    with open(OUTPUT_JSON_FILE, 'r') as f:
        data = json.load(f)
    
    # Print statistics
    print(f"Dataset name: {data['dataset']['name']}")
    print(f"Cell sets: {len(data['cell_sets'])}")
    print(f"Cell types: {len(data['cell_types'])}")
    print(f"Tissues: {len(data['tissues'])}")
    print(f"Diseases: {len(data['diseases'])}")
    print(f"Developmental stages: {len(data['developmental_stages'])}")
    print(f"Assays: {len(data['assays'])}")
    
    # Count relationships
    subset_rels = sum(1 for cs in data['cell_sets'] if 'subset_of' in cs)
    cell_type_rels = sum(1 for cs in data['cell_sets'] if 'predominantly_consists_of' in cs)
    tissue_rels = sum(len(cs.get('has_tissue', [])) for cs in data['cell_sets'])
    disease_rels = sum(len(cs.get('has_disease', [])) for cs in data['cell_sets'])
    dev_stage_rels = sum(len(cs.get('has_developmental_stage', [])) for cs in data['cell_sets'])
    assay_rels = sum(len(cs.get('has_assay', [])) for cs in data['cell_sets'])
    
    print("\nRelationships:")
    print(f"subset_of relationships: {subset_rels}")
    print(f"predominantly_consists_of relationships: {cell_type_rels}")
    print(f"Tissue associations: {tissue_rels}")
    print(f"Disease associations: {disease_rels}")
    print(f"Developmental stage associations: {dev_stage_rels}")
    print(f"Assay associations: {assay_rels}")
    
    # Sample cell set
    if data['cell_sets']:
        print("\nSample cell set:")
        cs = data['cell_sets'][0]
        print(f"  ID: {cs['id']}")
        print(f"  Name: {cs['name']}")
        print(f"  Cell count: {cs['cell_count']}")
        print(f"  Observation column: {cs['obs_column']}")
        
        if 'predominantly_consists_of' in cs:
            print(f"  Cell type: {cs['predominantly_consists_of']}")
            
        if 'has_tissue' in cs and cs['has_tissue']:
            print(f"  Has tissue: {cs['has_tissue'][0]['term']} ({cs['has_tissue'][0]['count']} cells)")
    
    print("\n" + "="*80)
    print(f"Complete! Dataset saved to {OUTPUT_JSON_FILE}")
    print("="*80 + "\n")

if __name__ == "__main__":
    run_example()