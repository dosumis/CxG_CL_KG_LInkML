
# Class: Cell

An individual cell in the dataset.

URI: [sc_schema:Cell](https://w3id.org/single-cell-schema/Cell)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CellSet],[CellSet]<belongs_to_cell_sets%200..*-%20[Cell&#124;id:uriorcurie],[CellSet]++-%20cells%200..*>[Cell],[Dataset]++-%20cells%200..*>[Cell],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[CellSet],[CellSet]<belongs_to_cell_sets%200..*-%20[Cell&#124;id:uriorcurie],[CellSet]++-%20cells%200..*>[Cell],[Dataset]++-%20cells%200..*>[Cell],[Dataset])

## Referenced by Class

 *  **None** *[cells](cells.md)*  <sub>0..\*</sub>  **[Cell](Cell.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [belongs_to_cell_sets](belongs_to_cell_sets.md)  <sub>0..\*</sub>
     * Description: The cell sets that this cell belongs to.
     * Range: [CellSet](CellSet.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | sc_schema:Cell |