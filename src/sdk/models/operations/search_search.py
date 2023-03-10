from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import searchindexrequest as shared_searchindexrequest
from ..shared import searchindexresponse as shared_searchindexresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchSearchPathParams:
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SearchSearchRequest:
    path_params: SearchSearchPathParams = dataclasses.field()
    request: shared_searchindexrequest.SearchIndexRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchSearchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    search_index_response: Optional[shared_searchindexresponse.SearchIndexResponse] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    