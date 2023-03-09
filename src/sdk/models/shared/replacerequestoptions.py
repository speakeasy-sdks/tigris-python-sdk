from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReplaceRequestOptions:
    r"""ReplaceRequestOptions
    Additional options for replace requests.
    """
    
    write_options: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('write_options'), 'exclude': lambda f: f is None }})
    