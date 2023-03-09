from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import dropcollectionrequest as shared_dropcollectionrequest
from ..shared import dropcollectionresponse as shared_dropcollectionresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisDropCollectionPathParams:
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisDropCollectionRequest:
    path_params: TigrisDropCollectionPathParams = dataclasses.field()
    request: shared_dropcollectionrequest.DropCollectionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisDropCollectionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    drop_collection_response: Optional[shared_dropcollectionresponse.DropCollectionResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    