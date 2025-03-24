
# Class: CellType

A cell type from the Cell Ontology.

URI: [sc_schema:CellType](https://w3id.org/single-cell-schema/CellType)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm],[CellSet]<predominantly_in%200..*-%20[CellType&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F;source_uri(i):uriorcurie%20%3F],[CellSet]-%20predominantly_consists_of%200..1>[CellType],[OntologyTerm]^-[CellType],[CellSet])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm],[CellSet]<predominantly_in%200..*-%20[CellType&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F;source_uri(i):uriorcurie%20%3F],[CellSet]-%20predominantly_consists_of%200..1>[CellType],[OntologyTerm]^-[CellType],[CellSet])

## Parents

 *  is_a: [OntologyTerm](OntologyTerm.md) - A term in an ontology.

## Referenced by Class

 *  **None** *[predominantly_consists_of](predominantly_consists_of.md)*  <sub>0..1</sub>  **[CellType](CellType.md)**

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
 * [predominantly_in](predominantly_in.md)  <sub>0..\*</sub>
     * Description: A cell set that predominantly consists of this cell type.
     * Range: [CellSet](CellSet.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | sc_schema:CellType |