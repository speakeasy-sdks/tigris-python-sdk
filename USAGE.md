<!-- Start SDK Example Usage [usage] -->
```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.CacheCreateCacheRequest(
    create_cache_request=shared.CreateCacheRequest(),
    name='string',
    project='string',
)

res = s.cache.create(req)

if res.create_cache_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->