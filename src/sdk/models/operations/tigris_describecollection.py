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
    project: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TigrisDescribeCollectionRequest:
    path_params: TigrisDescribeCollectionPathParams = dataclasses.field()
    request: shared_describecollectionrequest.DescribeCollectionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TigrisDescribeCollectionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    describe_collection_response: Optional[shared_describecollectionresponse.DescribeCollectionResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    