# Single Cell Transcriptomics LinkML Schema

A LinkML schema for representing single cell transcriptomics data following the CellXGene schema.

## Overview

This project provides a LinkML schema for modeling single cell transcriptomics data from AnnData (h5ad) files, following the [CellXGene schema](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/5.3.0/schema.md). It enables the representation of:

- Cell sets (groups of cells sharing a common annotation)
- Relationships between cell sets (subset relationships)
- Linking cell sets to ontology terms for cell types, tissues, diseases, developmental stages, and assays
- Recording metadata associations with cell counts

## Project Structure

This project has been structured following LinkML best practices:

```
├── README.md                 # Project documentation
├── setup.py                  # Package installation configuration
└── src/                      # Source code directory
    ├── data/                 # Data processing utilities
    │   ├── generate_sample_data.py     # Tool to generate sample AnnData files
    │   ├── populate_schema.py          # Tool to convert AnnData to LinkML instance data 
    │   ├── run_example.py              # End-to-end example script
    │   ├── validate_data.py            # Validation tool for LinkML instance data
    │   └── visualize_graph.py          # Knowledge graph visualization tool
    └── single_cell_schema/   # Schema and generated artifacts
        ├── docs/             # Markdown documentation for schema
        ├── excel/            # Excel representation of schema
        ├── graphql/          # GraphQL schema
        ├── jsonld/           # JSON-LD context
        ├── jsonschema/       # JSON Schema
        ├── owl/              # OWL/RDF representation
        ├── prefixmap/        # Prefix map
        ├── protobuf/         # Protocol Buffers schema
        ├── shacl/            # SHACL constraints
        ├── shex/             # ShEx schema
        ├── single_cell_schema.py  # Python dataclasses
        ├── single_cell_schema.yaml  # LinkML schema definition
        └── sqlschema/        # SQL schema
```

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

You can install this package directly from the repository:

```bash
# Clone the repository
git clone https://github.com/yourusername/CxG_CL_KG_LInkML.git
cd CxG_CL_KG_LInkML

# Install the package in development mode
pip install -e .
```

### Quick Start: Run the Example

The easiest way to get started is to run the example script, which demonstrates the complete workflow:

```bash
# Using the installed command line tool
sc-run-example

# Or using the Python module
python -m src.data.run_example
```

This script will:
1. Generate a sample AnnData file with synthetic single-cell data
2. Extract cell sets and relationships to populate the LinkML schema
3. Save the results to a JSON file
4. Display statistics about the generated knowledge graph

### Generating Sample Data

For testing purposes, you can generate a sample AnnData (h5ad) file using the provided tool:

```bash
# Using the installed command line tool
sc-gen-sample --output sample_data.h5ad --n-cells 1000 --n-genes 200

# Or using the Python module
python -m src.data.generate_sample_data --output sample_data.h5ad --n-cells 1000 --n-genes 200
```

This will create a realistic single-cell dataset with:
- 1000 cells and 200 genes (by default)
- Cell type annotations at two levels of granularity
- Tissue, disease, developmental stage, and assay annotations
- Dimension reduction embeddings (PCA, UMAP)

### Populating the Schema from an AnnData file

Use the populate-schema tool to extract data from an AnnData h5ad file and create a knowledge graph according to the schema:

```bash
# Using the installed command line tool
sc-populate-schema path/to/dataset.h5ad --output my_dataset.json

# Or using the Python module
python -m src.data.populate_schema path/to/dataset.h5ad --output my_dataset.json
```

### Validating the Schema

To validate that your data conforms to the LinkML schema:

```bash
# Using the installed command line tool
sc-validate sample_dataset.json

# Or using the Python module
python -m src.data.validate_data sample_dataset.json
```

This tool will check all entities and relationships to ensure they follow the schema constraints. If the data is valid, you'll see a success message. If there are validation errors, they will be displayed with details about what went wrong.

Command line options:
```
usage: sc-validate [-h] [--schema SCHEMA] [--verbose] data_file

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
# Using the installed command line tool
sc-visualize sample_dataset.json --output knowledge_graph.png

# Or using the Python module
python -m src.data.visualize_graph sample_dataset.json --output knowledge_graph.png
```

This will create a visual representation of the knowledge graph with:
- Different colors for different node types (cell sets, cell types, tissues, etc.)
- Different colors for different relationship types
- Node sizes proportional to cell counts
- Clear labels for all entities

Command line options:
```
usage: sc-visualize [-h] [--output OUTPUT] [--title TITLE] [--no-metadata] [--max-nodes MAX_NODES] [--verbose] data_file

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
sc-visualize sample_dataset.json --max-nodes 50
```

## Generated LinkML Artifacts

The LinkML project structure comes with various generated artifacts that can be used for different purposes:

### Python Data Classes

The schema generates Python dataclasses for programmatic data manipulation. We provide an example script that demonstrates how to use these dataclasses:

```bash
# Using the command line tool
sc-dataclass-example

# Or using the Python module
python -m src.data.dataclass_example

# This creates a sample dataset with:
# - T cells and B cells as cell types
# - Blood as a tissue
# - Healthy control as a disease
# - Adult as a developmental stage
# - 10x 3' v3 as an assay
# - Two cell sets linked to all these terms
```

The dataclasses provide type checking and validation according to the schema:

```python
from src.single_cell_schema.single_cell_schema import CellSet, CellType, Dataset, MetadataAssociation

# Create a cell set
cell_set = CellSet(
    id="cs:123",
    name="T cells",
    cell_count=1000,
    obs_column="cell_type",
    has_tissue=[
        MetadataAssociation(
            term="UBERON:0000178",  # blood
            count=1000
        )
    ]
)

# The dataclasses validate required fields and types
# For example, this would raise an error because cell_count must be an integer:
# cell_set = CellSet(id="cs:123", name="T cells", cell_count="1000")
```

### RDF/OWL Representation

The OWL representation (`src/single_cell_schema/owl/single_cell_schema.owl.ttl`) can be loaded into RDF triple stores for SPARQL querying or integrated with other ontologies.

### JSON Schema

The JSON Schema representation (`src/single_cell_schema/jsonschema/single_cell_schema.schema.json`) can be used for validating JSON data against the schema.

### GraphQL Schema

The GraphQL schema (`src/single_cell_schema/graphql/single_cell_schema.graphql`) can be used to set up a GraphQL API for querying the data.

### SQL Schema

The SQL schema (`src/single_cell_schema/sqlschema/single_cell_schema.sql`) can be used to create a relational database to store the data.

## Schema Details

The schema is defined in `src/single_cell_schema/single_cell_schema.yaml` and follows the LinkML specification.

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

## Command-line Tools

After installation, the following command-line tools are available:

| Command | Description |
|---------|-------------|
| `sc-gen-sample` | Generate a sample AnnData (h5ad) file for testing |
| `sc-populate-schema` | Extract data from an AnnData file and populate the LinkML schema |
| `sc-validate` | Validate that data conforms to the LinkML schema |
| `sc-visualize` | Create a visualization of the knowledge graph |
| `sc-run-example` | Run an end-to-end example workflow |
| `sc-dataclass-example` | Demonstrate using the generated Python dataclasses |

## Future Work

Some potential enhancements to consider:

1. **Integration with existing data portals**: Interface with the CellXGene Data Portal and other single-cell repositories to import data directly.

2. **Graph database support**: Add exporters for graph databases like Neo4j, to enable more powerful querying of the knowledge graph.

3. **Web-based visualization**: Create a web application to interactively explore the cell set relationships and metadata.

4. **Inference capabilities**: Add support for inferring additional relationships based on the ontology hierarchies.

5. **Data standardization**: Add more validation rules to ensure data quality and consistency.

## License

MIT