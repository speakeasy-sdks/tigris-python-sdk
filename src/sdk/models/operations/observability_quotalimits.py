from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import quotalimitsresponse as shared_quotalimitsresponse
from ..shared import status as shared_status
from typing import Any, Optional


@dataclasses.dataclass
class ObservabilityQuotaLimitsRequest:
    request: dict[str, Any] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ObservabilityQuotaLimitsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    quota_limits_response: Optional[shared_quotalimitsresponse.QuotaLimitsResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    