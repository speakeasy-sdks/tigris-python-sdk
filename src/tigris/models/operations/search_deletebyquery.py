"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import deletebyqueryrequest as shared_deletebyqueryrequest
from ...models.shared import deletebyqueryresponse as shared_deletebyqueryresponse
from ...models.shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class SearchDeleteByQueryRequest:
    delete_by_query_request: shared_deletebyqueryrequest.DeleteByQueryRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    index: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index', 'style': 'simple', 'explode': False }})
    r"""The index name of the documents that needs deletion."""
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""The project name."""
    



@dataclasses.dataclass
class SearchDeleteByQueryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    delete_by_query_response: Optional[shared_deletebyqueryresponse.DeleteByQueryResponse] = dataclasses.field(default=None)
    r"""OK"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

