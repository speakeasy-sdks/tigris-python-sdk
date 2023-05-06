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


res = s.cache.create(shared.CreateCacheRequest(
    options=shared.CreateCacheOptions(
        ttl_ms=253291,
    ),
), 'commodi', 'quam')

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


res = s.cache.delete({
    "velit": 'error',
    "quia": 'quis',
}, 'vitae', 'laborum')

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


res = s.cache.get_key('animi', 'enim', 'odit')

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


res = s.cache.list('quo')

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
    count=196582,
    cursor=949572,
    name='Mr. Alberta Schuster',
    pattern='temporibus',
    project='laborum',
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


res = s.cache.set_key(req)

if res.set_response is not None:
    # handle response
```
