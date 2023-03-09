from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getdocumentresponse as shared_getdocumentresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchGetPathParams:
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SearchGetQueryParams:
    ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ids', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class SearchGetRequest:
    path_params: SearchGetPathParams = dataclasses.field()
    query_params: SearchGetQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class SearchGetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_document_response: Optional[shared_getdocumentresponse.GetDocumentResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    