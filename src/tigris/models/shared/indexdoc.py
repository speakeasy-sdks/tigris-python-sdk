"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import docmeta as shared_docmeta
from dataclasses_json import Undefined, dataclass_json
from tigris import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IndexDoc:
    
    doc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('doc'), 'exclude': lambda f: f is None }})
    r"""Actual search document"""
    metadata: Optional[shared_docmeta.DocMeta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""Contains metadata related to the search hit, has information about document created_at/updated_at as well."""
    