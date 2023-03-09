from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listnamespacesresponse as shared_listnamespacesresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class ManagementListNamespacesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_namespaces_response: Optional[shared_listnamespacesresponse.ListNamespacesResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    