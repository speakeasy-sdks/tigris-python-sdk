"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import searchhitmeta as shared_searchhitmeta
from dataclasses_json import Undefined, dataclass_json
from tigris import utils
from typing import Optional


@dataclasses.dataclass
class SearchHitData:
    r"""Actual search document"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchHit:
    data: Optional[SearchHitData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""Actual search document"""
    metadata: Optional[shared_searchhitmeta.SearchHitMeta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""Contains metadata related to the search hit, has information about document created_at/updated_at as well."""
    

