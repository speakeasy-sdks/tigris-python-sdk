"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import getnamespacemetadatarequest as shared_getnamespacemetadatarequest
from ...models.shared import getnamespacemetadataresponse as shared_getnamespacemetadataresponse
from ...models.shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class ManagementGetNamespaceMetadataRequest:
    get_namespace_metadata_request: shared_getnamespacemetadatarequest.GetNamespaceMetadataRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    metadata_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metadataKey', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class ManagementGetNamespaceMetadataResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_namespace_metadata_response: Optional[shared_getnamespacemetadataresponse.GetNamespaceMetadataResponse] = dataclasses.field(default=None)
    r"""OK"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

