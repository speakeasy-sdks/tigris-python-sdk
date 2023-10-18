"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import importrequestoptions as shared_importrequestoptions
from dataclasses_json import Undefined, dataclass_json
from tigris import utils
from typing import List, Optional


@dataclasses.dataclass
class ImportRequestDocuments:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ImportRequest:
    autogenerated: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autogenerated'), 'exclude': lambda f: f is None }})
    r"""The list of autogenerated fields of the collection"""
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})
    r"""Optionally specify a database branch name to perform operation on"""
    create_collection: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('create_collection'), 'exclude': lambda f: f is None }})
    r"""Allow to create collection if it doesn't exists"""
    documents: Optional[List[ImportRequestDocuments]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documents'), 'exclude': lambda f: f is None }})
    r"""Array of documents to import. Each document is a JSON object."""
    options: Optional[shared_importrequestoptions.ImportRequestOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""additional options for import requests."""
    primary_key: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary_key'), 'exclude': lambda f: f is None }})
    r"""List of fields which constitutes primary key of the collection If not specified and field with name 'id' is present, it's used as a primary key, further if inferred type is UUID, then it's set as autogenerated."""
    

