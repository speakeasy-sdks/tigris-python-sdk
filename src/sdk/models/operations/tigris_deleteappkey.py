from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deleteappkeyrequest as shared_deleteappkeyrequest
from ..shared import deleteappkeyresponse as shared_deleteappkeyresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisDeleteAppKeyPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisDeleteAppKeyRequest:
    path_params: TigrisDeleteAppKeyPathParams = dataclasses.field()
    request: shared_deleteappkeyrequest.DeleteAppKeyRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisDeleteAppKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_app_key_response: Optional[shared_deleteappkeyresponse.DeleteAppKeyResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    