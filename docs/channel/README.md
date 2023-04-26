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
    channel="eligendi",
    project="sint",
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
    channel="aliquid",
    end="provident",
    event="necessitatibus",
    limit=572252,
    project="officia",
    session_id="dolor",
    socket_id="debitis",
    start="a",
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
    project="dolorum",
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
    channel="in",
    page=449198,
    page_size=846409,
    project="maiores",
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
        channel="rerum",
        messages=[
            shared.Message(
                data="magnam",
                id="cd66ae39-5efb-49ba-88f3-a66997074ba4",
                name="Laurie Mosciski",
                sequence="vero",
            ),
        ],
        project="aspernatur",
    ),
    channel="architecto",
    project="magnam",
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
    channel="et",
    project="excepturi",
)

res = s.channel.realtime_presence(req)

if res.presence_response is not None:
    # handle response
```
