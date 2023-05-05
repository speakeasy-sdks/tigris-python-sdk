<!-- Start SDK Example Usage -->
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
        ttl_ms=548814,
    ),
), 'provident', 'distinctio')

if res.create_cache_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->