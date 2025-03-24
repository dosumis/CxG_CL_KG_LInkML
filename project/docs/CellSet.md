
# Class: CellSet

A set of cells sharing a common annotation in a named obs column.

URI: [sc_schema:CellSet](https://w3id.org/single-cell-schema/CellSet)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MetadataAssociation],[CellType],[MetadataAssociation]<has_assay%200..*-++[CellSet&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F;obs_column:string%20%3F;cell_count:integer%20%3F],[MetadataAssociation]<has_developmental_stage%200..*-++[CellSet],[MetadataAssociation]<has_disease%200..*-++[CellSet],[MetadataAssociation]<has_tissue%200..*-++[CellSet],[CellType]<predominantly_consists_of%200..1-%20[CellSet],[CellSet]<subset_of%200..*-%20[CellSet],[Cell]<cells%200..*-++[CellSet],[Cell]-%20belongs_to_cell_sets%200..*>[CellSet],[Dataset]-%20cell_sets%200..*>[CellSet],[CellType]-%20predominantly_in%200..*>[CellSet],[Tissue]-%20present_in_cell_sets%200..*>[CellSet],[Disease]-%20present_in_cell_sets%200..*>[CellSet],[DevelopmentalStage]-%20present_in_cell_sets%200..*>[CellSet],[Assay]-%20present_in_cell_sets%200..*>[CellSet],[Tissue],[Disease],[DevelopmentalStage],[Dataset],[Cell],[Assay])](https://yuml.me/diagram/nofunky;dir:TB/class/[MetadataAssociation],[CellType],[MetadataAssociation]<has_assay%200..*-++[CellSet&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F;obs_column:string%20%3F;cell_count:integer%20%3F],[MetadataAssociation]<has_developmental_stage%200..*-++[CellSet],[MetadataAssociation]<has_disease%200..*-++[CellSet],[MetadataAssociation]<has_tissue%200..*-++[CellSet],[CellType]<predominantly_consists_of%200..1-%20[CellSet],[CellSet]<subset_of%200..*-%20[CellSet],[Cell]<cells%200..*-++[CellSet],[Cell]-%20belongs_to_cell_sets%200..*>[CellSet],[Dataset]-%20cell_sets%200..*>[CellSet],[CellType]-%20predominantly_in%200..*>[CellSet],[Tissue]-%20present_in_cell_sets%200..*>[CellSet],[Disease]-%20present_in_cell_sets%200..*>[CellSet],[DevelopmentalStage]-%20present_in_cell_sets%200..*>[CellSet],[Assay]-%20present_in_cell_sets%200..*>[CellSet],[Tissue],[Disease],[DevelopmentalStage],[Dataset],[Cell],[Assay])

## Referenced by Class

 *  **None** *[belongs_to_cell_sets](belongs_to_cell_sets.md)*  <sub>0..\*</sub>  **[CellSet](CellSet.md)**
 *  **None** *[cell_sets](cell_sets.md)*  <sub>0..\*</sub>  **[CellSet](CellSet.md)**
 *  **None** *[predominantly_in](predominantly_in.md)*  <sub>0..\*</sub>  **[CellSet](CellSet.md)**
 *  **None** *[present_in_cell_sets](present_in_cell_sets.md)*  <sub>0..\*</sub>  **[CellSet](CellSet.md)**
 *  **None** *[subset_of](subset_of.md)*  <sub>0..\*</sub>  **[CellSet](CellSet.md)**

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
 * [obs_column](obs_column.md)  <sub>0..1</sub>
     * Description: The name of the observation column in the AnnData object.
     * Range: [String](types/String.md)
 * [cell_count](cell_count.md)  <sub>0..1</sub>
     * Description: The number of cells in the cell set.
     * Range: [Integer](types/Integer.md)
 * [cells](cells.md)  <sub>0..\*</sub>
     * Description: The cells in the cell set.
     * Range: [Cell](Cell.md)
 * [subset_of](subset_of.md)  <sub>0..\*</sub>
     * Description: A cell set that this cell set is a subset of.
     * Range: [CellSet](CellSet.md)
 * [predominantly_consists_of](predominantly_consists_of.md)  <sub>0..1</sub>
     * Description: A cell type that this cell set predominantly consists of.
     * Range: [CellType](CellType.md)
 * [has_tissue](has_tissue.md)  <sub>0..\*</sub>
     * Description: The tissue associated with this cell set, with cell count.
     * Range: [MetadataAssociation](MetadataAssociation.md)
 * [has_disease](has_disease.md)  <sub>0..\*</sub>
     * Description: The disease associated with this cell set, with cell count.
     * Range: [MetadataAssociation](MetadataAssociation.md)
 * [has_developmental_stage](has_developmental_stage.md)  <sub>0..\*</sub>
     * Description: The developmental stage associated with this cell set, with cell count.
     * Range: [MetadataAssociation](MetadataAssociation.md)
 * [has_assay](has_assay.md)  <sub>0..\*</sub>
     * Description: The assay associated with this cell set, with cell count.
     * Range: [MetadataAssociation](MetadataAssociation.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | sc_schema:CellSet |