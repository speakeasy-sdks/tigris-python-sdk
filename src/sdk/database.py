import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Database:
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
        
    def tigris_begin_transaction(self, request: operations.TigrisBeginTransactionRequest) -> operations.TigrisBeginTransactionResponse:
        r"""Begin a transaction
        Starts a new transaction and returns a transactional object. All reads/writes performed
         within a transaction will run with serializable isolation. Tigris offers global transactions,
         with ACID properties and strict serializability.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/database/transactions/begin', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisBeginTransactionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BeginTransactionResponse])
                res.begin_transaction_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def tigris_commit_transaction(self, request: operations.TigrisCommitTransactionRequest) -> operations.TigrisCommitTransactionResponse:
        r"""Commit a Transaction
        Atomically commit all the changes performed in the context of the transaction. Commit provides all
         or nothing semantics by ensuring no partial updates are in the project due to a transaction failure.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/database/transactions/commit', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisCommitTransactionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CommitTransactionResponse])
                res.commit_transaction_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def tigris_create_branch(self, request: operations.TigrisCreateBranchRequest) -> operations.TigrisCreateBranchResponse:
        r"""Create a database branch
        Creates a new database branch, if not already existing.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/database/branches/{branch}/create', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisCreateBranchResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateBranchResponse])
                res.create_branch_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def tigris_delete_branch(self, request: operations.TigrisDeleteBranchRequest) -> operations.TigrisDeleteBranchResponse:
        r"""Delete a database branch
        Deletes a database branch, if exists.
         Throws 400 Bad Request if \"main\" branch is being deleted
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/database/branches/{branch}/delete', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisDeleteBranchResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeleteBranchResponse])
                res.delete_branch_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def tigris_describe_database(self, request: operations.TigrisDescribeDatabaseRequest) -> operations.TigrisDescribeDatabaseResponse:
        r"""Describe database
        This API returns information related to the project along with all the collections inside the project.
         This can be used to retrieve the size of the project or to retrieve schemas, branches and the size of all the collections present in this project.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/database/describe', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisDescribeDatabaseResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DescribeDatabaseResponse])
                res.describe_database_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def tigris_list_branches(self, request: operations.TigrisListBranchesRequest) -> operations.TigrisListBranchesResponse:
        r"""List database branches
        List database branches
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/database/branches', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisListBranchesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListBranchesResponse])
                res.list_branches_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def tigris_list_collections(self, request: operations.TigrisListCollectionsRequest) -> operations.TigrisListCollectionsResponse:
        r"""List Collections
        List all the collections present in the project passed in the request.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/database/collections', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisListCollectionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListCollectionsResponse])
                res.list_collections_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def tigris_rollback_transaction(self, request: operations.TigrisRollbackTransactionRequest) -> operations.TigrisRollbackTransactionResponse:
        r"""Rollback a transaction
        Rollback transaction discards all the changes
         performed in the transaction
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/projects/{project}/database/transactions/rollback', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisRollbackTransactionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.RollbackTransactionResponse])
                res.rollback_transaction_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    