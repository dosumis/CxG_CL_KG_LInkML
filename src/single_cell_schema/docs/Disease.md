
# Class: Disease

A disease from the Mondo Disease Ontology.

URI: [sc_schema:Disease](https://w3id.org/single-cell-schema/Disease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm],[CellSet]<present_in_cell_sets%200..*-%20[Disease&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F;source_uri(i):uriorcurie%20%3F],[OntologyTerm]^-[Disease],[CellSet])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm],[CellSet]<present_in_cell_sets%200..*-%20[Disease&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F;source_uri(i):uriorcurie%20%3F],[OntologyTerm]^-[Disease],[CellSet])

## Parents

 *  is_a: [OntologyTerm](OntologyTerm.md) - A term in an ontology.

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
 * [present_in_cell_sets](present_in_cell_sets.md)  <sub>0..\*</sub>
     * Description: The cell sets that this ontology term is present in.
     * Range: [CellSet](CellSet.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | sc_schema:Disease |