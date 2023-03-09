from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listcachesresponse as shared_listcachesresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class CacheListCachesPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CacheListCachesRequest:
    path_params: CacheListCachesPathParams = dataclasses.field()
    

@dataclasses.dataclass
class CacheListCachesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_caches_response: Optional[shared_listcachesresponse.ListCachesResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    