from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getsetrequest as shared_getsetrequest
from ..shared import getsetresponse as shared_getsetresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class CacheGetSetPathParams:
    key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'key', 'style': 'simple', 'explode': False }})
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CacheGetSetRequest:
    path_params: CacheGetSetPathParams = dataclasses.field()
    request: shared_getsetrequest.GetSetRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CacheGetSetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_set_response: Optional[shared_getsetresponse.GetSetResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    