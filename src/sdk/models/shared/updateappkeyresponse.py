from __future__ import annotations
import dataclasses
from ..shared import appkey as shared_appkey
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateAppKeyResponse:
    r"""UpdateAppKeyResponse
    Returns response for updating the app key description
    """
    
    updated_app_key: Optional[shared_appkey.AppKey] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_app_key'), 'exclude': lambda f: f is None }})
    