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
    code=758379,
    id='e5e6a95d-8a0d-4446-8e2a-f7a73cf3be45',
    name='Jeannie Leannon MD',
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


res = s.namespace.get_metadata(shared.GetNamespaceMetadataRequest(
    metadata_key='neque',
    value={
        "vel": 'libero',
    },
), 'voluptas')

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


res = s.namespace.insert_metadata(shared.InsertNamespaceMetadataRequest(
    metadata_key='deserunt',
    value={
        "ipsum": 'incidunt',
        "qui": 'cupiditate',
    },
), 'maxime')

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


res = s.namespace.update_metadata(shared.UpdateNamespaceMetadataRequest(
    metadata_key='pariatur',
    value={
        "dicta": 'laborum',
        "totam": 'incidunt',
        "aspernatur": 'dolores',
    },
), 'distinctio')

if res.update_namespace_metadata_response is not None:
    # handle response
```
