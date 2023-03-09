<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()
s.config_security(
    security=shared.Security(
        bearer_auth=shared.SchemeBearerAuth(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
    )
)
   
req = operations.TigrisCreateAppKeyRequest(
    path_params=operations.TigrisCreateAppKeyPathParams(
        project="unde",
    ),
    request=shared.CreateAppKeyRequest(
        description="deserunt",
        name="porro",
    ),
)
    
res = s.application_keys.tigris_create_app_key(req)

if res.create_app_key_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->