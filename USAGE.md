<!-- Start SDK Example Usage -->


```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CacheCreateCacheRequest(
    create_cache_request=shared.CreateCacheRequest(
        options=shared.CreateCacheOptions(
            ttl_ms=548814,
        ),
    ),
    name='Kelvin Sporer',
    project='corrupti',
)

res = s.cache.create(req)

if res.create_cache_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->