from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import status as shared_status
from ..shared import updateusermetadatarequest as shared_updateusermetadatarequest
from ..shared import updateusermetadataresponse as shared_updateusermetadataresponse
from typing import Optional


@dataclasses.dataclass
class ManagementUpdateUserMetadataPathParams:
    metadata_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metadataKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ManagementUpdateUserMetadataRequest:
    path_params: ManagementUpdateUserMetadataPathParams = dataclasses.field()
    request: shared_updateusermetadatarequest.UpdateUserMetadataRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ManagementUpdateUserMetadataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    update_user_metadata_response: Optional[shared_updateusermetadataresponse.UpdateUserMetadataResponse] = dataclasses.field(default=None)
    