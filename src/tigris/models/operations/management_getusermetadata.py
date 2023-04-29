"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getusermetadatarequest as shared_getusermetadatarequest
from ..shared import getusermetadataresponse as shared_getusermetadataresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class ManagementGetUserMetadataRequest:
    
    get_user_metadata_request: shared_getusermetadatarequest.GetUserMetadataRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    metadata_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metadataKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ManagementGetUserMetadataResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_user_metadata_response: Optional[shared_getusermetadataresponse.GetUserMetadataResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    