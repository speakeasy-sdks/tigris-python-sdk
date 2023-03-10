from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listbranchesresponse as shared_listbranchesresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisListBranchesPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisListBranchesRequest:
    path_params: TigrisListBranchesPathParams = dataclasses.field()
    

@dataclasses.dataclass
class TigrisListBranchesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_branches_response: Optional[shared_listbranchesresponse.ListBranchesResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    