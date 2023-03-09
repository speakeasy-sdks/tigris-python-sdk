from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import searchrequest as shared_searchrequest
from ..shared import status as shared_status
from ..shared import streamingsearchresponse as shared_streamingsearchresponse
from typing import Optional


@dataclasses.dataclass
class TigrisSearchPathParams:
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisSearchRequest:
    path_params: TigrisSearchPathParams = dataclasses.field()
    request: shared_searchrequest.SearchRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisSearchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    streaming_search_response: Optional[shared_streamingsearchresponse.StreamingSearchResponse] = dataclasses.field(default=None)
    