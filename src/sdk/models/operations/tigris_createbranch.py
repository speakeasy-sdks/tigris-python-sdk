from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createbranchresponse as shared_createbranchresponse
from ..shared import status as shared_status
from typing import Any, Optional


@dataclasses.dataclass
class TigrisCreateBranchPathParams:
    branch: str = dataclasses.field(metadata={'path_param': { 'field_name': 'branch', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisCreateBranchRequest:
    path_params: TigrisCreateBranchPathParams = dataclasses.field()
    request: dict[str, Any] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisCreateBranchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_branch_response: Optional[shared_createbranchresponse.CreateBranchResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    