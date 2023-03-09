from __future__ import annotations
import dataclasses
from ..shared import page as shared_page
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchMetadata:
    found: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('found'), 'exclude': lambda f: f is None }})
    page: Optional[shared_page.Page] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page'), 'exclude': lambda f: f is None }})
    total_pages: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_pages'), 'exclude': lambda f: f is None }})
    