#!/usr/bin/env python
"""
Generate a sample AnnData (h5ad) file for testing the single cell schema.
"""

import argparse
import logging
import os
import random
import numpy as np
import pandas as pd
import scanpy as sc
from typing import List, Tuple, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define sample data
CELL_TYPES = [
    "CL:0000084",  # T cell
    "CL:0000236",  # B cell
    "CL:0000576",  # monocyte
    "CL:0000775",  # neutrophil
    "CL:0000094",  # granulocyte
    "CL:0000813",  # memory B cell
    "CL:0000814",  # mature NK T cell
    "CL:0000939",  # T helper cell
]

TISSUES = [
    "UBERON:0000178",  # blood
    "UBERON:0002371",  # bone marrow
    "UBERON:0002509",  # lymph node
    "UBERON:0002370",  # thymus
    "UBERON:0002106",  # spleen
]

DISEASES = [
    "MONDO:0005109",  # diabetes mellitus
    "MONDO:0005299",  # asthma
    "MONDO:0007179",  # rheumatoid arthritis
    "MONDO:0005812",  # healthy control
]

DEV_STAGES = [
    "HsapDv:0000087",  # adult
    "HsapDv:0000082",  # adolescent stage
    "HsapDv:0000246",  # middle aged adult stage
]

ASSAYS = [
    "EFO:0008913",  # 10x 3' v2
    "EFO:0008914",  # 10x 3' v3
    "EFO:0010550",  # Smart-seq2
]

def generate_sample_data(
    n_cells: int = 1000,
    n_genes: int = 200,
    random_seed: int = 42,
    output_file: str = "sample_data.h5ad",
) -> None:
    """
    Generate a sample AnnData object and save it to an h5ad file.
    
    Args:
        n_cells: Number of cells to generate.
        n_genes: Number of genes to generate.
        random_seed: Random seed for reproducibility.
        output_file: Path to the output h5ad file.
    """
    logger.info(f"Generating sample data with {n_cells} cells and {n_genes} genes")
    
    # Set random seed for reproducibility
    np.random.seed(random_seed)
    random.seed(random_seed)
    
    # Generate random count data
    X = np.random.negative_binomial(5, 0.3, size=(n_cells, n_genes))
    
    # Generate gene names (features)
    var_names = [f"gene_{i}" for i in range(n_genes)]
    
    # Generate cell metadata (observations)
    obs = pd.DataFrame(index=[f"cell_{i}" for i in range(n_cells)])
    
    # Generate cell type annotations with hierarchical structure
    # Level 1: broad cell types
    broad_cell_types = np.random.choice(CELL_TYPES[:4], size=n_cells)
    
    # Level 2: more specific cell types (adding more detail to some cells)
    specific_cell_types = broad_cell_types.copy()
    
    # Replace some T cells with more specific T cell subtypes
    t_cell_mask = broad_cell_types == "CL:0000084"
    specific_t_cells = np.random.choice(["CL:0000814", "CL:0000939"], size=t_cell_mask.sum())
    specific_cell_types[t_cell_mask] = specific_t_cells
    
    # Replace some B cells with memory B cells
    b_cell_mask = broad_cell_types == "CL:0000236"
    memory_mask = np.random.choice([True, False], size=b_cell_mask.sum(), p=[0.3, 0.7])
    specific_cell_types[b_cell_mask] = np.where(memory_mask, "CL:0000813", "CL:0000236")
    
    # Add to observation dataframe
    obs["cell_type_l1"] = broad_cell_types
    obs["cell_type"] = specific_cell_types
    
    # Generate tissue annotations
    obs["tissue"] = np.random.choice(TISSUES, size=n_cells)
    
    # Generate disease annotations (skewed toward healthy)
    obs["disease"] = np.random.choice(DISEASES, size=n_cells, p=[0.1, 0.1, 0.1, 0.7])
    
    # Generate developmental stage annotations
    obs["development_stage"] = np.random.choice(DEV_STAGES, size=n_cells, p=[0.7, 0.15, 0.15])
    
    # Generate assay annotations
    obs["assay"] = np.random.choice(ASSAYS, size=n_cells, p=[0.5, 0.3, 0.2])
    
    # Create AnnData object
    adata = sc.AnnData(X=X, obs=obs, var=pd.DataFrame(index=var_names))
    
    # Add some computed metrics
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.pca(adata, n_comps=20)
    sc.pp.neighbors(adata)
    sc.tl.umap(adata)
    
    # Save to file
    logger.info(f"Saving AnnData to {output_file}")
    adata.write_h5ad(output_file)
    logger.info("Sample data generation complete")
    
    return adata


def main():
    parser = argparse.ArgumentParser(description="Generate a sample AnnData (h5ad) file for testing the single cell schema")
    parser.add_argument("--n-cells", type=int, default=1000, help="Number of cells to generate (default: 1000)")
    parser.add_argument("--n-genes", type=int, default=200, help="Number of genes to generate (default: 200)")
    parser.add_argument("--random-seed", type=int, default=42, help="Random seed for reproducibility (default: 42)")
    parser.add_argument("--output", "-o", default="sample_data.h5ad", help="Path to the output h5ad file (default: sample_data.h5ad)")
    
    args = parser.parse_args()
    
    generate_sample_data(
        n_cells=args.n_cells,
        n_genes=args.n_genes,
        random_seed=args.random_seed,
        output_file=args.output,
    )


if __name__ == "__main__":
    main()