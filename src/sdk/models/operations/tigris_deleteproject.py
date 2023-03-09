from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deleteprojectresponse as shared_deleteprojectresponse
from ..shared import status as shared_status
from typing import Any, Optional


@dataclasses.dataclass
class TigrisDeleteProjectPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisDeleteProjectRequest:
    path_params: TigrisDeleteProjectPathParams = dataclasses.field()
    request: dict[str, Any] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisDeleteProjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_project_response: Optional[shared_deleteprojectresponse.DeleteProjectResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    