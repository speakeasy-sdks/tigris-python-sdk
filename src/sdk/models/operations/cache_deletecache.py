from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deletecacheresponse as shared_deletecacheresponse
from ..shared import status as shared_status
from typing import Any, Optional


@dataclasses.dataclass
class CacheDeleteCachePathParams:
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CacheDeleteCacheRequest:
    path_params: CacheDeleteCachePathParams = dataclasses.field()
    request: dict[str, Any] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CacheDeleteCacheResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_cache_response: Optional[shared_deletecacheresponse.DeleteCacheResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    