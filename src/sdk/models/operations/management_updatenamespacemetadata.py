from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import status as shared_status
from ..shared import updatenamespacemetadatarequest as shared_updatenamespacemetadatarequest
from ..shared import updatenamespacemetadataresponse as shared_updatenamespacemetadataresponse
from typing import Optional


@dataclasses.dataclass
class ManagementUpdateNamespaceMetadataPathParams:
    metadata_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metadataKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ManagementUpdateNamespaceMetadataRequest:
    path_params: ManagementUpdateNamespaceMetadataPathParams = dataclasses.field()
    request: shared_updatenamespacemetadatarequest.UpdateNamespaceMetadataRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ManagementUpdateNamespaceMetadataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    update_namespace_metadata_response: Optional[shared_updatenamespacemetadataresponse.UpdateNamespaceMetadataResponse] = dataclasses.field(default=None)
    