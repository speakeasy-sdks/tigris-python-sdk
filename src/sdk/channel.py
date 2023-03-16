import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Channel:
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
        
    def get(self, request: operations.RealtimeGetRTChannelRequest) -> operations.RealtimeGetRTChannelResponse:
        r"""Get the details about a channel
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.RealtimeGetRTChannelPathParams, base_url, '/v1/projects/{project}/realtime/channels/{channel}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RealtimeGetRTChannelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetRTChannelResponse])
                res.get_rt_channel_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def get_messages(self, request: operations.RealtimeReadMessagesRequest) -> operations.RealtimeReadMessagesResponse:
        r"""Get all messages for a channel
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.RealtimeReadMessagesPathParams, base_url, '/v1/projects/{project}/realtime/channels/{channel}/messages', request.path_params)
        
        query_params = utils.get_query_params(operations.RealtimeReadMessagesQueryParams, request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RealtimeReadMessagesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ReadMessagesResponse])
                res.read_messages_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def list(self, request: operations.RealtimeGetRTChannelsRequest) -> operations.RealtimeGetRTChannelsResponse:
        r"""Get all channels for your application project
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.RealtimeGetRTChannelsPathParams, base_url, '/v1/projects/{project}/realtime/channels', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RealtimeGetRTChannelsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetRTChannelsResponse])
                res.get_rt_channels_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def list_subscriptions(self, request: operations.RealtimeListSubscriptionsRequest) -> operations.RealtimeListSubscriptionsResponse:
        r"""Get the subscriptions details about a channel
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.RealtimeListSubscriptionsPathParams, base_url, '/v1/projects/{project}/realtime/channels/{channel}/subscriptions', request.path_params)
        
        query_params = utils.get_query_params(operations.RealtimeListSubscriptionsQueryParams, request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RealtimeListSubscriptionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListSubscriptionResponse])
                res.list_subscription_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def push_messages(self, request: operations.RealtimeMessagesRequest) -> operations.RealtimeMessagesResponse:
        r"""push messages to a single channel
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.RealtimeMessagesPathParams, base_url, '/v1/projects/{project}/realtime/channels/{channel}/messages', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RealtimeMessagesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.MessagesResponse])
                res.messages_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    def realtime_presence(self, request: operations.RealtimePresenceRequest) -> operations.RealtimePresenceResponse:
        r"""Presence about the channel
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.RealtimePresencePathParams, base_url, '/v1/projects/{project}/realtime/channels/{channel}/presence', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RealtimePresenceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PresenceResponse])
                res.presence_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Status])
                res.status = out

        return res

    