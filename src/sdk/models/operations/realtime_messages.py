from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import messagesrequest as shared_messagesrequest
from ..shared import messagesresponse as shared_messagesresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class RealtimeMessagesPathParams:
    channel: str = dataclasses.field(metadata={'path_param': { 'field_name': 'channel', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RealtimeMessagesRequest:
    path_params: RealtimeMessagesPathParams = dataclasses.field()
    request: shared_messagesrequest.MessagesRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class RealtimeMessagesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    messages_response: Optional[shared_messagesresponse.MessagesResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    