from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createorreplacedocumentrequest as shared_createorreplacedocumentrequest
from ..shared import createorreplacedocumentresponse as shared_createorreplacedocumentresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchCreateOrReplacePathParams:
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SearchCreateOrReplaceRequest:
    path_params: SearchCreateOrReplacePathParams = dataclasses.field()
    request: shared_createorreplacedocumentrequest.CreateOrReplaceDocumentRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchCreateOrReplaceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_or_replace_document_response: Optional[shared_createorreplacedocumentresponse.CreateOrReplaceDocumentResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    