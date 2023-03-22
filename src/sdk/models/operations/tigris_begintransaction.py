"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import begintransactionrequest as shared_begintransactionrequest
from ..shared import begintransactionresponse as shared_begintransactionresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisBeginTransactionRequest:
    
    begin_transaction_request: shared_begintransactionrequest.BeginTransactionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})  
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Project name whose DB this transaction belongs to."""  
    

@dataclasses.dataclass
class TigrisBeginTransactionResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    begin_transaction_response: Optional[shared_begintransactionresponse.BeginTransactionResponse] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""  
    