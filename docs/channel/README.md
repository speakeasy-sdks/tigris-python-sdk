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


res = s.channel.get('iusto', 'dicta')

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
    channel='harum',
    end='enim',
    event='accusamus',
    limit=414263,
    project='repudiandae',
    session_id='quae',
    socket_id='ipsum',
    start='quidem',
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


res = s.channel.list('molestias')

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


res = s.channel.list_subscriptions('excepturi', 'pariatur', 265389, 508969)

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
    channel='rem',
    messages=[
        shared.Message(
            data='quasi',
            id='e91e450a-d2ab-4d44-a698-02d502a94bb4',
            name='Andre Franey',
            sequence='aliquid',
        ),
        shared.Message(
            data='provident',
            id='e9a3efa7-7dfb-414c-966a-e395efb9ba88',
            name='Vincent Nolan',
            sequence='natus',
        ),
        shared.Message(
            data='omnis',
            id='7074ba44-69b6-4e21-8195-9890afa563e2',
            name='Joyce Kertzmann',
            sequence='eius',
        ),
        shared.Message(
            data='maxime',
            id='8b711e5b-7fd2-4ed0-a892-1cddc692601f',
            name='Clyde Kling',
            sequence='eaque',
        ),
    ],
    project='pariatur',
), 'nemo', 'voluptatibus')

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


res = s.channel.realtime_presence('perferendis', 'fugiat')

if res.presence_response is not None:
    # handle response
```
