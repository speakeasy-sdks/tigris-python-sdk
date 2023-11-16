"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import readmessagesresponse as shared_readmessagesresponse
from ...models.shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class RealtimeReadMessagesRequest:
    channel: str = dataclasses.field(metadata={'path_param': { 'field_name': 'channel', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    end: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end', 'style': 'form', 'explode': True }})
    event: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'event', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    session_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'session_id', 'style': 'form', 'explode': True }})
    socket_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'socket_id', 'style': 'form', 'explode': True }})
    start: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class RealtimeReadMessagesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    read_messages_response: Optional[shared_readmessagesresponse.ReadMessagesResponse] = dataclasses.field(default=None)
    r"""OK"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

