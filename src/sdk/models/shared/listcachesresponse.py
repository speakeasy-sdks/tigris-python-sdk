from __future__ import annotations
import dataclasses
from ..shared import cachemetadata as shared_cachemetadata
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCachesResponse:
    caches: Optional[list[shared_cachemetadata.CacheMetadata]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caches'), 'exclude': lambda f: f is None }})
    