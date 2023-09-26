"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import querytimeseriesmetricsresponse as shared_querytimeseriesmetricsresponse
from ..shared import status as shared_status
from typing import Optional



@dataclasses.dataclass
class ObservabilityQueryTimeSeriesMetricsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    query_time_series_metrics_response: Optional[shared_querytimeseriesmetricsresponse.QueryTimeSeriesMetricsResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

