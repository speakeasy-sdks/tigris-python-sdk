"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import insertrequest as shared_insertrequest
from ..shared import insertresponse as shared_insertresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisInsertRequest:
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    r"""Collection name where to insert documents."""
    insert_request: shared_insertrequest.InsertRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Project name whose db is under target to insert documents."""
    



@dataclasses.dataclass
class TigrisInsertResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    insert_response: Optional[shared_insertresponse.InsertResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

