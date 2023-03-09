import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Search:
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
        
    def create_document(self, request: operations.SearchCreateByIDRequest) -> operations.SearchCreateByIDResponse:
        r"""Create a single document
        CreateById is used for indexing a single document. The API expects a single document. An \"id\" is optional
         and the server can automatically generate it for you in case it is missing. In cases an id is provided in
         the document and the document already exists then that document will not be indexed and an error is returned
         with HTTP status code 409.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{index}/documents/{id}', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchCreateByIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateByIDResponse])
                res.create_by_id_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def create_documents(self, request: operations.SearchCreateRequest) -> operations.SearchCreateResponse:
        r"""Create multiple documents
        Create is used for indexing a single or multiple documents. The API expects an array of documents.
         Each document is a JSON object. An \"id\" is optional and the server can automatically generate it for you in
         case it is missing. In cases when an id is provided in the document and the document already exists then that
         document will not be indexed and in the response there will be an error corresponding to that document id other
         documents will succeed. Returns an array of status indicating the status of each document.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{index}/documents', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchCreateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateDocumentResponse])
                res.create_document_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def delete_documents(self, request: operations.SearchDeleteRequest) -> operations.SearchDeleteResponse:
        r"""Delete documents by ids
        Delete one or more documents by id. Returns an array of status indicating the status of each document. Each status
         has an error field that is set to null in case document is deleted successfully otherwise it will non null with
         an error code and message.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{index}/documents', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchDeleteResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeleteDocumentResponse])
                res.delete_document_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def delete_index(self, request: operations.SearchDeleteIndexRequest) -> operations.SearchDeleteIndexResponse:
        r"""Deletes search index
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{name}', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchDeleteIndexResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeleteIndexResponse])
                res.delete_index_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def find_documents(self, request: operations.SearchSearchRequest) -> operations.SearchSearchResponse:
        r"""Search Documents.
        Searches an index for the documents matching the query. A search can be a term search or a phrase search.
         Search API allows filtering the result set using filters as documented
         <a href=\"https://docs.tigrisdata.com/overview/query#specification-1\" title=\"here\">here</a>. You can also perform
         a faceted search by passing the fields in the facet parameter. You can find more detailed documentation of the
         Search API with multiple examples <a href=\"https://docs.tigrisdata.com/overview/search\" title=\"here\">here</a>.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{index}/documents/search', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchSearchResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SearchIndexResponse])
                res.search_index_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def get_documents(self, request: operations.SearchGetRequest) -> operations.SearchGetResponse:
        r"""Get a single or multiple documents
        Retrieves one or more documents by id. The response is an array of documents in the same order it is requests.
         A null is returned for the documents that are not found.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{index}/documents', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetDocumentResponse])
                res.get_document_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def get_index(self, request: operations.SearchGetIndexRequest) -> operations.SearchGetIndexResponse:
        r"""Get information about a search index
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{name}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchGetIndexResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetIndexResponse])
                res.get_index_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def list_indexes(self, request: operations.SearchListIndexesRequest) -> operations.SearchListIndexesResponse:
        r"""List search indexes
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchListIndexesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListIndexesResponse])
                res.list_indexes_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def query_delete_documents(self, request: operations.SearchDeleteByQueryRequest) -> operations.SearchDeleteByQueryResponse:
        r"""Delete documents by query
        DeleteByQuery is used to delete documents that match the filter. A filter is required. To delete document by id,
         you can pass the filter as follows ```{\"id\": \"test\"}```. Returns a count of number of documents deleted.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{index}/documents/deleteByQuery', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchDeleteByQueryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeleteByQueryResponse])
                res.delete_by_query_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def replace_documents(self, request: operations.SearchCreateOrReplaceRequest) -> operations.SearchCreateOrReplaceResponse:
        r"""Create or replace documents in an index
        Creates or replaces one or more documents. Each document is a JSON object. A document is replaced
         if it already exists. An \"id\" is generated automatically in case it is missing in the document. The
         document is created if \"id\" doesn't exists otherwise it is replaced. Returns an array of status indicating
         the status of each document.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{index}/documents', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchCreateOrReplaceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateOrReplaceDocumentResponse])
                res.create_or_replace_document_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def update_documents(self, request: operations.SearchUpdateRequest) -> operations.SearchUpdateResponse:
        r"""Update documents in an index
        Updates one or more documents by \"id\". Each document is required to have the
         \"id\" field in it. Returns an array of status indicating the status of each document. Each status
         has an error field that is set to null in case document is updated successfully otherwise the error
         field is set with a code and message.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{index}/documents', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchUpdateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UpdateDocumentResponse])
                res.update_document_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def update_index(self, request: operations.SearchCreateOrUpdateIndexRequest) -> operations.SearchCreateOrUpdateIndexResponse:
        r"""Creates or updates search index
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/search/indexes/{name}', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchCreateOrUpdateIndexResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateOrUpdateIndexResponse])
                res.create_or_update_index_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    