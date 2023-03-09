from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deleteindexrequest as shared_deleteindexrequest
from ..shared import deleteindexresponse as shared_deleteindexresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchDeleteIndexPathParams:
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SearchDeleteIndexRequest:
    path_params: SearchDeleteIndexPathParams = dataclasses.field()
    request: shared_deleteindexrequest.DeleteIndexRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchDeleteIndexResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_index_response: Optional[shared_deleteindexresponse.DeleteIndexResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    