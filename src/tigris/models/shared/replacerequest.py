"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .replacerequestoptions import ReplaceRequestOptions
from dataclasses_json import Undefined, dataclass_json
from tigris import utils
from typing import List, Optional


@dataclasses.dataclass
class ReplaceRequestDocuments:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReplaceRequest:
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})
    r"""Optionally specify a database branch name to perform operation on"""
    documents: Optional[List[ReplaceRequestDocuments]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documents'), 'exclude': lambda f: f is None }})
    r"""Array of documents to be replaced. Each document is a JSON object."""
    options: Optional[ReplaceRequestOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""Additional options for replace requests."""
    

