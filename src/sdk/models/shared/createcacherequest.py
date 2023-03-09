from __future__ import annotations
import dataclasses
from ..shared import createcacheoptions as shared_createcacheoptions
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCacheRequest:
    options: Optional[shared_createcacheoptions.CreateCacheOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    