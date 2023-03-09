from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import rollbacktransactionrequest as shared_rollbacktransactionrequest
from ..shared import rollbacktransactionresponse as shared_rollbacktransactionresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisRollbackTransactionPathParams:
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisRollbackTransactionRequest:
    path_params: TigrisRollbackTransactionPathParams = dataclasses.field()
    request: shared_rollbacktransactionrequest.RollbackTransactionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisRollbackTransactionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    rollback_transaction_response: Optional[shared_rollbacktransactionresponse.RollbackTransactionResponse] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    