from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createorupdateindexrequest as shared_createorupdateindexrequest
from ..shared import createorupdateindexresponse as shared_createorupdateindexresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchCreateOrUpdateIndexPathParams:
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SearchCreateOrUpdateIndexRequest:
    path_params: SearchCreateOrUpdateIndexPathParams = dataclasses.field()
    request: shared_createorupdateindexrequest.CreateOrUpdateIndexRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchCreateOrUpdateIndexResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_or_update_index_response: Optional[shared_createorupdateindexresponse.CreateOrUpdateIndexResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    