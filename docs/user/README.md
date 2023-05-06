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


res = s.user.get_metadata(shared.GetUserMetadataRequest(
    metadata_key='recusandae',
    value={
        "minima": 'eaque',
    },
), 'a')

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


res = s.user.insert_metadata(shared.InsertUserMetadataRequest(
    metadata_key='libero',
    value={
        "aut": 'deleniti',
    },
), 'impedit')

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


res = s.user.update_metadata(shared.UpdateUserMetadataRequest(
    metadata_key='aliquam',
    value={
        "accusamus": 'inventore',
    },
), 'non')

if res.update_user_metadata_response is not None:
    # handle response
```
