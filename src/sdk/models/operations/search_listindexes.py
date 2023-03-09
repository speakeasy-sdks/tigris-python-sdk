from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listindexesresponse as shared_listindexesresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchListIndexesPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SearchListIndexesQueryParams:
    filter_branch: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter.branch', 'style': 'form', 'explode': True }})
    filter_collection: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter.collection', 'style': 'form', 'explode': True }})
    filter_type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter.type', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class SearchListIndexesRequest:
    path_params: SearchListIndexesPathParams = dataclasses.field()
    query_params: SearchListIndexesQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class SearchListIndexesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_indexes_response: Optional[shared_listindexesresponse.ListIndexesResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    