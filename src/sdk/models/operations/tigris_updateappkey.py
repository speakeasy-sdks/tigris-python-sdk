from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import status as shared_status
from ..shared import updateappkeyrequest as shared_updateappkeyrequest
from ..shared import updateappkeyresponse as shared_updateappkeyresponse
from typing import Optional


@dataclasses.dataclass
class TigrisUpdateAppKeyPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisUpdateAppKeyRequest:
    path_params: TigrisUpdateAppKeyPathParams = dataclasses.field()
    request: shared_updateappkeyrequest.UpdateAppKeyRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisUpdateAppKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    update_app_key_response: Optional[shared_updateappkeyresponse.UpdateAppKeyResponse] = dataclasses.field(default=None)
    