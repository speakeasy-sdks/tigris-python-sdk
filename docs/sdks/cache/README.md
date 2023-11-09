# Cache
(*cache*)

## Overview

The cache section provide APIs that can be used to perform cache operations.

### Available Operations

* [create](#create) - Creates the cache
* [delete](#delete) - Deletes the cache
* [delete_keys](#delete_keys) - Deletes an entry from cache
* [get_key](#get_key) - Reads an entry from cache
* [get_set_key](#get_set_key) - Sets an entry in the cache and returns the previous value if exists
* [list](#list) - Lists all the caches for the given project
* [list_keys](#list_keys) - Lists all the key for this cache
* [set_key](#set_key) - Sets an entry in the cache

## create

Creates the cache

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="",
)

req = operations.CacheCreateCacheRequest(
    create_cache_request=shared.CreateCacheRequest(
        options=shared.CreateCacheOptions(),
    ),
    name='string',
    project='string',
)

res = s.cache.create(req)

if res.create_cache_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CacheCreateCacheRequest](../../models/operations/cachecreatecacherequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CacheCreateCacheResponse](../../models/operations/cachecreatecacheresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete

Deletes the cache

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="",
)

req = operations.CacheDeleteCacheRequest(
    delete_cache_request=shared.DeleteCacheRequest(),
    name='string',
    project='string',
)

res = s.cache.delete(req)

if res.delete_cache_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CacheDeleteCacheRequest](../../models/operations/cachedeletecacherequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CacheDeleteCacheResponse](../../models/operations/cachedeletecacheresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_keys

Deletes an entry from cache

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="",
)

req = operations.CacheDelRequest(
    del_request=shared.DelRequest(),
    key='<key>',
    name='string',
    project='string',
)

res = s.cache.delete_keys(req)

if res.del_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.CacheDelRequest](../../models/operations/cachedelrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CacheDelResponse](../../models/operations/cachedelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_key

Reads an entry from cache

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    bearer_auth="",
)

req = operations.CacheGetRequest(
    key='<key>',
    name='string',
    project='string',
)

res = s.cache.get_key(req)

if res.get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.CacheGetRequest](../../models/operations/cachegetrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CacheGetResponse](../../models/operations/cachegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_set_key

Sets an entry in the cache and returns the previous value if exists

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="",
)

req = operations.CacheGetSetRequest(
    get_set_request=shared.GetSetRequest(),
    key='<key>',
    name='string',
    project='string',
)

res = s.cache.get_set_key(req)

if res.get_set_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CacheGetSetRequest](../../models/operations/cachegetsetrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CacheGetSetResponse](../../models/operations/cachegetsetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list

Lists all the caches for the given project

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    bearer_auth="",
)

req = operations.CacheListCachesRequest(
    project='string',
)

res = s.cache.list(req)

if res.list_caches_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CacheListCachesRequest](../../models/operations/cachelistcachesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CacheListCachesResponse](../../models/operations/cachelistcachesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_keys

Lists all the key for this cache

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    bearer_auth="",
)

req = operations.CacheKeysRequest(
    name='string',
    project='string',
)

res = s.cache.list_keys(req)

if res.keys_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.CacheKeysRequest](../../models/operations/cachekeysrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CacheKeysResponse](../../models/operations/cachekeysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## set_key

Sets an entry in the cache

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="",
)

req = operations.CacheSetRequest(
    set_request=shared.SetRequest(),
    key='<key>',
    name='string',
    project='string',
)

res = s.cache.set_key(req)

if res.set_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.CacheSetRequest](../../models/operations/cachesetrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CacheSetResponse](../../models/operations/cachesetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
