<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.TigrisDeleteAppKeyRequest(
    delete_app_key_request=shared.DeleteAppKeyRequest(
        id="unde",
    ),
    project="deserunt",
)
    
res = s.app_key.delete(req)

if res.delete_app_key_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->