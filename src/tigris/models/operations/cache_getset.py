"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getsetrequest as shared_getsetrequest
from ..shared import getsetresponse as shared_getsetresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class CacheGetSetRequest:
    get_set_request: shared_getsetrequest.GetSetRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'key', 'style': 'simple', 'explode': False }})
    r"""cache key"""
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    r"""cache name"""
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Tigris project name"""
    



@dataclasses.dataclass
class CacheGetSetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_set_response: Optional[shared_getsetresponse.GetSetResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

