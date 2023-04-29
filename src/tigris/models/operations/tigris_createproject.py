"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createprojectresponse as shared_createprojectresponse
from ..shared import status as shared_status
from typing import Any, Optional


@dataclasses.dataclass
class TigrisCreateProjectRequest:
    
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Create project with this name."""
    request_body: dict[str, Any] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisCreateProjectResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_project_response: Optional[shared_createprojectresponse.CreateProjectResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    