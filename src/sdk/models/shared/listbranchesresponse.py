"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import branchinfo as shared_branchinfo
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBranchesResponse:
    r"""OK"""
    
    branches: Optional[list[shared_branchinfo.BranchInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branches'), 'exclude': lambda f: f is None }})
    r"""List of all the branches in this database"""  
    