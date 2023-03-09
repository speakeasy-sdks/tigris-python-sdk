from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import status as shared_status
from ..shared import updatedocumentrequest as shared_updatedocumentrequest
from ..shared import updatedocumentresponse as shared_updatedocumentresponse
from typing import Optional


@dataclasses.dataclass
class SearchUpdatePathParams:
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SearchUpdateRequest:
    path_params: SearchUpdatePathParams = dataclasses.field()
    request: shared_updatedocumentrequest.UpdateDocumentRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    update_document_response: Optional[shared_updatedocumentresponse.UpdateDocumentResponse] = dataclasses.field(default=None)
    