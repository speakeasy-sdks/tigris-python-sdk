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
        bearer_auth="",
    ),
)

req = operations.ManagementGetUserMetadataRequest(
    get_user_metadata_request=shared.GetUserMetadataRequest(
        metadata_key='consectetur',
        value={
            "iste": 'temporibus',
        },
    ),
    metadata_key='accusantium',
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
        bearer_auth="",
    ),
)

req = operations.ManagementInsertUserMetadataRequest(
    insert_user_metadata_request=shared.InsertUserMetadataRequest(
        metadata_key='rem',
        value={
            "laudantium": 'eum',
        },
    ),
    metadata_key='mollitia',
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
        bearer_auth="",
    ),
)

req = operations.ManagementUpdateUserMetadataRequest(
    update_user_metadata_request=shared.UpdateUserMetadataRequest(
        metadata_key='ab',
        value={
            "non": 'voluptatem',
            "dolor": 'occaecati',
            "numquam": 'impedit',
        },
    ),
    metadata_key='explicabo',
)

res = s.user.update_metadata(req)

if res.update_user_metadata_response is not None:
    # handle response
```
