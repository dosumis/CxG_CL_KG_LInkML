# Auto generated from single_cell_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-24T09:08:29
# Schema: single-cell-schema
#
# id: https://w3id.org/single-cell-schema
# description: A LinkML schema for representing single cell transcriptomics data following the CellXGene schema.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = "0.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CVCL = CurieNamespace('CVCL', 'http://purl.obolibrary.org/obo/CVCL_')
EFO = CurieNamespace('EFO', 'http://purl.obolibrary.org/obo/EFO_')
HSAPDV = CurieNamespace('HsapDv', 'http://purl.obolibrary.org/obo/HsapDv_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
MMUSDV = CurieNamespace('MmusDv', 'http://purl.obolibrary.org/obo/MmusDv_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SC_SCHEMA = CurieNamespace('sc_schema', 'https://w3id.org/single-cell-schema/')
DEFAULT_ = SC_SCHEMA


# Types

# Class references
class CellSetId(URIorCURIE):
    pass


class OntologyTermId(URIorCURIE):
    pass


class CellTypeId(OntologyTermId):
    pass


class TissueId(OntologyTermId):
    pass


class DiseaseId(OntologyTermId):
    pass


class DevelopmentalStageId(OntologyTermId):
    pass


class AssayId(OntologyTermId):
    pass


class CellId(URIorCURIE):
    pass


class DatasetId(URIorCURIE):
    pass


@dataclass(repr=False)
class CellSet(YAMLRoot):
    """
    A set of cells sharing a common annotation in a named obs column.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SC_SCHEMA["CellSet"]
    class_class_curie: ClassVar[str] = "sc_schema:CellSet"
    class_name: ClassVar[str] = "CellSet"
    class_model_uri: ClassVar[URIRef] = SC_SCHEMA.CellSet

    id: Union[str, CellSetId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    obs_column: Optional[str] = None
    cell_count: Optional[int] = None
    cells: Optional[Union[Dict[Union[str, CellId], Union[dict, "Cell"]], List[Union[dict, "Cell"]]]] = empty_dict()
    subset_of: Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]] = empty_list()
    predominantly_consists_of: Optional[Union[str, CellTypeId]] = None
    has_tissue: Optional[Union[Union[dict, "MetadataAssociation"], List[Union[dict, "MetadataAssociation"]]]] = empty_list()
    has_disease: Optional[Union[Union[dict, "MetadataAssociation"], List[Union[dict, "MetadataAssociation"]]]] = empty_list()
    has_developmental_stage: Optional[Union[Union[dict, "MetadataAssociation"], List[Union[dict, "MetadataAssociation"]]]] = empty_list()
    has_assay: Optional[Union[Union[dict, "MetadataAssociation"], List[Union[dict, "MetadataAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellSetId):
            self.id = CellSetId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.obs_column is not None and not isinstance(self.obs_column, str):
            self.obs_column = str(self.obs_column)

        if self.cell_count is not None and not isinstance(self.cell_count, int):
            self.cell_count = int(self.cell_count)

        self._normalize_inlined_as_list(slot_name="cells", slot_type=Cell, key_name="id", keyed=True)

        if not isinstance(self.subset_of, list):
            self.subset_of = [self.subset_of] if self.subset_of is not None else []
        self.subset_of = [v if isinstance(v, CellSetId) else CellSetId(v) for v in self.subset_of]

        if self.predominantly_consists_of is not None and not isinstance(self.predominantly_consists_of, CellTypeId):
            self.predominantly_consists_of = CellTypeId(self.predominantly_consists_of)

        if not isinstance(self.has_tissue, list):
            self.has_tissue = [self.has_tissue] if self.has_tissue is not None else []
        self.has_tissue = [v if isinstance(v, MetadataAssociation) else MetadataAssociation(**as_dict(v)) for v in self.has_tissue]

        if not isinstance(self.has_disease, list):
            self.has_disease = [self.has_disease] if self.has_disease is not None else []
        self.has_disease = [v if isinstance(v, MetadataAssociation) else MetadataAssociation(**as_dict(v)) for v in self.has_disease]

        if not isinstance(self.has_developmental_stage, list):
            self.has_developmental_stage = [self.has_developmental_stage] if self.has_developmental_stage is not None else []
        self.has_developmental_stage = [v if isinstance(v, MetadataAssociation) else MetadataAssociation(**as_dict(v)) for v in self.has_developmental_stage]

        if not isinstance(self.has_assay, list):
            self.has_assay = [self.has_assay] if self.has_assay is not None else []
        self.has_assay = [v if isinstance(v, MetadataAssociation) else MetadataAssociation(**as_dict(v)) for v in self.has_assay]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologyTerm(YAMLRoot):
    """
    A term in an ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SC_SCHEMA["OntologyTerm"]
    class_class_curie: ClassVar[str] = "sc_schema:OntologyTerm"
    class_name: ClassVar[str] = "OntologyTerm"
    class_model_uri: ClassVar[URIRef] = SC_SCHEMA.OntologyTerm

    id: Union[str, OntologyTermId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyTermId):
            self.id = OntologyTermId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetadataAssociation(YAMLRoot):
    """
    An association between a cell set and metadata with a cell count.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SC_SCHEMA["MetadataAssociation"]
    class_class_curie: ClassVar[str] = "sc_schema:MetadataAssociation"
    class_name: ClassVar[str] = "MetadataAssociation"
    class_model_uri: ClassVar[URIRef] = SC_SCHEMA.MetadataAssociation

    term: Optional[Union[str, OntologyTermId]] = None
    count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.term is not None and not isinstance(self.term, OntologyTermId):
            self.term = OntologyTermId(self.term)

        if self.count is not None and not isinstance(self.count, int):
            self.count = int(self.count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellType(OntologyTerm):
    """
    A cell type from the Cell Ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SC_SCHEMA["CellType"]
    class_class_curie: ClassVar[str] = "sc_schema:CellType"
    class_name: ClassVar[str] = "CellType"
    class_model_uri: ClassVar[URIRef] = SC_SCHEMA.CellType

    id: Union[str, CellTypeId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    predominantly_in: Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellTypeId):
            self.id = CellTypeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if not isinstance(self.predominantly_in, list):
            self.predominantly_in = [self.predominantly_in] if self.predominantly_in is not None else []
        self.predominantly_in = [v if isinstance(v, CellSetId) else CellSetId(v) for v in self.predominantly_in]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tissue(OntologyTerm):
    """
    A tissue from the Uberon Ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SC_SCHEMA["Tissue"]
    class_class_curie: ClassVar[str] = "sc_schema:Tissue"
    class_name: ClassVar[str] = "Tissue"
    class_model_uri: ClassVar[URIRef] = SC_SCHEMA.Tissue

    id: Union[str, TissueId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    present_in_cell_sets: Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TissueId):
            self.id = TissueId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if not isinstance(self.present_in_cell_sets, list):
            self.present_in_cell_sets = [self.present_in_cell_sets] if self.present_in_cell_sets is not None else []
        self.present_in_cell_sets = [v if isinstance(v, CellSetId) else CellSetId(v) for v in self.present_in_cell_sets]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disease(OntologyTerm):
    """
    A disease from the Mondo Disease Ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SC_SCHEMA["Disease"]
    class_class_curie: ClassVar[str] = "sc_schema:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = SC_SCHEMA.Disease

    id: Union[str, DiseaseId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    present_in_cell_sets: Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if not isinstance(self.present_in_cell_sets, list):
            self.present_in_cell_sets = [self.present_in_cell_sets] if self.present_in_cell_sets is not None else []
        self.present_in_cell_sets = [v if isinstance(v, CellSetId) else CellSetId(v) for v in self.present_in_cell_sets]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DevelopmentalStage(OntologyTerm):
    """
    A developmental stage from the appropriate developmental stage ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SC_SCHEMA["DevelopmentalStage"]
    class_class_curie: ClassVar[str] = "sc_schema:DevelopmentalStage"
    class_name: ClassVar[str] = "DevelopmentalStage"
    class_model_uri: ClassVar[URIRef] = SC_SCHEMA.DevelopmentalStage

    id: Union[str, DevelopmentalStageId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    present_in_cell_sets: Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DevelopmentalStageId):
            self.id = DevelopmentalStageId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if not isinstance(self.present_in_cell_sets, list):
            self.present_in_cell_sets = [self.present_in_cell_sets] if self.present_in_cell_sets is not None else []
        self.present_in_cell_sets = [v if isinstance(v, CellSetId) else CellSetId(v) for v in self.present_in_cell_sets]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assay(OntologyTerm):
    """
    An assay from the Experimental Factor Ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SC_SCHEMA["Assay"]
    class_class_curie: ClassVar[str] = "sc_schema:Assay"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = SC_SCHEMA.Assay

    id: Union[str, AssayId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    present_in_cell_sets: Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssayId):
            self.id = AssayId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if not isinstance(self.present_in_cell_sets, list):
            self.present_in_cell_sets = [self.present_in_cell_sets] if self.present_in_cell_sets is not None else []
        self.present_in_cell_sets = [v if isinstance(v, CellSetId) else CellSetId(v) for v in self.present_in_cell_sets]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Cell(YAMLRoot):
    """
    An individual cell in the dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SC_SCHEMA["Cell"]
    class_class_curie: ClassVar[str] = "sc_schema:Cell"
    class_name: ClassVar[str] = "Cell"
    class_model_uri: ClassVar[URIRef] = SC_SCHEMA.Cell

    id: Union[str, CellId] = None
    belongs_to_cell_sets: Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellId):
            self.id = CellId(self.id)

        if not isinstance(self.belongs_to_cell_sets, list):
            self.belongs_to_cell_sets = [self.belongs_to_cell_sets] if self.belongs_to_cell_sets is not None else []
        self.belongs_to_cell_sets = [v if isinstance(v, CellSetId) else CellSetId(v) for v in self.belongs_to_cell_sets]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A single cell transcriptomics dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SC_SCHEMA["Dataset"]
    class_class_curie: ClassVar[str] = "sc_schema:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = SC_SCHEMA.Dataset

    id: Union[str, DatasetId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    cell_sets: Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]] = empty_list()
    cells: Optional[Union[Dict[Union[str, CellId], Union[dict, Cell]], List[Union[dict, Cell]]]] = empty_dict()
    ontology_terms: Optional[Union[Union[str, OntologyTermId], List[Union[str, OntologyTermId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.cell_sets, list):
            self.cell_sets = [self.cell_sets] if self.cell_sets is not None else []
        self.cell_sets = [v if isinstance(v, CellSetId) else CellSetId(v) for v in self.cell_sets]

        self._normalize_inlined_as_list(slot_name="cells", slot_type=Cell, key_name="id", keyed=True)

        if not isinstance(self.ontology_terms, list):
            self.ontology_terms = [self.ontology_terms] if self.ontology_terms is not None else []
        self.ontology_terms = [v if isinstance(v, OntologyTermId) else OntologyTermId(v) for v in self.ontology_terms]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SC_SCHEMA.id, name="id", curie=SC_SCHEMA.curie('id'),
                   model_uri=SC_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SC_SCHEMA.name, name="name", curie=SC_SCHEMA.curie('name'),
                   model_uri=SC_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SC_SCHEMA.description, name="description", curie=SC_SCHEMA.curie('description'),
                   model_uri=SC_SCHEMA.description, domain=None, range=Optional[str])

slots.source_uri = Slot(uri=SC_SCHEMA.source_uri, name="source_uri", curie=SC_SCHEMA.curie('source_uri'),
                   model_uri=SC_SCHEMA.source_uri, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.obs_column = Slot(uri=SC_SCHEMA.obs_column, name="obs_column", curie=SC_SCHEMA.curie('obs_column'),
                   model_uri=SC_SCHEMA.obs_column, domain=None, range=Optional[str])

slots.cell_count = Slot(uri=SC_SCHEMA.cell_count, name="cell_count", curie=SC_SCHEMA.curie('cell_count'),
                   model_uri=SC_SCHEMA.cell_count, domain=None, range=Optional[int])

slots.cells = Slot(uri=SC_SCHEMA.cells, name="cells", curie=SC_SCHEMA.curie('cells'),
                   model_uri=SC_SCHEMA.cells, domain=None, range=Optional[Union[Dict[Union[str, CellId], Union[dict, Cell]], List[Union[dict, Cell]]]])

slots.subset_of = Slot(uri=SC_SCHEMA.subset_of, name="subset_of", curie=SC_SCHEMA.curie('subset_of'),
                   model_uri=SC_SCHEMA.subset_of, domain=None, range=Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]])

slots.predominantly_consists_of = Slot(uri=SC_SCHEMA.predominantly_consists_of, name="predominantly_consists_of", curie=SC_SCHEMA.curie('predominantly_consists_of'),
                   model_uri=SC_SCHEMA.predominantly_consists_of, domain=None, range=Optional[Union[str, CellTypeId]])

slots.predominantly_in = Slot(uri=SC_SCHEMA.predominantly_in, name="predominantly_in", curie=SC_SCHEMA.curie('predominantly_in'),
                   model_uri=SC_SCHEMA.predominantly_in, domain=None, range=Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]])

slots.has_tissue = Slot(uri=SC_SCHEMA.has_tissue, name="has_tissue", curie=SC_SCHEMA.curie('has_tissue'),
                   model_uri=SC_SCHEMA.has_tissue, domain=None, range=Optional[Union[Union[dict, MetadataAssociation], List[Union[dict, MetadataAssociation]]]])

slots.has_disease = Slot(uri=SC_SCHEMA.has_disease, name="has_disease", curie=SC_SCHEMA.curie('has_disease'),
                   model_uri=SC_SCHEMA.has_disease, domain=None, range=Optional[Union[Union[dict, MetadataAssociation], List[Union[dict, MetadataAssociation]]]])

slots.has_developmental_stage = Slot(uri=SC_SCHEMA.has_developmental_stage, name="has_developmental_stage", curie=SC_SCHEMA.curie('has_developmental_stage'),
                   model_uri=SC_SCHEMA.has_developmental_stage, domain=None, range=Optional[Union[Union[dict, MetadataAssociation], List[Union[dict, MetadataAssociation]]]])

slots.has_assay = Slot(uri=SC_SCHEMA.has_assay, name="has_assay", curie=SC_SCHEMA.curie('has_assay'),
                   model_uri=SC_SCHEMA.has_assay, domain=None, range=Optional[Union[Union[dict, MetadataAssociation], List[Union[dict, MetadataAssociation]]]])

slots.present_in_cell_sets = Slot(uri=SC_SCHEMA.present_in_cell_sets, name="present_in_cell_sets", curie=SC_SCHEMA.curie('present_in_cell_sets'),
                   model_uri=SC_SCHEMA.present_in_cell_sets, domain=None, range=Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]])

slots.belongs_to_cell_sets = Slot(uri=SC_SCHEMA.belongs_to_cell_sets, name="belongs_to_cell_sets", curie=SC_SCHEMA.curie('belongs_to_cell_sets'),
                   model_uri=SC_SCHEMA.belongs_to_cell_sets, domain=None, range=Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]])

slots.cell_sets = Slot(uri=SC_SCHEMA.cell_sets, name="cell_sets", curie=SC_SCHEMA.curie('cell_sets'),
                   model_uri=SC_SCHEMA.cell_sets, domain=None, range=Optional[Union[Union[str, CellSetId], List[Union[str, CellSetId]]]])

slots.ontology_terms = Slot(uri=SC_SCHEMA.ontology_terms, name="ontology_terms", curie=SC_SCHEMA.curie('ontology_terms'),
                   model_uri=SC_SCHEMA.ontology_terms, domain=None, range=Optional[Union[Union[str, OntologyTermId], List[Union[str, OntologyTermId]]]])

slots.term = Slot(uri=SC_SCHEMA.term, name="term", curie=SC_SCHEMA.curie('term'),
                   model_uri=SC_SCHEMA.term, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.count = Slot(uri=SC_SCHEMA.count, name="count", curie=SC_SCHEMA.curie('count'),
                   model_uri=SC_SCHEMA.count, domain=None, range=Optional[int])