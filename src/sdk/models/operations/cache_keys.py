from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import keysresponse as shared_keysresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class CacheKeysPathParams:
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CacheKeysQueryParams:
    count: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'count', 'style': 'form', 'explode': True }})
    cursor: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    pattern: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pattern', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class CacheKeysRequest:
    path_params: CacheKeysPathParams = dataclasses.field()
    query_params: CacheKeysQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class CacheKeysResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    keys_response: Optional[shared_keysresponse.KeysResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    