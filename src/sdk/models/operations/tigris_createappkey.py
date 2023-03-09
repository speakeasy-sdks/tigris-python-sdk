from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createappkeyrequest as shared_createappkeyrequest
from ..shared import createappkeyresponse as shared_createappkeyresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisCreateAppKeyPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisCreateAppKeyRequest:
    path_params: TigrisCreateAppKeyPathParams = dataclasses.field()
    request: shared_createappkeyrequest.CreateAppKeyRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisCreateAppKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_app_key_response: Optional[shared_createappkeyresponse.CreateAppKeyResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    