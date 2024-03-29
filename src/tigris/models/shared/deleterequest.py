"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import deleterequestoptions as shared_deleterequestoptions
from dataclasses_json import Undefined, dataclass_json
from tigris import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteRequest:
    
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})
    r"""Optionally specify a database branch name to perform operation on"""
    filter: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter'), 'exclude': lambda f: f is None }})
    r"""Delete documents which matching specified filter. A filter can simply be key, value where key is the field name and value would be the value for this field. Or a filter can be logical where two or more fields can be logically joined using $or and $and. A few examples of filter: <li> To delete a user document where the id has a value 1: ```{\\"id\\": 1 }``` <li> To delete all the user documents where the key \\"id\\" has a value 1 or 2 or 3: `{\\"$or\\": [{\\"id\\": 1}, {\\"id\\": 2}, {\\"id\\": 3}]}`"""
    options: Optional[shared_deleterequestoptions.DeleteRequestOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""Additional options for deleted requests."""
    