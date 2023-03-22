"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import describecollectionrequest as shared_describecollectionrequest
from ..shared import describecollectionresponse as shared_describecollectionresponse
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class TigrisDescribeCollectionPathParams:
    
    collection: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection', 'style': 'simple', 'explode': False }})
    r"""Name of the collection."""  
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    r"""Project name whose db is under target to get description of its collection."""  
    

@dataclasses.dataclass
class TigrisDescribeCollectionRequest:
    
    path_params: TigrisDescribeCollectionPathParams = dataclasses.field()  
    request: shared_describecollectionrequest.DescribeCollectionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class TigrisDescribeCollectionResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    describe_collection_response: Optional[shared_describecollectionresponse.DescribeCollectionResponse] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""Default error response"""  
    