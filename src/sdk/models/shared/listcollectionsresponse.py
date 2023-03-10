from __future__ import annotations
import dataclasses
from ..shared import collectioninfo as shared_collectioninfo
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCollectionsResponse:
    collections: Optional[list[shared_collectioninfo.CollectionInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collections'), 'exclude': lambda f: f is None }})
    