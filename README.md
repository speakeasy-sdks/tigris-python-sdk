# tigris-core

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/tigris-python-sdk.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.TigrisDeleteAppKeyRequest(
    delete_app_key_request=shared.DeleteAppKeyRequest(
        id="corrupti",
    ),
    project="provident",
)
    
res = s.app_key.delete(req)

if res.delete_app_key_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### app_key

* `delete` - Deletes the app key
* `list` - List all the app keys
* `rotate` - Rotates the app key secret
* `tigris_create_app_key` - Creates the app key
* `update` - Updates the description of the app key

### auth

* `get` - Access Token

### cache

* `create` - Creates the cache
* `delete` - Deletes the cache
* `delete_keys` - Deletes an entry from cache
* `get_key` - Reads an entry from cache
* `get_set_key` - Sets an entry in the cache and returns the previous value if exists
* `list` - Lists all the caches for the given project
* `list_keys` - Lists all the key for this cache
* `set_key` - Sets an entry in the cache

### channel

* `get` - Get the details about a channel
* `get_messages` - Get all messages for a channel
* `list` - Get all channels for your application project
* `list_subscriptions` - Get the subscriptions details about a channel
* `push_messages` - push messages to a single channel
* `realtime_presence` - Presence about the channel

### collection

* `create` - Create or update a collection
* `delete_documents` - Delete Documents
* `describe` - Describe Collection
* `drop` - Drop Collection
* `import_documents` - Import Documents
* `insert_documents` - Insert Documents
* `read_documents` - Read Documents
* `replace_documents` - Insert or Replace Documents
* `search_documents` - Search Documents.
* `update_documents` - Update Documents.

### database

* `begin_transaction` - Begin a transaction
* `commit_transaction` - Commit a Transaction
* `create_branch` - Create a database branch
* `delete_branch` - Delete a database branch
* `describe` - Describe database
* `list_collections` - List Collections
* `rollback_transaction` - Rollback a transaction
* `tigris_list_branches` - List database branches

### namespace

* `create` - Creates a Namespace
* `get` - Describe the details of all namespaces
* `get_metadata` - Reads the Namespace Metadata
* `insert_metadata` - Inserts Namespace Metadata
* `list` - Lists all Namespaces
* `update_metadata` - Updates Namespace Metadata

### project

* `create` - Create Project
* `delete_project` - Delete Project and all resources under project
* `list` - List Projects

### search

* `create_document` - Create a single document
* `create_documents` - Create multiple documents
* `delete_documents` - Delete documents by ids
* `delete_index` - Deletes search index
* `find_documents` - Search Documents.
* `get_documents` - Get a single or multiple documents
* `get_index` - Get information about a search index
* `list_indexes` - List search indexes
* `query_delete_documents` - Delete documents by query
* `replace_documents` - Create or replace documents in an index
* `update_documents` - Update documents in an index
* `update_index` - Creates or updates search index

### system

* `get_health` - Health Check
* `get_server_info` - Information about the server
* `observability_quota_usage` - Queries current namespace quota usage
* `query_quota_limits` - Queries current namespace quota limits
* `query_time_series_metrics` - Queries time series metrics

### user

* `get_metadata` - Reads the User Metadata
* `insert_metadata` - Inserts User Metadata
* `update_metadata` - Updates User Metadata
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
