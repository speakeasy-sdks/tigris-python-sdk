"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listappkeysresponse as shared_listappkeysresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisListAppKeysPathParams:
    
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Project name filter"""  
    

@dataclasses.dataclass
class TigrisListAppKeysRequest:
    
    path_params: TigrisListAppKeysPathParams = dataclasses.field()  
    

@dataclasses.dataclass
class TigrisListAppKeysResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    list_app_keys_response: Optional[shared_listappkeysresponse.ListAppKeysResponse] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""  
    