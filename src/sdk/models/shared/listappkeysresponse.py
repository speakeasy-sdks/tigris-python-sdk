from __future__ import annotations
import dataclasses
from ..shared import appkey as shared_appkey
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListAppKeysResponse:
    r"""ListAppKeysResponse
    ListAppKeysResponse returns one or more visible app keys to user
    """
    
    app_keys: Optional[list[shared_appkey.AppKey]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_keys'), 'exclude': lambda f: f is None }})
    