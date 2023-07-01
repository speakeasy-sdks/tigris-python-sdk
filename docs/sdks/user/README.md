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
        metadata_key='distinctio',
        value=shared.GetUserMetadataRequestValue(),
    ),
    metadata_key='quod',
)

res = s.user.get_metadata(req)

if res.get_user_metadata_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ManagementGetUserMetadataRequest](../../models/operations/managementgetusermetadatarequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.ManagementGetUserMetadataResponse](../../models/operations/managementgetusermetadataresponse.md)**


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
        metadata_key='odio',
        value=shared.InsertUserMetadataRequestValue(),
    ),
    metadata_key='similique',
)

res = s.user.insert_metadata(req)

if res.insert_user_metadata_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ManagementInsertUserMetadataRequest](../../models/operations/managementinsertusermetadatarequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.ManagementInsertUserMetadataResponse](../../models/operations/managementinsertusermetadataresponse.md)**


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
        metadata_key='facilis',
        value=shared.UpdateUserMetadataRequestValue(),
    ),
    metadata_key='vero',
)

res = s.user.update_metadata(req)

if res.update_user_metadata_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ManagementUpdateUserMetadataRequest](../../models/operations/managementupdateusermetadatarequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.ManagementUpdateUserMetadataResponse](../../models/operations/managementupdateusermetadataresponse.md)**
