"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import insertusermetadatarequest as shared_insertusermetadatarequest
from ...models.shared import insertusermetadataresponse as shared_insertusermetadataresponse
from ...models.shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class ManagementInsertUserMetadataRequest:
    insert_user_metadata_request: shared_insertusermetadatarequest.InsertUserMetadataRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    metadata_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metadataKey', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class ManagementInsertUserMetadataResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    insert_user_metadata_response: Optional[shared_insertusermetadataresponse.InsertUserMetadataResponse] = dataclasses.field(default=None)
    r"""OK"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

