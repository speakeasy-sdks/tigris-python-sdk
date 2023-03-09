from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getnamespacemetadatarequest as shared_getnamespacemetadatarequest
from ..shared import getnamespacemetadataresponse as shared_getnamespacemetadataresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class ManagementGetNamespaceMetadataPathParams:
    metadata_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metadataKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ManagementGetNamespaceMetadataRequest:
    path_params: ManagementGetNamespaceMetadataPathParams = dataclasses.field()
    request: shared_getnamespacemetadatarequest.GetNamespaceMetadataRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ManagementGetNamespaceMetadataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_namespace_metadata_response: Optional[shared_getnamespacemetadataresponse.GetNamespaceMetadataResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    