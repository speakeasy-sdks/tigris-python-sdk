"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import committransactionrequest as shared_committransactionrequest
from ...models.shared import committransactionresponse as shared_committransactionresponse
from ...models.shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisCommitTransactionRequest:
    commit_transaction_request: shared_committransactionrequest.CommitTransactionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Project name whose DB this transaction belongs to."""
    



@dataclasses.dataclass
class TigrisCommitTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    commit_transaction_response: Optional[shared_committransactionresponse.CommitTransactionResponse] = dataclasses.field(default=None)
    r"""OK"""
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""
    

