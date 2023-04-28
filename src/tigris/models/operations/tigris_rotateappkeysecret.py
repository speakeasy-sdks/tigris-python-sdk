"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import rotateappkeyrequest as shared_rotateappkeyrequest
from ..shared import rotateappkeyresponse as shared_rotateappkeyresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisRotateAppKeySecretRequest:
    
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})

    r"""project name"""
    rotate_app_key_request: shared_rotateappkeyrequest.RotateAppKeyRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})

    

@dataclasses.dataclass
class TigrisRotateAppKeySecretResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    rotate_app_key_response: Optional[shared_rotateappkeyresponse.RotateAppKeyResponse] = dataclasses.field(default=None)

    r"""OK"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)

    r"""Default error response"""
    