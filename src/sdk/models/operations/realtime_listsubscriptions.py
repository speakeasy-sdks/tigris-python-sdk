from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listsubscriptionresponse as shared_listsubscriptionresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class RealtimeListSubscriptionsPathParams:
    channel: str = dataclasses.field(metadata={'path_param': { 'field_name': 'channel', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RealtimeListSubscriptionsQueryParams:
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class RealtimeListSubscriptionsRequest:
    path_params: RealtimeListSubscriptionsPathParams = dataclasses.field()
    query_params: RealtimeListSubscriptionsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class RealtimeListSubscriptionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_subscription_response: Optional[shared_listsubscriptionresponse.ListSubscriptionResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    