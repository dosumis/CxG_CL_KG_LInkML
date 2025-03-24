
# Class: OntologyTerm

A term in an ontology.

URI: [sc_schema:OntologyTerm](https://w3id.org/single-cell-schema/OntologyTerm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Tissue],[Dataset]-%20ontology_terms%200..*>[OntologyTerm&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F;source_uri:uriorcurie%20%3F],[MetadataAssociation]-%20term%200..1>[OntologyTerm],[OntologyTerm]^-[Tissue],[OntologyTerm]^-[Disease],[OntologyTerm]^-[DevelopmentalStage],[OntologyTerm]^-[CellType],[OntologyTerm]^-[Assay],[MetadataAssociation],[Disease],[DevelopmentalStage],[Dataset],[CellType],[Assay])](https://yuml.me/diagram/nofunky;dir:TB/class/[Tissue],[Dataset]-%20ontology_terms%200..*>[OntologyTerm&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F;source_uri:uriorcurie%20%3F],[MetadataAssociation]-%20term%200..1>[OntologyTerm],[OntologyTerm]^-[Tissue],[OntologyTerm]^-[Disease],[OntologyTerm]^-[DevelopmentalStage],[OntologyTerm]^-[CellType],[OntologyTerm]^-[Assay],[MetadataAssociation],[Disease],[DevelopmentalStage],[Dataset],[CellType],[Assay])

## Children

 * [Assay](Assay.md) - An assay from the Experimental Factor Ontology.
 * [CellType](CellType.md) - A cell type from the Cell Ontology.
 * [DevelopmentalStage](DevelopmentalStage.md) - A developmental stage from the appropriate developmental stage ontology.
 * [Disease](Disease.md) - A disease from the Mondo Disease Ontology.
 * [Tissue](Tissue.md) - A tissue from the Uberon Ontology.

## Referenced by Class

 *  **None** *[ontology_terms](ontology_terms.md)*  <sub>0..\*</sub>  **[OntologyTerm](OntologyTerm.md)**
 *  **None** *[term](term.md)*  <sub>0..1</sub>  **[OntologyTerm](OntologyTerm.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an entity.
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description of an entity.
     * Range: [String](types/String.md)
 * [source_uri](source_uri.md)  <sub>0..1</sub>
     * Description: The URI of the source ontology term.
     * Range: [Uriorcurie](types/Uriorcurie.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | sc_schema:OntologyTerm |