
# Class: Dataset

A single cell transcriptomics dataset.

URI: [sc_schema:Dataset](https://w3id.org/single-cell-schema/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm],[OntologyTerm]<ontology_terms%200..*-%20[Dataset&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F],[Cell]<cells%200..*-++[Dataset],[CellSet]<cell_sets%200..*-%20[Dataset],[CellSet],[Cell])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm],[OntologyTerm]<ontology_terms%200..*-%20[Dataset&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F],[Cell]<cells%200..*-++[Dataset],[CellSet]<cell_sets%200..*-%20[Dataset],[CellSet],[Cell])

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
 * [cell_sets](cell_sets.md)  <sub>0..\*</sub>
     * Description: The cell sets in the dataset.
     * Range: [CellSet](CellSet.md)
 * [cells](cells.md)  <sub>0..\*</sub>
     * Description: The cells in the cell set.
     * Range: [Cell](Cell.md)
 * [ontology_terms](ontology_terms.md)  <sub>0..\*</sub>
     * Description: The ontology terms used in the dataset.
     * Range: [OntologyTerm](OntologyTerm.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | sc_schema:Dataset |