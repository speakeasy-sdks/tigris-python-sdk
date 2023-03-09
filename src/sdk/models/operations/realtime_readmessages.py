from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import readmessagesresponse as shared_readmessagesresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class RealtimeReadMessagesPathParams:
    channel: str = dataclasses.field(metadata={'path_param': { 'field_name': 'channel', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RealtimeReadMessagesQueryParams:
    end: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end', 'style': 'form', 'explode': True }})
    event: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'event', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    session_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'session_id', 'style': 'form', 'explode': True }})
    socket_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'socket_id', 'style': 'form', 'explode': True }})
    start: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class RealtimeReadMessagesRequest:
    path_params: RealtimeReadMessagesPathParams = dataclasses.field()
    query_params: RealtimeReadMessagesQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class RealtimeReadMessagesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    read_messages_response: Optional[shared_readmessagesresponse.ReadMessagesResponse] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    