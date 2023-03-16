import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Collection:
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
        
    def create(self, request: operations.TigrisCreateOrUpdateCollectionRequest) -> operations.TigrisCreateOrUpdateCollectionResponse:
        r"""Create or update a collection
        Creates a new collection or atomically upgrades the collection to the new schema provided in the request.
         Schema changes are applied atomically and immediately without any downtime.
         Tigris Offers two types of collections: <p></p>
            <li> `DOCUMENTS`: Offers rich CRUD APIs.
            <li> `MESSAGES`: Offers event streaming APIs.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisCreateOrUpdateCollectionPathParams, base_url, '/v1/projects/{project}/database/collections/{collection}/createOrUpdate', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisCreateOrUpdateCollectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateOrUpdateCollectionResponse])
                res.create_or_update_collection_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def delete_documents(self, request: operations.TigrisDeleteRequest) -> operations.TigrisDeleteResponse:
        r"""Delete Documents
        Delete a range of documents in the collection using the condition provided in the filter.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisDeletePathParams, base_url, '/v1/projects/{project}/database/collections/{collection}/documents/delete', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisDeleteResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeleteResponse])
                res.delete_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def describe(self, request: operations.TigrisDescribeCollectionRequest) -> operations.TigrisDescribeCollectionResponse:
        r"""Describe Collection
        Returns the information related to the collection. This can be used to retrieve the schema or size of the collection.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisDescribeCollectionPathParams, base_url, '/v1/projects/{project}/database/collections/{collection}/describe', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisDescribeCollectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DescribeCollectionResponse])
                res.describe_collection_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def drop(self, request: operations.TigrisDropCollectionRequest) -> operations.TigrisDropCollectionResponse:
        r"""Drop Collection
        Drops the collection inside this project. This API deletes all of the
         documents inside this collection and any metadata associated with it.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisDropCollectionPathParams, base_url, '/v1/projects/{project}/database/collections/{collection}/drop', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisDropCollectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DropCollectionResponse])
                res.drop_collection_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def import_documents(self, request: operations.TigrisImportRequest) -> operations.TigrisImportResponse:
        r"""Import Documents
        Imports documents into the collection.
        
         It automatically:
          * Detects the schema of the documents in the batch
          * Evolves the schema as soon as it's backward compatible
          * Creates collection with inferred schema (if requested)
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisImportPathParams, base_url, '/v1/projects/{project}/database/collections/{collection}/documents/import', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisImportResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ImportResponse])
                res.import_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def insert_documents(self, request: operations.TigrisInsertRequest) -> operations.TigrisInsertResponse:
        r"""Insert Documents
        Inserts new documents in the collection and returns an AlreadyExists error if any of the documents
         in the request already exists. Insert provides idempotency by returning an error if the document
         already exists. To replace documents, use REPLACE API instead of INSERT.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisInsertPathParams, base_url, '/v1/projects/{project}/database/collections/{collection}/documents/insert', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisInsertResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InsertResponse])
                res.insert_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def read_documents(self, request: operations.TigrisReadRequest) -> operations.TigrisReadResponse:
        r"""Read Documents
        Reads a range of documents from the collection, or messages from a collection in case of event streaming. Tigris does not require you to
         index any fields and automatically index all the fields which means you can filter by any field in the document.
         An empty filter will trigger reading all the documents inside this collection. The API supports pagination that
         can be used by passing `Limit/Skip` parameters. The `skip` parameter skips the number of documents from the start and
         the `limit` parameter is used to specify the number of documents to read. You can find more detailed documentation
         of the Read API <a href=\"https://docs.tigrisdata.com/overview/query\" title=\"here\">here</a>.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisReadPathParams, base_url, '/v1/projects/{project}/database/collections/{collection}/documents/read', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisReadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.StreamingReadResponse])
                res.streaming_read_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def replace_documents(self, request: operations.TigrisReplaceRequest) -> operations.TigrisReplaceResponse:
        r"""Insert or Replace Documents
        Inserts the documents or replaces the existing documents in the collections.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisReplacePathParams, base_url, '/v1/projects/{project}/database/collections/{collection}/documents/replace', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisReplaceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ReplaceResponse])
                res.replace_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def search_documents(self, request: operations.TigrisSearchRequest) -> operations.TigrisSearchResponse:
        r"""Search Documents.
        Searches a collection for the documents matching the query, or messages in case of event streaming. A search can be
         a term search or a phrase search. Search API allows filtering the result set using filters as documented <a href=\"https://docs.tigrisdata.com/overview/query#specification-1\" title=\"here\">here</a>.
         You can also perform a faceted search by passing the fields in the facet parameter.
         You can find more detailed documentation of the Search API with multiple examples <a href=\"https://docs.tigrisdata.com/overview/search\" title=\"here\">here</a>.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisSearchPathParams, base_url, '/v1/projects/{project}/database/collections/{collection}/documents/search', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisSearchResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.StreamingSearchResponse])
                res.streaming_search_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def update_documents(self, request: operations.TigrisUpdateRequest) -> operations.TigrisUpdateResponse:
        r"""Update Documents.
        Update a range of documents in the collection using the condition provided in the filter.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisUpdatePathParams, base_url, '/v1/projects/{project}/database/collections/{collection}/documents/update', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisUpdateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UpdateResponse])
                res.update_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    