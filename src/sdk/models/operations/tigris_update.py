from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import status as shared_status
from ..shared import updaterequest as shared_updaterequest
from ..shared import updateresponse as shared_updateresponse
from typing import Optional


@dataclasses.dataclass
class TigrisUpdatePathParams:
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisUpdateRequest:
    path_params: TigrisUpdatePathParams = dataclasses.field()
    request: shared_updaterequest.UpdateRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    update_response: Optional[shared_updateresponse.UpdateResponse] = dataclasses.field(default=None)
    