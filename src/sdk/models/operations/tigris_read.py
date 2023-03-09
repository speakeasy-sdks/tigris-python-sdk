from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import readrequest as shared_readrequest
from ..shared import status as shared_status
from ..shared import streamingreadresponse as shared_streamingreadresponse
from typing import Optional


@dataclasses.dataclass
class TigrisReadPathParams:
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisReadRequest:
    path_params: TigrisReadPathParams = dataclasses.field()
    request: shared_readrequest.ReadRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisReadResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    streaming_read_response: Optional[shared_streamingreadresponse.StreamingReadResponse] = dataclasses.field(default=None)
    