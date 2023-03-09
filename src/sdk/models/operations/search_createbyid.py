from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createbyidrequest as shared_createbyidrequest
from ..shared import createbyidresponse as shared_createbyidresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchCreateByIDPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SearchCreateByIDRequest:
    path_params: SearchCreateByIDPathParams = dataclasses.field()
    request: shared_createbyidrequest.CreateByIDRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchCreateByIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_by_id_response: Optional[shared_createbyidresponse.CreateByIDResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    