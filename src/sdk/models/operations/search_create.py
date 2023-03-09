from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createdocumentrequest as shared_createdocumentrequest
from ..shared import createdocumentresponse as shared_createdocumentresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchCreatePathParams:
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SearchCreateRequest:
    path_params: SearchCreatePathParams = dataclasses.field()
    request: shared_createdocumentrequest.CreateDocumentRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_document_response: Optional[shared_createdocumentresponse.CreateDocumentResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    