#!/usr/bin/env python
"""
Example of using the generated LinkML Python dataclasses for single cell transcriptomics data.
"""

import uuid
import sys
import json
from typing import List, Dict, Any, Optional, Union

# Import the generated dataclasses
from single_cell_schema.single_cell_schema import (
    CellSet, 
    CellType, 
    Tissue, 
    Disease, 
    DevelopmentalStage,
    Assay, 
    Cell, 
    Dataset, 
    MetadataAssociation
)


def create_example_data() -> Dict[str, Any]:
    """
    Create an example dataset using the LinkML Python dataclasses.
    
    Returns:
        A dictionary containing the created entities.
    """
    print("Creating example data using LinkML dataclasses...")
    
    # Create cell types
    t_cell = CellType(
        id="CL:0000084",
        name="T cell",
        description="A type of lymphocyte that develops in the thymus.",
        source_uri="http://purl.obolibrary.org/obo/CL_0000084",
        predominantly_in=[]
    )
    
    b_cell = CellType(
        id="CL:0000236",
        name="B cell",
        description="A type of lymphocyte that produces antibodies.",
        source_uri="http://purl.obolibrary.org/obo/CL_0000236",
        predominantly_in=[]
    )
    
    # Create tissues
    blood = Tissue(
        id="UBERON:0000178",
        name="blood",
        description="The fluid that circulates in the heart, arteries, capillaries, and veins.",
        source_uri="http://purl.obolibrary.org/obo/UBERON_0000178",
        present_in_cell_sets=[]
    )
    
    # Create diseases
    healthy = Disease(
        id="MONDO:0005812",
        name="healthy control",
        description="A person who does not have the condition under study.",
        source_uri="http://purl.obolibrary.org/obo/MONDO_0005812",
        present_in_cell_sets=[]
    )
    
    # Create developmental stages
    adult = DevelopmentalStage(
        id="HsapDv:0000087",
        name="adult",
        description="The stage of development during which an organism is fully developed.",
        source_uri="http://purl.obolibrary.org/obo/HsapDv_0000087",
        present_in_cell_sets=[]
    )
    
    # Create assays
    tenx_v3 = Assay(
        id="EFO:0008914",
        name="10x 3' v3",
        description="10x Genomics 3' gene expression v3 assay.",
        source_uri="http://purl.obolibrary.org/obo/EFO_0008914",
        present_in_cell_sets=[]
    )
    
    # Create cell sets
    t_cell_set_id = f"cs:t_cells_{uuid.uuid4().hex[:8]}"
    t_cell_set = CellSet(
        id=t_cell_set_id,
        name="T cells",
        description="T cells from blood",
        obs_column="cell_type",
        cell_count=500,
        cells=[],
        subset_of=[],
        predominantly_consists_of=t_cell.id,
        has_tissue=[
            MetadataAssociation(
                term=blood.id,
                count=500
            )
        ],
        has_disease=[
            MetadataAssociation(
                term=healthy.id,
                count=500
            )
        ],
        has_developmental_stage=[
            MetadataAssociation(
                term=adult.id,
                count=500
            )
        ],
        has_assay=[
            MetadataAssociation(
                term=tenx_v3.id,
                count=500
            )
        ]
    )
    
    b_cell_set_id = f"cs:b_cells_{uuid.uuid4().hex[:8]}"
    b_cell_set = CellSet(
        id=b_cell_set_id,
        name="B cells",
        description="B cells from blood",
        obs_column="cell_type",
        cell_count=300,
        cells=[],
        subset_of=[],
        predominantly_consists_of=b_cell.id,
        has_tissue=[
            MetadataAssociation(
                term=blood.id,
                count=300
            )
        ],
        has_disease=[
            MetadataAssociation(
                term=healthy.id,
                count=300
            )
        ],
        has_developmental_stage=[
            MetadataAssociation(
                term=adult.id,
                count=300
            )
        ],
        has_assay=[
            MetadataAssociation(
                term=tenx_v3.id,
                count=300
            )
        ]
    )
    
    # Update references
    t_cell.predominantly_in.append(t_cell_set_id)
    b_cell.predominantly_in.append(b_cell_set_id)
    blood.present_in_cell_sets.extend([t_cell_set_id, b_cell_set_id])
    healthy.present_in_cell_sets.extend([t_cell_set_id, b_cell_set_id])
    adult.present_in_cell_sets.extend([t_cell_set_id, b_cell_set_id])
    tenx_v3.present_in_cell_sets.extend([t_cell_set_id, b_cell_set_id])
    
    # Create dataset
    dataset = Dataset(
        id=f"ds:{uuid.uuid4().hex[:8]}",
        name="Example immune cells dataset",
        description="A simple dataset with T cells and B cells for demonstration purposes",
        cell_sets=[t_cell_set_id, b_cell_set_id],
        cells=[],
        ontology_terms=[
            t_cell.id, b_cell.id, blood.id, healthy.id, adult.id, tenx_v3.id
        ]
    )
    
    # Return all created entities
    return {
        "dataset": dataset.dict(),
        "cell_sets": [t_cell_set.dict(), b_cell_set.dict()],
        "cell_types": [t_cell.dict(), b_cell.dict()],
        "tissues": [blood.dict()],
        "diseases": [healthy.dict()],
        "developmental_stages": [adult.dict()],
        "assays": [tenx_v3.dict()]
    }


def save_to_json(data: Dict[str, Any], output_file: str) -> None:
    """
    Save the data to a JSON file.
    
    Args:
        data: The data to save.
        output_file: The path to the output file.
    """
    print(f"Saving data to {output_file}...")
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {output_file}")


def main():
    """Main function."""
    output_file = "dataclass_example.json"
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    
    data = create_example_data()
    save_to_json(data, output_file)
    
    print("\nExample usage of the generated LinkML dataclasses:")
    print("1. Created CellType instances for T cells and B cells")
    print("2. Created Tissue, Disease, DevelopmentalStage, and Assay instances")
    print("3. Created CellSet instances linked to the ontology terms")
    print("4. Created a Dataset containing the cell sets")
    print("5. Serialized all data to JSON")
    print("\nThe dataclasses provide type-checking and validation according to the schema!")


if __name__ == "__main__":
    main()