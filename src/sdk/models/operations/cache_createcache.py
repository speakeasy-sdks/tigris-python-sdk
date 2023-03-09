from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createcacherequest as shared_createcacherequest
from ..shared import createcacheresponse as shared_createcacheresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class CacheCreateCachePathParams:
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CacheCreateCacheRequest:
    path_params: CacheCreateCachePathParams = dataclasses.field()
    request: shared_createcacherequest.CreateCacheRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CacheCreateCacheResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_cache_response: Optional[shared_createcacheresponse.CreateCacheResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    