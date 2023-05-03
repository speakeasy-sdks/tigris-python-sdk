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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.CreateNamespaceRequest(
    code=286915,
    id='3a1108e0-adcf-44b9-a187-9fce953f73ef',
    name='Darla Rau',
)

res = s.namespace.create(req)

if res.create_namespace_response is not None:
    # handle response
```

## get

Get details for all namespaces

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.namespace.get()

if res.describe_namespaces_response is not None:
    # handle response
```

## get_metadata

GetNamespaceMetadata inserts the user metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ManagementGetNamespaceMetadataRequest(
    get_namespace_metadata_request=shared.GetNamespaceMetadataRequest(
        metadata_key='similique',
        value={
            "vero": 'ducimus',
            "dolore": 'quibusdam',
            "illum": 'sequi',
        },
    ),
    metadata_key='natus',
)

res = s.namespace.get_metadata(req)

if res.get_namespace_metadata_response is not None:
    # handle response
```

## insert_metadata

InsertNamespaceMetadata inserts the namespace metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ManagementInsertNamespaceMetadataRequest(
    insert_namespace_metadata_request=shared.InsertNamespaceMetadataRequest(
        metadata_key='impedit',
        value={
            "voluptatibus": 'exercitationem',
        },
    ),
    metadata_key='nulla',
)

res = s.namespace.insert_metadata(req)

if res.insert_namespace_metadata_response is not None:
    # handle response
```

## list

List all namespace

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.namespace.list()

if res.list_namespaces_response is not None:
    # handle response
```

## update_metadata

UpdateNamespaceMetadata updates the user metadata object

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ManagementUpdateNamespaceMetadataRequest(
    update_namespace_metadata_request=shared.UpdateNamespaceMetadataRequest(
        metadata_key='fugit',
        value={
            "maiores": 'doloribus',
            "iusto": 'eligendi',
            "ducimus": 'alias',
            "officia": 'tempora',
        },
    ),
    metadata_key='ipsam',
)

res = s.namespace.update_metadata(req)

if res.update_namespace_metadata_response is not None:
    # handle response
```
