from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getinforesponse as shared_getinforesponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class ObservabilityGetInfoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_info_response: Optional[shared_getinforesponse.GetInfoResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    