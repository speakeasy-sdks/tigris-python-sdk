from __future__ import annotations
import dataclasses
from ..shared import indexinfo as shared_indexinfo
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIndexesResponse:
    indexes: Optional[list[shared_indexinfo.IndexInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indexes'), 'exclude': lambda f: f is None }})
    