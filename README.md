# Single Cell Transcriptomics LinkML Schema

A LinkML schema for representing single cell transcriptomics data following the CellXGene schema.

## Overview

This project provides a LinkML schema for modeling single cell transcriptomics data from AnnData (h5ad) files, following the [CellXGene schema](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/5.3.0/schema.md). It enables the representation of:

- Cell sets (groups of cells sharing a common annotation)
- Relationships between cell sets (subset relationships)
- Linking cell sets to ontology terms for cell types, tissues, diseases, developmental stages, and assays
- Recording metadata associations with cell counts

## Schema Design

The schema is designed around these key entities:

- **CellSet**: A set of cells sharing a common annotation in a named observation column
- **CellType**: A cell type from the Cell Ontology
- **Tissue**: A tissue from the Uberon Ontology
- **Disease**: A disease from the Mondo Disease Ontology
- **DevelopmentalStage**: A developmental stage from the appropriate developmental stage ontology
- **Assay**: An assay from the Experimental Factor Ontology
- **Dataset**: A container for all data from a single cell transcriptomics experiment

Key relationships include:
- `subset_of`: Indicates one cell set is a subset of another
- `predominantly_consists_of`: Links a cell set to its primary cell type
- Metadata associations (`has_tissue`, `has_disease`, `has_developmental_stage`, `has_assay`): Link cell sets to metadata terms with cell counts

## Usage

### Requirements

- Python 3.8+
- Required packages: `linkml`, `anndata`, `scanpy`, `numpy`, `pandas`

### Installation

```bash
pip install linkml anndata scanpy
```

### Quick Start: Run the Example

The easiest way to get started is to run the example script, which demonstrates the complete workflow:

```bash
python run_example.py
```

This script will:
1. Generate a sample AnnData file with synthetic single-cell data
2. Extract cell sets and relationships to populate the LinkML schema
3. Save the results to a JSON file
4. Display statistics about the generated knowledge graph

### Generating Sample Data

For testing purposes, you can generate a sample AnnData (h5ad) file using the provided script:

```bash
python generate_sample_data.py --output sample_data.h5ad --n-cells 1000 --n-genes 200
```

This will create a realistic single-cell dataset with:
- 1000 cells and 200 genes (by default)
- Cell type annotations at two levels of granularity
- Tissue, disease, developmental stage, and assay annotations
- Dimension reduction embeddings (PCA, UMAP)

### Populating the Schema from an AnnData file

Use the `populate_schema.py` script to extract data from an AnnData h5ad file and create a knowledge graph according to the schema:

```bash
# If you have your own h5ad file:
python populate_schema.py path/to/dataset.h5ad --output my_dataset.json

# Or using the generated sample data:
python populate_schema.py sample_data.h5ad --output sample_dataset.json
```

### Validating the Schema

To validate that your data conforms to the LinkML schema:

```bash
python validate_data.py sample_dataset.json
```

This tool will check all entities and relationships to ensure they follow the schema constraints. If the data is valid, you'll see a success message. If there are validation errors, they will be displayed with details about what went wrong.

Command line options:
```
usage: validate_data.py [-h] [--schema SCHEMA] [--verbose] data_file

Validate data against the LinkML schema

positional arguments:
  data_file             Path to the data file (JSON or YAML)

optional arguments:
  -h, --help            show this help message and exit
  --schema SCHEMA, -s SCHEMA
                        Path to the LinkML schema file (default: single_cell_schema.yaml)
  --verbose, -v         Enable verbose output
```

### Visualizing the Knowledge Graph

To visualize the relationships in your data as a knowledge graph:

```bash
python visualize_graph.py sample_dataset.json --output knowledge_graph.png
```

This will create a visual representation of the knowledge graph with:
- Different colors for different node types (cell sets, cell types, tissues, etc.)
- Different colors for different relationship types
- Node sizes proportional to cell counts
- Clear labels for all entities

Command line options:
```
usage: visualize_graph.py [-h] [--output OUTPUT] [--title TITLE] [--no-metadata] [--max-nodes MAX_NODES] [--verbose] data_file

Visualize the knowledge graph from single cell transcriptomics data

positional arguments:
  data_file             Path to the data file (JSON or YAML)

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Path to the output image file (default: knowledge_graph.png)
  --title TITLE, -t TITLE
                        Title for the plot (default: 'Single Cell Transcriptomics Knowledge Graph')
  --no-metadata         Do not include metadata nodes (tissues, diseases, etc.)
  --max-nodes MAX_NODES
                        Maximum number of nodes to include in the graph
  --verbose, -v         Enable verbose output
```

For large datasets, you may want to limit the visualization to a subset of nodes:

```bash
python visualize_graph.py sample_dataset.json --max-nodes 50
```

#### Command Line Options

```
usage: populate_schema.py [-h] [--output OUTPUT] [--format {json,yaml}]
                          [--dataset-name DATASET_NAME]
                          [--cell-type-columns CELL_TYPE_COLUMNS [CELL_TYPE_COLUMNS ...]]
                          [--tissue-column TISSUE_COLUMN]
                          [--disease-column DISEASE_COLUMN]
                          [--dev-stage-column DEV_STAGE_COLUMN]
                          [--assay-column ASSAY_COLUMN]
                          input_file

Populate single cell transcriptomics schema from AnnData (h5ad) files

positional arguments:
  input_file            Path to the input h5ad file

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Path to the output file (default: dataset.json)
  --format {json,yaml}, -f {json,yaml}
                        Output format (default: json)
  --dataset-name DATASET_NAME
                        Name of the dataset (default: derived from input filename)
  --cell-type-columns CELL_TYPE_COLUMNS [CELL_TYPE_COLUMNS ...]
                        Column names in AnnData.obs that contain cell type annotations
                        (default: ['cell_type', 'cell_ontology_term'])
  --tissue-column TISSUE_COLUMN
                        Column name in AnnData.obs that contains tissue annotations
                        (default: 'tissue')
  --disease-column DISEASE_COLUMN
                        Column name in AnnData.obs that contains disease annotations
                        (default: 'disease')
  --dev-stage-column DEV_STAGE_COLUMN
                        Column name in AnnData.obs that contains developmental stage annotations
                        (default: 'development_stage')
  --assay-column ASSAY_COLUMN
                        Column name in AnnData.obs that contains assay annotations
                        (default: 'assay')
```

## Schema Details

The schema is defined in `single_cell_schema.yaml` and follows the LinkML specification.

### Key Classes

- **CellSet**: Represents a group of cells sharing a common annotation
- **OntologyTerm**: Abstract parent class for ontology terms
- **CellType**, **Tissue**, **Disease**, **DevelopmentalStage**, **Assay**: Specific ontology term types
- **MetadataAssociation**: Links a cell set to an ontology term with a cell count
- **Cell**: Represents an individual cell
- **Dataset**: The top-level container

### Prefixes and Namespaces

The schema includes prefixes for key ontologies:
- Cell Ontology (CL)
- Uberon Anatomy Ontology (UBERON)
- Mondo Disease Ontology (MONDO)
- Experimental Factor Ontology (EFO)
- Human and Mouse developmental stage ontologies (HsapDv, MmusDv)

## License

MIT