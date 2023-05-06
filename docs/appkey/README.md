# app_key

## Overview

The application keys section provide APIs that can be used to manage application keys for your project. A single project can have one or more application keys.

### Available Operations

* [delete](#delete) - Deletes the app key
* [list](#list) - List all the app keys
* [rotate](#rotate) - Rotates the app key secret
* [tigris_create_app_key](#tigris_create_app_key) - Creates the app key
* [update](#update) - Updates the description of the app key

## delete

Delete an app key.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.app_key.delete(shared.DeleteAppKeyRequest(
    id='d9d8d69a-674e-40f4-a7cc-8796ed151a05',
), 'repellendus')

if res.delete_app_key_response is not None:
    # handle response
```

## list

Lists all app keys visible to requesting actor.

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.app_key.list('sapiente')

if res.list_app_keys_response is not None:
    # handle response
```

## rotate

Endpoint is used to rotate the secret for the app key.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.app_key.rotate(shared.RotateAppKeyRequest(
    id='c2ddf7cc-78ca-41ba-928f-c816742cb739',
    project='aspernatur',
), 'perferendis')

if res.rotate_app_key_response is not None:
    # handle response
```

## tigris_create_app_key

Create an app key.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.app_key.tigris_create_app_key(shared.CreateAppKeyRequest(
    description='ad',
    name='Louis Moore',
), 'laboriosam')

if res.create_app_key_response is not None:
    # handle response
```

## update

Update the description of an app key.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.app_key.update(shared.UpdateAppKeyRequest(
    description='hic',
    id='ea7596eb-10fa-4aa2-b52c-5955907aff1a',
    name='Cecilia Crooks',
), 'occaecati')

if res.update_app_key_response is not None:
    # handle response
```
