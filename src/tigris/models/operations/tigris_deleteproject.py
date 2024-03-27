"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import deleteprojectrequest as shared_deleteprojectrequest
from ...models.shared import deleteprojectresponse as shared_deleteprojectresponse
from ...models.shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisDeleteProjectRequest:
    delete_project_request: shared_deleteprojectrequest.DeleteProjectRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Delete Project with this name. <p></p>**Note**: Deletes all resources under this project. Use with caution."""
    



@dataclasses.dataclass
class TigrisDeleteProjectResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    delete_project_response: Optional[shared_deleteprojectresponse.DeleteProjectResponse] = dataclasses.field(default=None)
    r"""OK"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

