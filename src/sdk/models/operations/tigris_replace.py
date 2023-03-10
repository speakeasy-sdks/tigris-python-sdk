from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import replacerequest as shared_replacerequest
from ..shared import replaceresponse as shared_replaceresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisReplacePathParams:
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisReplaceRequest:
    path_params: TigrisReplacePathParams = dataclasses.field()
    request: shared_replacerequest.ReplaceRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisReplaceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    replace_response: Optional[shared_replaceresponse.ReplaceResponse] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    