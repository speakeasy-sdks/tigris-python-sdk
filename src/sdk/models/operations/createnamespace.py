from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createnamespacerequest as shared_createnamespacerequest
from ..shared import createnamespaceresponse as shared_createnamespaceresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class CreateNamespaceRequest:
    request: shared_createnamespacerequest.CreateNamespaceRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateNamespaceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_namespace_response: Optional[shared_createnamespaceresponse.CreateNamespaceResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    