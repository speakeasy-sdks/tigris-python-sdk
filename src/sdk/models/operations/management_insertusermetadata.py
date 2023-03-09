from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import insertusermetadatarequest as shared_insertusermetadatarequest
from ..shared import insertusermetadataresponse as shared_insertusermetadataresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class ManagementInsertUserMetadataPathParams:
    metadata_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metadataKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ManagementInsertUserMetadataRequest:
    path_params: ManagementInsertUserMetadataPathParams = dataclasses.field()
    request: shared_insertusermetadatarequest.InsertUserMetadataRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ManagementInsertUserMetadataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    insert_user_metadata_response: Optional[shared_insertusermetadataresponse.InsertUserMetadataResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    