"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import status as shared_status
from ..shared import updatedocumentrequest as shared_updatedocumentrequest
from ..shared import updatedocumentresponse as shared_updatedocumentresponse
from typing import Optional


@dataclasses.dataclass
class SearchUpdateRequest:
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    r"""Index name where to create documents."""
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Project name whose db is under target to insert documents."""
    update_document_request: shared_updatedocumentrequest.UpdateDocumentRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class SearchUpdateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    update_document_response: Optional[shared_updatedocumentresponse.UpdateDocumentResponse] = dataclasses.field(default=None)
    r"""OK"""
    

