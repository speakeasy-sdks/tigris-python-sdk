"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import healthcheckresponse as shared_healthcheckresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class HealthAPIHealthResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    health_check_response: Optional[shared_healthcheckresponse.HealthCheckResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    