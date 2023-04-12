<!-- Start SDK Example Usage -->
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
        id="corrupti",
    ),
    project="provident",
)
    
res = s.app_key.delete(req)

if res.delete_app_key_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->