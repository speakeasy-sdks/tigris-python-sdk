from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listcollectionsresponse as shared_listcollectionsresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisListCollectionsPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisListCollectionsQueryParams:
    branch: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'branch', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class TigrisListCollectionsRequest:
    path_params: TigrisListCollectionsPathParams = dataclasses.field()
    query_params: TigrisListCollectionsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class TigrisListCollectionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_collections_response: Optional[shared_listcollectionsresponse.ListCollectionsResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    