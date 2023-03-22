"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateOrUpdateCollectionRequest:
    
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})
    r"""Optionally specify a database branch name to perform operation on"""  
    only_create: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('only_create'), 'exclude': lambda f: f is None }})
    r"""If set to `true` then the update schema request to the collection will fail by returning a conflict with HTTP Status code 409. The default is false."""  
    options: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""Collection requests modifying options."""  
    schema: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""The schema specifications are same as JSON schema specification defined <a href="https://json-schema.org/specification.html" title="here">here</a>.<p></p> Schema example: `{  "title": "user",  "description": "Collection of documents with details of users",  "properties": {    "id": {      "description": "A unique identifier for the user",      "type": "integer"    },    "name": {      "description": "Name of the user",      "type": "string",      "maxLength": 128    },    "balance": {      "description": "User account balance",      "type": "number"    }  },  "primary_key": ["id"] }`"""  
    