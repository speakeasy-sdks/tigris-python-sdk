from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import importrequest as shared_importrequest
from ..shared import importresponse as shared_importresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisImportPathParams:
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisImportRequest:
    path_params: TigrisImportPathParams = dataclasses.field()
    request: shared_importrequest.ImportRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisImportResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    import_response: Optional[shared_importresponse.ImportResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    