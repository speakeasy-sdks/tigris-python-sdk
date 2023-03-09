from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import describedatabaserequest as shared_describedatabaserequest
from ..shared import describedatabaseresponse as shared_describedatabaseresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisDescribeDatabasePathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisDescribeDatabaseRequest:
    path_params: TigrisDescribeDatabasePathParams = dataclasses.field()
    request: shared_describedatabaserequest.DescribeDatabaseRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisDescribeDatabaseResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    describe_database_response: Optional[shared_describedatabaseresponse.DescribeDatabaseResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    