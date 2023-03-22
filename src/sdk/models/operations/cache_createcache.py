"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createcacherequest as shared_createcacherequest
from ..shared import createcacheresponse as shared_createcacheresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class CacheCreateCacheRequest:
    
    create_cache_request: shared_createcacherequest.CreateCacheRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})  
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    r"""cache name"""  
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Tigris project name"""  
    

@dataclasses.dataclass
class CacheCreateCacheResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    create_cache_response: Optional[shared_createcacheresponse.CreateCacheResponse] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""  
    