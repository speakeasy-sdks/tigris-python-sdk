from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getresponse as shared_getresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class CacheGetPathParams:
    key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'key', 'style': 'simple', 'explode': False }})
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CacheGetRequest:
    path_params: CacheGetPathParams = dataclasses.field()
    

@dataclasses.dataclass
class CacheGetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_response: Optional[shared_getresponse.GetResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    