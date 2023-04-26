# user

## Overview

A User on the Tigris Platform.

### Available Operations

* [get_metadata](#get_metadata) - Reads the User Metadata
* [insert_metadata](#insert_metadata) - Inserts User Metadata
* [update_metadata](#update_metadata) - Updates User Metadata

## get_metadata

GetUserMetadata inserts the user metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ManagementGetUserMetadataRequest(
    get_user_metadata_request=shared.GetUserMetadataRequest(
        metadata_key="qui",
        value={
            "ex": "deleniti",
            "itaque": "dolorum",
            "architecto": "omnis",
            "tenetur": "quasi",
        },
    ),
    metadata_key="at",
)

res = s.user.get_metadata(req)

if res.get_user_metadata_response is not None:
    # handle response
```

## insert_metadata

insertUserMetadata inserts the user metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ManagementInsertUserMetadataRequest(
    insert_user_metadata_request=shared.InsertUserMetadataRequest(
        metadata_key="et",
        value={
            "ipsa": "minima",
            "veritatis": "consectetur",
        },
    ),
    metadata_key="adipisci",
)

res = s.user.insert_metadata(req)

if res.insert_user_metadata_response is not None:
    # handle response
```

## update_metadata

updateUserMetadata updates the user metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ManagementUpdateUserMetadataRequest(
    update_user_metadata_request=shared.UpdateUserMetadataRequest(
        metadata_key="iste",
        value={
            "accusantium": "rem",
            "aut": "laudantium",
            "eum": "mollitia",
            "ab": "corrupti",
        },
    ),
    metadata_key="non",
)

res = s.user.update_metadata(req)

if res.update_user_metadata_response is not None:
    # handle response
```
