
# single-cell-schema


**metamodel version:** 1.7.0

**version:** 0.1.0


A LinkML schema for representing single cell transcriptomics data following the CellXGene schema.


### Classes

 * [Cell](Cell.md) - An individual cell in the dataset.
 * [CellSet](CellSet.md) - A set of cells sharing a common annotation in a named obs column.
 * [Dataset](Dataset.md) - A single cell transcriptomics dataset.
 * [MetadataAssociation](MetadataAssociation.md) - An association between a cell set and metadata with a cell count.
 * [OntologyTerm](OntologyTerm.md) - A term in an ontology.
     * [Assay](Assay.md) - An assay from the Experimental Factor Ontology.
     * [CellType](CellType.md) - A cell type from the Cell Ontology.
     * [DevelopmentalStage](DevelopmentalStage.md) - A developmental stage from the appropriate developmental stage ontology.
     * [Disease](Disease.md) - A disease from the Mondo Disease Ontology.
     * [Tissue](Tissue.md) - A tissue from the Uberon Ontology.

### Mixins


### Slots

 * [belongs_to_cell_sets](belongs_to_cell_sets.md) - The cell sets that this cell belongs to.
 * [cell_count](cell_count.md) - The number of cells in the cell set.
 * [cell_sets](cell_sets.md) - The cell sets in the dataset.
 * [cells](cells.md) - The cells in the cell set.
 * [count](count.md) - The number of cells with this metadata.
 * [description](description.md) - A human-readable description of an entity.
 * [has_assay](has_assay.md) - The assay associated with this cell set, with cell count.
 * [has_developmental_stage](has_developmental_stage.md) - The developmental stage associated with this cell set, with cell count.
 * [has_disease](has_disease.md) - The disease associated with this cell set, with cell count.
 * [has_tissue](has_tissue.md) - The tissue associated with this cell set, with cell count.
 * [id](id.md) - A unique identifier for an entity.
 * [name](name.md) - A human-readable name for an entity.
 * [obs_column](obs_column.md) - The name of the observation column in the AnnData object.
 * [ontology_terms](ontology_terms.md) - The ontology terms used in the dataset.
 * [predominantly_consists_of](predominantly_consists_of.md) - A cell type that this cell set predominantly consists of.
 * [predominantly_in](predominantly_in.md) - A cell set that predominantly consists of this cell type.
 * [present_in_cell_sets](present_in_cell_sets.md) - The cell sets that this ontology term is present in.
 * [source_uri](source_uri.md) - The URI of the source ontology term.
 * [subset_of](subset_of.md) - A cell set that this cell set is a subset of.
 * [term](term.md) - The ontology term.

### Enums


### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
