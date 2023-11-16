<!-- Start SDK Example Usage -->
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
<!-- End SDK Example Usage -->