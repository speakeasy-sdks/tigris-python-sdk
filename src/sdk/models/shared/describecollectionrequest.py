"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DescribeCollectionRequest:
    
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})
    r"""Optionally specify a database branch name to perform operation on"""  
    collection: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection'), 'exclude': lambda f: f is None }})
    r"""Name of the collection."""  
    options: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""Collection requests modifying options."""  
    project: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project'), 'exclude': lambda f: f is None }})
    r"""Project name whose db is under target to get description of its collection."""  
    schema_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema_format'), 'exclude': lambda f: f is None }})
    r"""Return schema in the requested format. Format can be JSON, Go, TypeScript, Java. Default is JSON."""  
    