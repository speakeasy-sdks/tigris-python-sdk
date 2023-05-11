"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from tigris.models import operations, shared
from typing import Any, Optional

class Project:
    r"""Every Tigris projects comes with a transactional document database built on FoundationDB, one of the most resilient and battle-tested open source distributed key-value store. A database is created automatically for you when you create a project."""
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
        
    
    def create(self, request_body: dict[str, Any], project: str) -> operations.TigrisCreateProjectResponse:
        r"""Create Project
        Creates a new project. Returns an AlreadyExists error with a status code 409 if the project already exists.
        """
        request = operations.TigrisCreateProjectRequest(
            request_body=request_body,
            project=project,
        )
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisCreateProjectRequest, base_url, '/v1/projects/{project}/create', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisCreateProjectResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateProjectResponse])
                res.create_project_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    
    def delete_project(self, request_body: dict[str, Any], project: str) -> operations.TigrisDeleteProjectResponse:
        r"""Delete Project and all resources under project
        Delete Project deletes all the collections in this project along with all of the documents, and associated metadata for these collections.
        """
        request = operations.TigrisDeleteProjectRequest(
            request_body=request_body,
            project=project,
        )
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TigrisDeleteProjectRequest, base_url, '/v1/projects/{project}/delete', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisDeleteProjectResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeleteProjectResponse])
                res.delete_project_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    
    def list(self) -> operations.TigrisListProjectsResponse:
        r"""List Projects
        List returns all the projects.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/projects'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TigrisListProjectsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListProjectsResponse])
                res.list_projects_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    