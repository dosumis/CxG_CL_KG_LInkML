#!/usr/bin/env python
"""
Validate that a generated dataset conforms to the LinkML schema.
"""

import argparse
import json
import logging
import os
import sys
import yaml
from typing import Dict, Any, List, Optional, Union

from linkml_runtime.loaders import json_loader, yaml_loader
from linkml_runtime.validators.jsonschemavalidator import JsonSchemaValidator
from linkml_runtime.utils.schemaview import SchemaView

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


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


def validate_dataset(data: Dict[str, Any], schema_file: str) -> List[str]:
    """
    Validate a dataset against the LinkML schema.
    
    Args:
        data: The dataset to validate.
        schema_file: Path to the LinkML schema file.
        
    Returns:
        A list of validation errors, if any.
    """
    logger.info(f"Validating data against schema: {schema_file}")
    
    # Load the schema
    schema_view = SchemaView(schema_file)
    
    # Create the validator
    validator = JsonSchemaValidator(schema_view)
    
    # Validate each component
    errors = []
    
    # Validate dataset
    if 'dataset' in data:
        dataset_errors = validator.validate(data['dataset'], 'Dataset')
        errors.extend([f"Dataset: {e}" for e in dataset_errors])
    
    # Validate cell sets
    if 'cell_sets' in data:
        for i, cell_set in enumerate(data['cell_sets']):
            cell_set_errors = validator.validate(cell_set, 'CellSet')
            errors.extend([f"CellSet {i} ({cell_set.get('id', 'unknown')}): {e}" for e in cell_set_errors])
    
    # Validate cell types
    if 'cell_types' in data:
        for i, cell_type in enumerate(data['cell_types']):
            cell_type_errors = validator.validate(cell_type, 'CellType')
            errors.extend([f"CellType {i} ({cell_type.get('id', 'unknown')}): {e}" for e in cell_type_errors])
    
    # Validate tissues
    if 'tissues' in data:
        for i, tissue in enumerate(data['tissues']):
            tissue_errors = validator.validate(tissue, 'Tissue')
            errors.extend([f"Tissue {i} ({tissue.get('id', 'unknown')}): {e}" for e in tissue_errors])
    
    # Validate diseases
    if 'diseases' in data:
        for i, disease in enumerate(data['diseases']):
            disease_errors = validator.validate(disease, 'Disease')
            errors.extend([f"Disease {i} ({disease.get('id', 'unknown')}): {e}" for e in disease_errors])
    
    # Validate developmental stages
    if 'developmental_stages' in data:
        for i, dev_stage in enumerate(data['developmental_stages']):
            dev_stage_errors = validator.validate(dev_stage, 'DevelopmentalStage')
            errors.extend([f"DevelopmentalStage {i} ({dev_stage.get('id', 'unknown')}): {e}" for e in dev_stage_errors])
    
    # Validate assays
    if 'assays' in data:
        for i, assay in enumerate(data['assays']):
            assay_errors = validator.validate(assay, 'Assay')
            errors.extend([f"Assay {i} ({assay.get('id', 'unknown')}): {e}" for e in assay_errors])
    
    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate data against the LinkML schema")
    parser.add_argument("data_file", help="Path to the data file (JSON or YAML)")
    parser.add_argument("--schema", "-s", default="single_cell_schema.yaml", 
                        help="Path to the LinkML schema file (default: single_cell_schema.yaml)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Check if the schema file exists
    if not os.path.exists(args.schema):
        logger.error(f"Schema file not found: {args.schema}")
        sys.exit(1)
    
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
    
    # Validate the data
    try:
        errors = validate_dataset(data, args.schema)
    except Exception as e:
        logger.error(f"Validation error: {e}")
        sys.exit(1)
    
    # Report results
    if errors:
        logger.error(f"Found {len(errors)} validation errors:")
        for i, error in enumerate(errors, 1):
            logger.error(f"{i}. {error}")
        sys.exit(1)
    else:
        logger.info("Validation successful! No errors found.")
        print("✅ Data is valid according to the schema.")


if __name__ == "__main__":
    main()