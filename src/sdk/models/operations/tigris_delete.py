from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deleterequest as shared_deleterequest
from ..shared import deleteresponse as shared_deleteresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisDeletePathParams:
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisDeleteRequest:
    path_params: TigrisDeletePathParams = dataclasses.field()
    request: shared_deleterequest.DeleteRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisDeleteResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_response: Optional[shared_deleteresponse.DeleteResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    