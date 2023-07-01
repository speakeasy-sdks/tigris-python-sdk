# namespace

## Overview

The Management section provide APIs that can be used to manage users, and app_keys.

### Available Operations

* [create](#create) - Creates a Namespace
* [get](#get) - Describe the details of all namespaces
* [get_metadata](#get_metadata) - Reads the Namespace Metadata
* [insert_metadata](#insert_metadata) - Inserts Namespace Metadata
* [list](#list) - Lists all Namespaces
* [update_metadata](#update_metadata) - Updates Namespace Metadata

## create

Creates a new namespace, if it does not exist

### Example Usage

```python
import tigris
from tigris.models import shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.CreateNamespaceRequest(
    code=982575,
    id='b576b0d5-f0d3-40c5-bbb2-587053202c73',
    name='Dean Welch',
)

res = s.namespace.create(req)

if res.create_namespace_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.CreateNamespaceRequest](../../models/shared/createnamespacerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateNamespaceResponse](../../models/operations/createnamespaceresponse.md)**


## get

Get details for all namespaces

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.namespace.get()

if res.describe_namespaces_response is not None:
    # handle response
```


### Response

**[operations.ManagementDescribeNamespacesResponse](../../models/operations/managementdescribenamespacesresponse.md)**


## get_metadata

GetNamespaceMetadata inserts the user metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ManagementGetNamespaceMetadataRequest(
    get_namespace_metadata_request=shared.GetNamespaceMetadataRequest(
        metadata_key='facilis',
        value=shared.GetNamespaceMetadataRequestValue(),
    ),
    metadata_key='perspiciatis',
)

res = s.namespace.get_metadata(req)

if res.get_namespace_metadata_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.ManagementGetNamespaceMetadataRequest](../../models/operations/managementgetnamespacemetadatarequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.ManagementGetNamespaceMetadataResponse](../../models/operations/managementgetnamespacemetadataresponse.md)**


## insert_metadata

InsertNamespaceMetadata inserts the namespace metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ManagementInsertNamespaceMetadataRequest(
    insert_namespace_metadata_request=shared.InsertNamespaceMetadataRequest(
        metadata_key='voluptatem',
        value=shared.InsertNamespaceMetadataRequestValue(),
    ),
    metadata_key='porro',
)

res = s.namespace.insert_metadata(req)

if res.insert_namespace_metadata_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.ManagementInsertNamespaceMetadataRequest](../../models/operations/managementinsertnamespacemetadatarequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.ManagementInsertNamespaceMetadataResponse](../../models/operations/managementinsertnamespacemetadataresponse.md)**


## list

List all namespace

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.namespace.list()

if res.list_namespaces_response is not None:
    # handle response
```


### Response

**[operations.ManagementListNamespacesResponse](../../models/operations/managementlistnamespacesresponse.md)**


## update_metadata

UpdateNamespaceMetadata updates the user metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ManagementUpdateNamespaceMetadataRequest(
    update_namespace_metadata_request=shared.UpdateNamespaceMetadataRequest(
        metadata_key='consequuntur',
        value=shared.UpdateNamespaceMetadataRequestValue(),
    ),
    metadata_key='blanditiis',
)

res = s.namespace.update_metadata(req)

if res.update_namespace_metadata_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.ManagementUpdateNamespaceMetadataRequest](../../models/operations/managementupdatenamespacemetadatarequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.ManagementUpdateNamespaceMetadataResponse](../../models/operations/managementupdatenamespacemetadataresponse.md)**
