from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getrtchannelsresponse as shared_getrtchannelsresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class RealtimeGetRTChannelsPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RealtimeGetRTChannelsRequest:
    path_params: RealtimeGetRTChannelsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class RealtimeGetRTChannelsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_rt_channels_response: Optional[shared_getrtchannelsresponse.GetRTChannelsResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    