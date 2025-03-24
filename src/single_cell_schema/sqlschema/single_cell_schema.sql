-- # Class: "CellSet" Description: "A set of cells sharing a common annotation in a named obs column."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an entity.
--     * Slot: description Description: A human-readable description of an entity.
--     * Slot: obs_column Description: The name of the observation column in the AnnData object.
--     * Slot: cell_count Description: The number of cells in the cell set.
--     * Slot: predominantly_consists_of Description: A cell type that this cell set predominantly consists of.
-- # Class: "OntologyTerm" Description: "A term in an ontology."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an entity.
--     * Slot: description Description: A human-readable description of an entity.
--     * Slot: source_uri Description: The URI of the source ontology term.
-- # Class: "MetadataAssociation" Description: "An association between a cell set and metadata with a cell count."
--     * Slot: id Description: 
--     * Slot: term Description: The ontology term.
--     * Slot: count Description: The number of cells with this metadata.
--     * Slot: CellSet_id Description: Autocreated FK slot
-- # Class: "CellType" Description: "A cell type from the Cell Ontology."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an entity.
--     * Slot: description Description: A human-readable description of an entity.
--     * Slot: source_uri Description: The URI of the source ontology term.
-- # Class: "Tissue" Description: "A tissue from the Uberon Ontology."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an entity.
--     * Slot: description Description: A human-readable description of an entity.
--     * Slot: source_uri Description: The URI of the source ontology term.
-- # Class: "Disease" Description: "A disease from the Mondo Disease Ontology."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an entity.
--     * Slot: description Description: A human-readable description of an entity.
--     * Slot: source_uri Description: The URI of the source ontology term.
-- # Class: "DevelopmentalStage" Description: "A developmental stage from the appropriate developmental stage ontology."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an entity.
--     * Slot: description Description: A human-readable description of an entity.
--     * Slot: source_uri Description: The URI of the source ontology term.
-- # Class: "Assay" Description: "An assay from the Experimental Factor Ontology."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an entity.
--     * Slot: description Description: A human-readable description of an entity.
--     * Slot: source_uri Description: The URI of the source ontology term.
-- # Class: "Cell" Description: "An individual cell in the dataset."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: CellSet_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: "Dataset" Description: "A single cell transcriptomics dataset."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an entity.
--     * Slot: description Description: A human-readable description of an entity.
-- # Class: "CellSet_subset_of" Description: ""
--     * Slot: CellSet_id Description: Autocreated FK slot
--     * Slot: subset_of_id Description: A cell set that this cell set is a subset of.
-- # Class: "CellType_predominantly_in" Description: ""
--     * Slot: CellType_id Description: Autocreated FK slot
--     * Slot: predominantly_in_id Description: A cell set that predominantly consists of this cell type.
-- # Class: "Tissue_present_in_cell_sets" Description: ""
--     * Slot: Tissue_id Description: Autocreated FK slot
--     * Slot: present_in_cell_sets_id Description: The cell sets that this ontology term is present in.
-- # Class: "Disease_present_in_cell_sets" Description: ""
--     * Slot: Disease_id Description: Autocreated FK slot
--     * Slot: present_in_cell_sets_id Description: The cell sets that this ontology term is present in.
-- # Class: "DevelopmentalStage_present_in_cell_sets" Description: ""
--     * Slot: DevelopmentalStage_id Description: Autocreated FK slot
--     * Slot: present_in_cell_sets_id Description: The cell sets that this ontology term is present in.
-- # Class: "Assay_present_in_cell_sets" Description: ""
--     * Slot: Assay_id Description: Autocreated FK slot
--     * Slot: present_in_cell_sets_id Description: The cell sets that this ontology term is present in.
-- # Class: "Cell_belongs_to_cell_sets" Description: ""
--     * Slot: Cell_id Description: Autocreated FK slot
--     * Slot: belongs_to_cell_sets_id Description: The cell sets that this cell belongs to.
-- # Class: "Dataset_cell_sets" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: cell_sets_id Description: The cell sets in the dataset.
-- # Class: "Dataset_ontology_terms" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: ontology_terms_id Description: The ontology terms used in the dataset.

CREATE TABLE "OntologyTerm" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	source_uri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "CellType" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	source_uri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Tissue" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	source_uri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Disease" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	source_uri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DevelopmentalStage" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	source_uri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Assay" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	source_uri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Dataset" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "CellSet" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	obs_column TEXT, 
	cell_count INTEGER, 
	predominantly_consists_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(predominantly_consists_of) REFERENCES "CellType" (id)
);
CREATE TABLE "Dataset_ontology_terms" (
	"Dataset_id" TEXT, 
	ontology_terms_id TEXT, 
	PRIMARY KEY ("Dataset_id", ontology_terms_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(ontology_terms_id) REFERENCES "OntologyTerm" (id)
);
CREATE TABLE "MetadataAssociation" (
	id INTEGER NOT NULL, 
	term TEXT, 
	count INTEGER, 
	"CellSet_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(term) REFERENCES "OntologyTerm" (id), 
	FOREIGN KEY("CellSet_id") REFERENCES "CellSet" (id)
);
CREATE TABLE "Cell" (
	id TEXT NOT NULL, 
	"CellSet_id" TEXT, 
	"Dataset_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("CellSet_id") REFERENCES "CellSet" (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "CellSet_subset_of" (
	"CellSet_id" TEXT, 
	subset_of_id TEXT, 
	PRIMARY KEY ("CellSet_id", subset_of_id), 
	FOREIGN KEY("CellSet_id") REFERENCES "CellSet" (id), 
	FOREIGN KEY(subset_of_id) REFERENCES "CellSet" (id)
);
CREATE TABLE "CellType_predominantly_in" (
	"CellType_id" TEXT, 
	predominantly_in_id TEXT, 
	PRIMARY KEY ("CellType_id", predominantly_in_id), 
	FOREIGN KEY("CellType_id") REFERENCES "CellType" (id), 
	FOREIGN KEY(predominantly_in_id) REFERENCES "CellSet" (id)
);
CREATE TABLE "Tissue_present_in_cell_sets" (
	"Tissue_id" TEXT, 
	present_in_cell_sets_id TEXT, 
	PRIMARY KEY ("Tissue_id", present_in_cell_sets_id), 
	FOREIGN KEY("Tissue_id") REFERENCES "Tissue" (id), 
	FOREIGN KEY(present_in_cell_sets_id) REFERENCES "CellSet" (id)
);
CREATE TABLE "Disease_present_in_cell_sets" (
	"Disease_id" TEXT, 
	present_in_cell_sets_id TEXT, 
	PRIMARY KEY ("Disease_id", present_in_cell_sets_id), 
	FOREIGN KEY("Disease_id") REFERENCES "Disease" (id), 
	FOREIGN KEY(present_in_cell_sets_id) REFERENCES "CellSet" (id)
);
CREATE TABLE "DevelopmentalStage_present_in_cell_sets" (
	"DevelopmentalStage_id" TEXT, 
	present_in_cell_sets_id TEXT, 
	PRIMARY KEY ("DevelopmentalStage_id", present_in_cell_sets_id), 
	FOREIGN KEY("DevelopmentalStage_id") REFERENCES "DevelopmentalStage" (id), 
	FOREIGN KEY(present_in_cell_sets_id) REFERENCES "CellSet" (id)
);
CREATE TABLE "Assay_present_in_cell_sets" (
	"Assay_id" TEXT, 
	present_in_cell_sets_id TEXT, 
	PRIMARY KEY ("Assay_id", present_in_cell_sets_id), 
	FOREIGN KEY("Assay_id") REFERENCES "Assay" (id), 
	FOREIGN KEY(present_in_cell_sets_id) REFERENCES "CellSet" (id)
);
CREATE TABLE "Dataset_cell_sets" (
	"Dataset_id" TEXT, 
	cell_sets_id TEXT, 
	PRIMARY KEY ("Dataset_id", cell_sets_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(cell_sets_id) REFERENCES "CellSet" (id)
);
CREATE TABLE "Cell_belongs_to_cell_sets" (
	"Cell_id" TEXT, 
	belongs_to_cell_sets_id TEXT, 
	PRIMARY KEY ("Cell_id", belongs_to_cell_sets_id), 
	FOREIGN KEY("Cell_id") REFERENCES "Cell" (id), 
	FOREIGN KEY(belongs_to_cell_sets_id) REFERENCES "CellSet" (id)
);