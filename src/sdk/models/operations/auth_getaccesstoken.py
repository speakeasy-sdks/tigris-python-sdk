from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getaccesstokenresponse as shared_getaccesstokenresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class AuthGetAccessTokenResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_access_token_response: Optional[shared_getaccesstokenresponse.GetAccessTokenResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    