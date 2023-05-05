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

req = operations.TigrisDeleteAppKeyRequest(
    delete_app_key_request=shared.DeleteAppKeyRequest(
        id='d69a674e-0f46-47cc-8796-ed151a05dfc2',
    ),
    project='at',
)

res = s.app_key.delete(req)

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

req = operations.TigrisListAppKeysRequest(
    project='at',
)

res = s.app_key.list(req)

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

req = operations.TigrisRotateAppKeySecretRequest(
    rotate_app_key_request=shared.RotateAppKeyRequest(
        id='f7cc78ca-1ba9-428f-8816-742cb7392059',
        project='sed',
    ),
    project='iste',
)

res = s.app_key.rotate(req)

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

req = operations.TigrisCreateAppKeyRequest(
    create_app_key_request=shared.CreateAppKeyRequest(
        description='dolor',
        name='Lester Welch',
    ),
    project='in',
)

res = s.app_key.tigris_create_app_key(req)

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

req = operations.TigrisUpdateAppKeyRequest(
    update_app_key_request=shared.UpdateAppKeyRequest(
        description='corporis',
        id='96eb10fa-aa23-452c-9955-907aff1a3a2f',
        name='Tracy Fritsch',
    ),
    project='molestiae',
)

res = s.app_key.update(req)

if res.update_app_key_response is not None:
    # handle response
```
