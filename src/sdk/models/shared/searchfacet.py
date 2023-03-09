from __future__ import annotations
import dataclasses
from ..shared import facetcount as shared_facetcount
from ..shared import facetstats as shared_facetstats
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchFacet:
    counts: Optional[list[shared_facetcount.FacetCount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('counts'), 'exclude': lambda f: f is None }})
    stats: Optional[shared_facetstats.FacetStats] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stats'), 'exclude': lambda f: f is None }})
    