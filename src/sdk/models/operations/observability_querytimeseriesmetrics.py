from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import querytimeseriesmetricsrequest as shared_querytimeseriesmetricsrequest
from ..shared import querytimeseriesmetricsresponse as shared_querytimeseriesmetricsresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class ObservabilityQueryTimeSeriesMetricsRequest:
    request: shared_querytimeseriesmetricsrequest.QueryTimeSeriesMetricsRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ObservabilityQueryTimeSeriesMetricsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    query_time_series_metrics_response: Optional[shared_querytimeseriesmetricsresponse.QueryTimeSeriesMetricsResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    