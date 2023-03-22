"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listindexesresponse as shared_listindexesresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchListIndexesPathParams:
    
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Tigris project name."""  
    

@dataclasses.dataclass
class SearchListIndexesQueryParams:
    
    filter_branch: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter.branch', 'style': 'form', 'explode': True }})
    r"""Applicable only in case index is backed by Tigris collection. This is the database branch for the above collection. For primary database it can be omitted or "main" can be passed."""  
    filter_collection: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter.collection', 'style': 'form', 'explode': True }})
    r"""Applicable only in case index is backed by Tigris collection."""  
    filter_type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter.type', 'style': 'form', 'explode': True }})
    r"""An index can be either managed by user explicitly then the type is set as "user" or the index is backed by Tigris collection. In case it is backed by Tigris collection the type is "tigris"."""  
    

@dataclasses.dataclass
class SearchListIndexesRequest:
    
    path_params: SearchListIndexesPathParams = dataclasses.field()  
    query_params: SearchListIndexesQueryParams = dataclasses.field()  
    

@dataclasses.dataclass
class SearchListIndexesResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    list_indexes_response: Optional[shared_listindexesresponse.ListIndexesResponse] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""  
    