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


res = s.channel.get('quasi', 'reiciendis')

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
    channel='voluptatibus',
    end='vero',
    event='nihil',
    limit=509624,
    project='voluptatibus',
    session_id='ipsa',
    socket_id='omnis',
    start='voluptate',
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


res = s.channel.list('cum')

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


res = s.channel.push_messages(shared.MessagesRequest(
    channel='perferendis',
    messages=[
        shared.Message(
            data='reprehenderit',
            id='4f15471b-5e6e-413b-99d4-88e1e91e450a',
            name='Benjamin O'Connell',
            sequence='labore',
        ),
    ],
    project='modi',
), 'qui', 'aliquid')

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


res = s.channel.realtime_presence('cupiditate', 'quos')

if res.presence_response is not None:
    # handle response
```
