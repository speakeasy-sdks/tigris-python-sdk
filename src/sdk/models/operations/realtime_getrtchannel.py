from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getrtchannelresponse as shared_getrtchannelresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class RealtimeGetRTChannelPathParams:
    channel: str = dataclasses.field(metadata={'path_param': { 'field_name': 'channel', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RealtimeGetRTChannelRequest:
    path_params: RealtimeGetRTChannelPathParams = dataclasses.field()
    

@dataclasses.dataclass
class RealtimeGetRTChannelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_rt_channel_response: Optional[shared_getrtchannelresponse.GetRTChannelResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    