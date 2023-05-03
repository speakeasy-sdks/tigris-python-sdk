# cache

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
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CacheCreateCacheRequest(
    create_cache_request=shared.CreateCacheRequest(
        options=shared.CreateCacheOptions(
            ttl_ms=244425,
        ),
    ),
    name='Miss Eugene Hauck',
    project='enim',
)

res = s.cache.create(req)

if res.create_cache_response is not None:
    # handle response
```

## delete

Deletes the cache

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CacheDeleteCacheRequest(
    request_body={
        "quo": 'sequi',
    },
    name='Vernon Ondricka Sr.',
    project='error',
)

res = s.cache.delete(req)

if res.delete_cache_response is not None:
    # handle response
```

## delete_keys

Deletes an entry from cache

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CacheDelRequest(
    request_body={
        "laborum": 'quasi',
        "reiciendis": 'voluptatibus',
        "vero": 'nihil',
        "praesentium": 'voluptatibus',
    },
    key='ipsa',
    name='Mr. Jared Ritchie',
    project='ut',
)

res = s.cache.delete_keys(req)

if res.del_response is not None:
    # handle response
```

## get_key

Reads an entry from cache

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CacheGetRequest(
    key='maiores',
    name='Stacy Gulgowski MD',
    project='enim',
)

res = s.cache.get_key(req)

if res.get_response is not None:
    # handle response
```

## get_set_key

Sets an entry in the cache and returns the previous value if exists

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CacheGetSetRequest(
    get_set_request=shared.GetSetRequest(
        value='accusamus',
    ),
    key='commodi',
    name='Eric Emmerich',
    project='excepturi',
)

res = s.cache.get_set_key(req)

if res.get_set_response is not None:
    # handle response
```

## list

Lists all the caches for the given project

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CacheListCachesRequest(
    project='pariatur',
)

res = s.cache.list(req)

if res.list_caches_response is not None:
    # handle response
```

## list_keys

Lists all the key for this cache

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CacheKeysRequest(
    count=265389,
    cursor=508969,
    name='Grady Botsford',
    pattern='veritatis',
    project='itaque',
)

res = s.cache.list_keys(req)

if res.keys_response is not None:
    # handle response
```

## set_key

Sets an entry in the cache

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CacheSetRequest(
    set_request=shared.SetRequest(
        ex=277718,
        nx=False,
        px=318569,
        value='consequatur',
        xx=False,
    ),
    key='est',
    name='Benjamin O'Connell',
    project='labore',
)

res = s.cache.set_key(req)

if res.set_response is not None:
    # handle response
```
