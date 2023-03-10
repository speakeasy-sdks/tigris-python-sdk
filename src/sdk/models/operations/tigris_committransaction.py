from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import committransactionrequest as shared_committransactionrequest
from ..shared import committransactionresponse as shared_committransactionresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisCommitTransactionPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisCommitTransactionRequest:
    path_params: TigrisCommitTransactionPathParams = dataclasses.field()
    request: shared_committransactionrequest.CommitTransactionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisCommitTransactionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    commit_transaction_response: Optional[shared_committransactionresponse.CommitTransactionResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    