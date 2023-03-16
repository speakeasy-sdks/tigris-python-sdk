import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Namespace:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def create(self, request: operations.CreateNamespaceRequest) -> operations.CreateNamespaceResponse:
        r"""Creates a Namespace
        Creates a new namespace, if it does not exist
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/management/namespaces/create'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateNamespaceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateNamespaceResponse])
                res.create_namespace_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def get(self) -> operations.ManagementDescribeNamespacesResponse:
        r"""Describe the details of all namespaces
        Get details for all namespaces
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/management/namespaces/describe'
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ManagementDescribeNamespacesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DescribeNamespacesResponse])
                res.describe_namespaces_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def get_metadata(self, request: operations.ManagementGetNamespaceMetadataRequest) -> operations.ManagementGetNamespaceMetadataResponse:
        r"""Reads the Namespace Metadata
        GetNamespaceMetadata inserts the user metadata object
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ManagementGetNamespaceMetadataPathParams, base_url, '/v1/management/namespace/metadata/{metadataKey}/get', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ManagementGetNamespaceMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetNamespaceMetadataResponse])
                res.get_namespace_metadata_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def insert_metadata(self, request: operations.ManagementInsertNamespaceMetadataRequest) -> operations.ManagementInsertNamespaceMetadataResponse:
        r"""Inserts Namespace Metadata
        InsertNamespaceMetadata inserts the namespace metadata object
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ManagementInsertNamespaceMetadataPathParams, base_url, '/v1/management/namespace/metadata/{metadataKey}/insert', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ManagementInsertNamespaceMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InsertNamespaceMetadataResponse])
                res.insert_namespace_metadata_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def list(self) -> operations.ManagementListNamespacesResponse:
        r"""Lists all Namespaces
        List all namespace
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/management/namespaces/list'
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ManagementListNamespacesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListNamespacesResponse])
                res.list_namespaces_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def update_metadata(self, request: operations.ManagementUpdateNamespaceMetadataRequest) -> operations.ManagementUpdateNamespaceMetadataResponse:
        r"""Updates Namespace Metadata
        UpdateNamespaceMetadata updates the user metadata object
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ManagementUpdateNamespaceMetadataPathParams, base_url, '/v1/management/namespace/metadata/{metadataKey}/update', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ManagementUpdateNamespaceMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UpdateNamespaceMetadataResponse])
                res.update_namespace_metadata_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    