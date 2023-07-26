# channel

## Overview

The realtime section provide APIs that can be used realtime operations.

### Available Operations

* [get](#get) - Get the details about a channel
* [get_messages](#get_messages) - Get all messages for a channel
* [list](#list) - Get all channels for your application project
* [list_subscriptions](#list_subscriptions) - Get the subscriptions details about a channel
* [push_messages](#push_messages) - push messages to a single channel
* [realtime_presence](#realtime_presence) - Presence about the channel

## get

Get the details about a channel

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.RealtimeGetRTChannelRequest(
    channel='quasi',
    project='repudiandae',
)

res = s.channel.get(req)

if res.get_rt_channel_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RealtimeGetRTChannelRequest](../../models/operations/realtimegetrtchannelrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.RealtimeGetRTChannelResponse](../../models/operations/realtimegetrtchannelresponse.md)**


## get_messages

Get all messages for a channel

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.RealtimeReadMessagesRequest(
    channel='sint',
    end='veritatis',
    event='itaque',
    limit=277718,
    project='enim',
    session_id='consequatur',
    socket_id='est',
    start='quibusdam',
)

res = s.channel.get_messages(req)

if res.read_messages_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RealtimeReadMessagesRequest](../../models/operations/realtimereadmessagesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.RealtimeReadMessagesResponse](../../models/operations/realtimereadmessagesresponse.md)**


## list

Get all channels for your application project

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.RealtimeGetRTChannelsRequest(
    project='explicabo',
)

res = s.channel.list(req)

if res.get_rt_channels_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RealtimeGetRTChannelsRequest](../../models/operations/realtimegetrtchannelsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.RealtimeGetRTChannelsResponse](../../models/operations/realtimegetrtchannelsresponse.md)**


## list_subscriptions

Get the subscriptions details about a channel

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.RealtimeListSubscriptionsRequest(
    channel='deserunt',
    page=716327,
    page_size=841386,
    project='labore',
)

res = s.channel.list_subscriptions(req)

if res.list_subscription_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.RealtimeListSubscriptionsRequest](../../models/operations/realtimelistsubscriptionsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.RealtimeListSubscriptionsResponse](../../models/operations/realtimelistsubscriptionsresponse.md)**


## push_messages

push messages to a single channel

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.RealtimeMessagesRequest(
    messages_request=shared.MessagesRequest(
        channel='modi',
        messages=[
            shared.Message(
                data='aliquid',
                id='9802d502-a94b-4b4f-a3c9-69e9a3efa77d',
                name='Jean Buckridge',
                sequence='facere',
            ),
        ],
        project='ea',
    ),
    channel='aliquid',
    project='laborum',
)

res = s.channel.push_messages(req)

if res.messages_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RealtimeMessagesRequest](../../models/operations/realtimemessagesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.RealtimeMessagesResponse](../../models/operations/realtimemessagesresponse.md)**


## realtime_presence

Presence about the channel

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.RealtimePresenceRequest(
    channel='accusamus',
    project='non',
)

res = s.channel.realtime_presence(req)

if res.presence_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RealtimePresenceRequest](../../models/operations/realtimepresencerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.RealtimePresenceResponse](../../models/operations/realtimepresenceresponse.md)**

