"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import deletedocumentrequest as shared_deletedocumentrequest
from ...models.shared import deletedocumentresponse as shared_deletedocumentresponse
from ...models.shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchDeleteRequest:
    delete_document_request: shared_deletedocumentrequest.DeleteDocumentRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    r"""The index name of the documents that needs deletion."""
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""The project name."""
    



@dataclasses.dataclass
class SearchDeleteResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    delete_document_response: Optional[shared_deletedocumentresponse.DeleteDocumentResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

