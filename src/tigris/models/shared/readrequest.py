"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import readrequestoptions as shared_readrequestoptions
from dataclasses_json import Undefined, dataclass_json
from tigris import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReadRequest:
    
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})

    r"""Optionally specify a database branch name to perform operation on"""
    fields_: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fields'), 'exclude': lambda f: f is None }})

    r"""To read specific fields from a document. Default is all."""
    filter: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter'), 'exclude': lambda f: f is None }})

    r"""Returns documents matching this filter. A filter can simply be a key, value pair where a key is the field name and the value would be the value for this field. Tigris also allows complex filtering by passing logical expressions. Logical filters are applied on two or more fields using `$or` and `$and`. A few examples of filters: <li> To read a user document where the id has a value 1: ```{\\"id\\": 1 }``` <li> To read all the user documents where the key \\"id\\" has a value 1 or 2 or 3: `{\\"$or\\": [{\\"id\\": 1}, {\\"id\\": 2}, {\\"id\\": 3}]}` Filter allows setting collation on an individual field level. To set collation for all the fields see options. The detailed documentation of the filter is <a href=\\"https://docs.tigrisdata.com/overview/query#specification-1\\" title=\\"here\\">here</a>."""
    options: Optional[shared_readrequestoptions.ReadRequestOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})

    r"""Options that can be used to modify the results, for example \\"limit\\" to control the number of documents returned by the server."""
    sort: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sort'), 'exclude': lambda f: f is None }})

    r"""Array of fields and corresponding sort orders to order the results. Ex: 1 `[{ \\"salary\\": \\"$desc\\" }]`, Ex: 2  `[{ \\"salary\\": \\"$asc\\"}]`"""
    