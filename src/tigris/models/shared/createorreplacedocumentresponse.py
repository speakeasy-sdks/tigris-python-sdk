"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import docstatus as shared_docstatus
from dataclasses_json import Undefined, dataclass_json
from tigris import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateOrReplaceDocumentResponse:
    r"""OK"""
    
    status: Optional[list[shared_docstatus.DocStatus]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""An array of statuses of all the documents received in the request. Order is same as it is received in the request. Each item of this array has an “id” and “error” key. Id is set as document id and error will be null in case of success, otherwise error is set with an error code and message."""
    