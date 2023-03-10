from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createorupdatecollectionrequest as shared_createorupdatecollectionrequest
from ..shared import createorupdatecollectionresponse as shared_createorupdatecollectionresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisCreateOrUpdateCollectionPathParams:
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisCreateOrUpdateCollectionRequest:
    path_params: TigrisCreateOrUpdateCollectionPathParams = dataclasses.field()
    request: shared_createorupdatecollectionrequest.CreateOrUpdateCollectionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisCreateOrUpdateCollectionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_or_update_collection_response: Optional[shared_createorupdatecollectionresponse.CreateOrUpdateCollectionResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    