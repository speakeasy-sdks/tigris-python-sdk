"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getresponse as shared_getresponse
from ..shared import status as shared_status
from typing import Optional



@dataclasses.dataclass
class CacheGetRequest:
    key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'key', 'style': 'simple', 'explode': False }})
    r"""cache key"""
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    r"""cache name"""
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Tigris project name"""
    




@dataclasses.dataclass
class CacheGetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_response: Optional[shared_getresponse.GetResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

