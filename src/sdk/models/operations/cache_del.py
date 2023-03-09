from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import delresponse as shared_delresponse
from ..shared import status as shared_status
from typing import Any, Optional


@dataclasses.dataclass
class CacheDelPathParams:
    key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'key', 'style': 'simple', 'explode': False }})
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CacheDelRequest:
    path_params: CacheDelPathParams = dataclasses.field()
    request: dict[str, Any] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CacheDelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    del_response: Optional[shared_delresponse.DelResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    