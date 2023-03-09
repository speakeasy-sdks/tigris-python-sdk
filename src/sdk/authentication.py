import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Authentication:
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
        
    def auth_get_access_token(self) -> operations.AuthGetAccessTokenResponse:
        r"""Access Token
        Endpoint for receiving access token from Tigris Server. The endpoint requires Grant Type(`grant_type`) which has
         two possible values <i>\"REFRESH_TOKEN\"</i> or <i>\"CLIENT_CREDENTIALS\"</i> based on which either Refresh token(`refresh_token`)
         needs to be set or client credentials(`client_id`, `client_secret`).
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/auth/token'
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AuthGetAccessTokenResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetAccessTokenResponse])
                res.get_access_token_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    