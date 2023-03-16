<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth=shared.SchemeBearerAuth(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
    ),
)

   
req = operations.TigrisDeleteAppKeyRequest(
    path_params=operations.TigrisDeleteAppKeyPathParams(
        project="unde",
    ),
    request=shared.DeleteAppKeyRequest(
        id="deserunt",
    ),
)
    
res = s.app_key.delete(req)

if res.delete_app_key_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->