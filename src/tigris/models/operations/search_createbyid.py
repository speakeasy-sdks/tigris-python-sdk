"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createbyidrequest as shared_createbyidrequest
from ..shared import createbyidresponse as shared_createbyidresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchCreateByIDRequest:
    
    create_by_id_request: shared_createbyidrequest.CreateByIDRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""document id."""
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    r"""index name where to create document."""
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Tigris project name."""
    

@dataclasses.dataclass
class SearchCreateByIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_by_id_response: Optional[shared_createbyidresponse.CreateByIDResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    