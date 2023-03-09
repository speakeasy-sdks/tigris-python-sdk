from __future__ import annotations
import dataclasses
from ..shared import appkey as shared_appkey
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RotateAppKeyResponse:
    r"""RotateAppKeyResponse
    RotateAppKeyResponse returns the new app key with rotated secret
    """
    
    app_key: Optional[shared_appkey.AppKey] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_key'), 'exclude': lambda f: f is None }})
    