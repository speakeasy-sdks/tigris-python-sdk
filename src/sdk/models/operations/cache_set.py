from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import setrequest as shared_setrequest
from ..shared import setresponse as shared_setresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class CacheSetPathParams:
    key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'key', 'style': 'simple', 'explode': False }})
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CacheSetRequest:
    path_params: CacheSetPathParams = dataclasses.field()
    request: shared_setrequest.SetRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CacheSetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    set_response: Optional[shared_setresponse.SetResponse] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    