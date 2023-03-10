from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deletebyqueryrequest as shared_deletebyqueryrequest
from ..shared import deletebyqueryresponse as shared_deletebyqueryresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchDeleteByQueryPathParams:
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SearchDeleteByQueryRequest:
    path_params: SearchDeleteByQueryPathParams = dataclasses.field()
    request: shared_deletebyqueryrequest.DeleteByQueryRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchDeleteByQueryResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_by_query_response: Optional[shared_deletebyqueryresponse.DeleteByQueryResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    