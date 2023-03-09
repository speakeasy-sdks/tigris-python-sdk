from __future__ import annotations
import dataclasses
from ..shared import searchfacet as shared_searchfacet
from ..shared import searchhit as shared_searchhit
from ..shared import searchmetadata as shared_searchmetadata
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchResponse:
    r"""SearchResponse
    Response struct for search
    """
    
    facets: Optional[dict[str, shared_searchfacet.SearchFacet]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('facets'), 'exclude': lambda f: f is None }})
    hits: Optional[list[shared_searchhit.SearchHit]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hits'), 'exclude': lambda f: f is None }})
    meta: Optional[shared_searchmetadata.SearchMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta'), 'exclude': lambda f: f is None }})
    