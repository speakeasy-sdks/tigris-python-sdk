# AppKey
(*app_key*)

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
        bearer_auth="",
    ),
)

req = operations.TigrisDeleteAppKeyRequest(
    delete_app_key_request=shared.DeleteAppKeyRequest(
        id='<ID>',
    ),
    project='Architect Cotton port',
)

res = s.app_key.delete(req)

if res.delete_app_key_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.TigrisDeleteAppKeyRequest](../../models/operations/tigrisdeleteappkeyrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.TigrisDeleteAppKeyResponse](../../models/operations/tigrisdeleteappkeyresponse.md)**


## list

Lists all app keys visible to requesting actor.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisListAppKeysRequest(
    project='Bronze Architect',
)

res = s.app_key.list(req)

if res.list_app_keys_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.TigrisListAppKeysRequest](../../models/operations/tigrislistappkeysrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.TigrisListAppKeysResponse](../../models/operations/tigrislistappkeysresponse.md)**


## rotate

Endpoint is used to rotate the secret for the app key.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisRotateAppKeySecretRequest(
    rotate_app_key_request=shared.RotateAppKeyRequest(
        id='<ID>',
        project='Facilitator',
    ),
    project='efficient compress',
)

res = s.app_key.rotate(req)

if res.rotate_app_key_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.TigrisRotateAppKeySecretRequest](../../models/operations/tigrisrotateappkeysecretrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.TigrisRotateAppKeySecretResponse](../../models/operations/tigrisrotateappkeysecretresponse.md)**


## tigris_create_app_key

Create an app key.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisCreateAppKeyRequest(
    create_app_key_request=shared.CreateAppKeyRequest(
        description='User-centric bifurcated product',
        name='magenta',
    ),
    project='indigo',
)

res = s.app_key.tigris_create_app_key(req)

if res.create_app_key_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.TigrisCreateAppKeyRequest](../../models/operations/tigriscreateappkeyrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.TigrisCreateAppKeyResponse](../../models/operations/tigriscreateappkeyresponse.md)**


## update

Update the description of an app key.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisUpdateAppKeyRequest(
    update_app_key_request=shared.UpdateAppKeyRequest(
        description='Optimized 24/7 middleware',
        id='<ID>',
        name='Clothing Tempe',
    ),
    project='Ohio ADP',
)

res = s.app_key.update(req)

if res.update_app_key_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.TigrisUpdateAppKeyRequest](../../models/operations/tigrisupdateappkeyrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.TigrisUpdateAppKeyResponse](../../models/operations/tigrisupdateappkeyresponse.md)**

