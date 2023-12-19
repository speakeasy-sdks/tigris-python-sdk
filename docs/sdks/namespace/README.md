# Namespace
(*namespace*)

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
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.CreateNamespaceRequest()

res = s.namespace.create(req)

if res.create_namespace_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.CreateNamespaceRequest](../../models/shared/createnamespacerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateNamespaceResponse](../../models/operations/createnamespaceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get details for all namespaces

### Example Usage

```python
import tigris

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.namespace.get()

if res.describe_namespaces_response is not None:
    # handle response
    pass
```


### Response

**[operations.ManagementDescribeNamespacesResponse](../../models/operations/managementdescribenamespacesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metadata

GetNamespaceMetadata inserts the user metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.ManagementGetNamespaceMetadataRequest(
    get_namespace_metadata_request=shared.GetNamespaceMetadataRequest(
        value=shared.Value(),
    ),
    metadata_key='string',
)

res = s.namespace.get_metadata(req)

if res.get_namespace_metadata_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.ManagementGetNamespaceMetadataRequest](../../models/operations/managementgetnamespacemetadatarequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.ManagementGetNamespaceMetadataResponse](../../models/operations/managementgetnamespacemetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## insert_metadata

InsertNamespaceMetadata inserts the namespace metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.ManagementInsertNamespaceMetadataRequest(
    insert_namespace_metadata_request=shared.InsertNamespaceMetadataRequest(
        value=shared.InsertNamespaceMetadataRequestValue(),
    ),
    metadata_key='string',
)

res = s.namespace.insert_metadata(req)

if res.insert_namespace_metadata_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.ManagementInsertNamespaceMetadataRequest](../../models/operations/managementinsertnamespacemetadatarequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.ManagementInsertNamespaceMetadataResponse](../../models/operations/managementinsertnamespacemetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list

List all namespace

### Example Usage

```python
import tigris

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.namespace.list()

if res.list_namespaces_response is not None:
    # handle response
    pass
```


### Response

**[operations.ManagementListNamespacesResponse](../../models/operations/managementlistnamespacesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_metadata

UpdateNamespaceMetadata updates the user metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.ManagementUpdateNamespaceMetadataRequest(
    update_namespace_metadata_request=shared.UpdateNamespaceMetadataRequest(
        value=shared.UpdateNamespaceMetadataRequestValue(),
    ),
    metadata_key='string',
)

res = s.namespace.update_metadata(req)

if res.update_namespace_metadata_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.ManagementUpdateNamespaceMetadataRequest](../../models/operations/managementupdatenamespacemetadatarequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.ManagementUpdateNamespaceMetadataResponse](../../models/operations/managementupdatenamespacemetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
