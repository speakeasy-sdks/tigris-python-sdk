"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createbranchrequest as shared_createbranchrequest
from ..shared import createbranchresponse as shared_createbranchresponse
from ..shared import status as shared_status
from typing import Optional



@dataclasses.dataclass
class TigrisCreateBranchRequest:
    branch: str = dataclasses.field(metadata={'path_param': { 'field_name': 'branch', 'style': 'simple', 'explode': False }})
    r"""Name of the database branch to be created. <p></p>**Note**: `main` is a reserved branch name for primary database and is automatically created with CreateProject"""
    create_branch_request: shared_createbranchrequest.CreateBranchRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Create a database branch in this project"""
    




@dataclasses.dataclass
class TigrisCreateBranchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_branch_response: Optional[shared_createbranchresponse.CreateBranchResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

