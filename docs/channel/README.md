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
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RealtimeGetRTChannelRequest(
    channel='modi',
    project='qui',
)

res = s.channel.get(req)

if res.get_rt_channel_response is not None:
    # handle response
```

## get_messages

Get all messages for a channel

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RealtimeReadMessagesRequest(
    channel='aliquid',
    end='cupiditate',
    event='quos',
    limit=20107,
    project='magni',
    session_id='assumenda',
    socket_id='ipsam',
    start='alias',
)

res = s.channel.get_messages(req)

if res.read_messages_response is not None:
    # handle response
```

## list

Get all channels for your application project

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RealtimeGetRTChannelsRequest(
    project='fugit',
)

res = s.channel.list(req)

if res.get_rt_channels_response is not None:
    # handle response
```

## list_subscriptions

Get the subscriptions details about a channel

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RealtimeListSubscriptionsRequest(
    channel='dolorum',
    page=569618,
    page_size=270008,
    project='facilis',
)

res = s.channel.list_subscriptions(req)

if res.list_subscription_response is not None:
    # handle response
```

## push_messages

push messages to a single channel

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RealtimeMessagesRequest(
    messages_request=shared.MessagesRequest(
        channel='tempore',
        messages=[
            shared.Message(
                data='delectus',
                id='63c969e9-a3ef-4a77-9fb1-4cd66ae395ef',
                name='Rene Reinger',
                sequence='deleniti',
            ),
            shared.Message(
                data='sapiente',
                id='3a669970-74ba-4446-9b6e-2141959890af',
                name='Tommy Kemmer',
                sequence='odit',
            ),
        ],
        project='nemo',
    ),
    channel='quasi',
    project='iure',
)

res = s.channel.push_messages(req)

if res.messages_response is not None:
    # handle response
```

## realtime_presence

Presence about the channel

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RealtimePresenceRequest(
    channel='doloribus',
    project='debitis',
)

res = s.channel.realtime_presence(req)

if res.presence_response is not None:
    # handle response
```
