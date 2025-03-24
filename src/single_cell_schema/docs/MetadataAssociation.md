
# Class: MetadataAssociation

An association between a cell set and metadata with a cell count.

URI: [sc_schema:MetadataAssociation](https://w3id.org/single-cell-schema/MetadataAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm],[OntologyTerm]<term%200..1-%20[MetadataAssociation&#124;count:integer%20%3F],[CellSet]++-%20has_assay%200..*>[MetadataAssociation],[CellSet]++-%20has_developmental_stage%200..*>[MetadataAssociation],[CellSet]++-%20has_disease%200..*>[MetadataAssociation],[CellSet]++-%20has_tissue%200..*>[MetadataAssociation],[CellSet])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm],[OntologyTerm]<term%200..1-%20[MetadataAssociation&#124;count:integer%20%3F],[CellSet]++-%20has_assay%200..*>[MetadataAssociation],[CellSet]++-%20has_developmental_stage%200..*>[MetadataAssociation],[CellSet]++-%20has_disease%200..*>[MetadataAssociation],[CellSet]++-%20has_tissue%200..*>[MetadataAssociation],[CellSet])

## Referenced by Class

 *  **None** *[has_assay](has_assay.md)*  <sub>0..\*</sub>  **[MetadataAssociation](MetadataAssociation.md)**
 *  **None** *[has_developmental_stage](has_developmental_stage.md)*  <sub>0..\*</sub>  **[MetadataAssociation](MetadataAssociation.md)**
 *  **None** *[has_disease](has_disease.md)*  <sub>0..\*</sub>  **[MetadataAssociation](MetadataAssociation.md)**
 *  **None** *[has_tissue](has_tissue.md)*  <sub>0..\*</sub>  **[MetadataAssociation](MetadataAssociation.md)**

## Attributes


### Own

 * [term](term.md)  <sub>0..1</sub>
     * Description: The ontology term.
     * Range: [OntologyTerm](OntologyTerm.md)
 * [count](count.md)  <sub>0..1</sub>
     * Description: The number of cells with this metadata.
     * Range: [Integer](types/Integer.md)
