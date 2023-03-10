from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import presenceresponse as shared_presenceresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class RealtimePresencePathParams:
    channel: str = dataclasses.field(metadata={'path_param': { 'field_name': 'channel', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RealtimePresenceRequest:
    path_params: RealtimePresencePathParams = dataclasses.field()
    

@dataclasses.dataclass
class RealtimePresenceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    presence_response: Optional[shared_presenceresponse.PresenceResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    