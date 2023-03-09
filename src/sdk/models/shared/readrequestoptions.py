from __future__ import annotations
import dataclasses
from ..shared import collation as shared_collation
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReadRequestOptions:
    r"""ReadRequestOptions
    Options that can be used to modify the results, for example \"limit\" to control the number of documents returned by the server.
    """
    
    collation: Optional[shared_collation.Collation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collation'), 'exclude': lambda f: f is None }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit'), 'exclude': lambda f: f is None }})
    offset: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offset'), 'exclude': lambda f: f is None }})
    skip: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skip'), 'exclude': lambda f: f is None }})
    