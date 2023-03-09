from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import insertrequest as shared_insertrequest
from ..shared import insertresponse as shared_insertresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisInsertPathParams:
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisInsertRequest:
    path_params: TigrisInsertPathParams = dataclasses.field()
    request: shared_insertrequest.InsertRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisInsertResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    insert_response: Optional[shared_insertresponse.InsertResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    