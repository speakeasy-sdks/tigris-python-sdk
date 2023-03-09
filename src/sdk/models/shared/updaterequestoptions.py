from __future__ import annotations
import dataclasses
from ..shared import collation as shared_collation
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateRequestOptions:
    r"""UpdateRequestOptions
    Additional options for update requests.
    """
    
    collation: Optional[shared_collation.Collation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collation'), 'exclude': lambda f: f is None }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit'), 'exclude': lambda f: f is None }})
    write_options: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('write_options'), 'exclude': lambda f: f is None }})
    