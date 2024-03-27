"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .collation import Collation
from dataclasses_json import Undefined, dataclass_json
from tigris import utils
from typing import List, Optional


@dataclasses.dataclass
class Facet:
    r"""Facet query to aggregate results on given fields. The field name for the facet search can be passed like this `{\\"brand\\": { \\"size\\": 10 }}` where the size controls the total facets for this field."""
    



@dataclasses.dataclass
class SearchRequestFields:
    pass


@dataclasses.dataclass
class SearchRequestFilter:
    r"""Filter stacks on top of query results to further narrow down the results. Similar to `ReadRequest.filter`"""
    



@dataclasses.dataclass
class Sort:
    r"""Array of fields and corresponding sort orders to order the results `[{ \\"salary\\": \\"$desc\\" }]`"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchRequest:
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})
    r"""Optionally specify a database branch name to perform operation on"""
    collation: Optional[Collation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collation'), 'exclude': lambda f: f is None }})
    r"""A collation allows you to specify string comparison rules. Default is case-sensitive, to override it you can set this option to 'ci' that will apply to all the text fields in the filters."""
    exclude_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exclude_fields'), 'exclude': lambda f: f is None }})
    r"""Array of document field names to exclude from results. `include_fields`, if specified, takes precedence over `exclude_fields`."""
    facet: Optional[Facet] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('facet'), 'exclude': lambda f: f is None }})
    r"""Facet query to aggregate results on given fields. The field name for the facet search can be passed like this `{\\"brand\\": { \\"size\\": 10 }}` where the size controls the total facets for this field."""
    fields: Optional[SearchRequestFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fields'), 'exclude': lambda f: f is None }})
    filter_: Optional[SearchRequestFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter'), 'exclude': lambda f: f is None }})
    r"""Filter stacks on top of query results to further narrow down the results. Similar to `ReadRequest.filter`"""
    include_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_fields'), 'exclude': lambda f: f is None }})
    r"""Array of document field names to include in results. By default, all fields are included."""
    page: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page'), 'exclude': lambda f: f is None }})
    r"""Optionally can specify the page to retrieve. If page is set then only hits for this page is returned"""
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size'), 'exclude': lambda f: f is None }})
    r"""Optionally can set the number of hits to be returned per page, default is 20."""
    q: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('q'), 'exclude': lambda f: f is None }})
    r"""Query string for searching across text fields"""
    search_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_fields'), 'exclude': lambda f: f is None }})
    r"""Array of fields to project search query against"""
    sort: Optional[Sort] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sort'), 'exclude': lambda f: f is None }})
    r"""Array of fields and corresponding sort orders to order the results `[{ \\"salary\\": \\"$desc\\" }]`"""
    

