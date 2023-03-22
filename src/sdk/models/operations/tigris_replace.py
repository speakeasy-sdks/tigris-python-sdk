"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import replacerequest as shared_replacerequest
from ..shared import replaceresponse as shared_replaceresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisReplaceRequest:
    
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    r"""Collection name where to replace documents."""  
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Project name whose db is under target to replace documents."""  
    replace_request: shared_replacerequest.ReplaceRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class TigrisReplaceResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    replace_response: Optional[shared_replaceresponse.ReplaceResponse] = dataclasses.field(default=None)
    r"""OK"""  
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""  
    