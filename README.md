<div align="center">
    <img src="https://user-images.githubusercontent.com/6267663/235892529-fc4d91d3-0e38-46c1-bbe4-b237ee973e62.svg" width="350px">
    <h1>Tigris Core Python SDK</h1>
   <p>Serverless NOSQL Database and Search Platform</p>
   <a href="https://www.tigrisdata.com/docs/references/api/"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/tigris-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/tigris-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/speakeasy-sdks/tigris-python-sdk/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/tigris-python-sdk?sort=semver&style=for-the-badge" /></a>
  <a href="https://www.tigrisdata.com/discord/"><img src="https://img.shields.io/static/v1?label=Discord&message=Join&color=7289da&style=for-the-badge" /></a>
</div>

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


req = operations.CacheCreateCacheRequest(
    create_cache_request=shared.CreateCacheRequest(
        options=shared.CreateCacheOptions(
            ttl_ms=548814,
        ),
    ),
    name='Kelvin Sporer',
    project='corrupti',
)

res = s.cache.create(req)

if res.create_cache_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [app_key](docs/appkey/README.md)

* [delete](docs/appkey/README.md#delete) - Deletes the app key
* [list](docs/appkey/README.md#list) - List all the app keys
* [rotate](docs/appkey/README.md#rotate) - Rotates the app key secret
* [tigris_create_app_key](docs/appkey/README.md#tigris_create_app_key) - Creates the app key
* [update](docs/appkey/README.md#update) - Updates the description of the app key

### [auth](docs/auth/README.md)

* [get](docs/auth/README.md#get) - Access Token

### [cache](docs/cache/README.md)

* [create](docs/cache/README.md#create) - Creates the cache
* [delete](docs/cache/README.md#delete) - Deletes the cache
* [delete_keys](docs/cache/README.md#delete_keys) - Deletes an entry from cache
* [get_key](docs/cache/README.md#get_key) - Reads an entry from cache
* [get_set_key](docs/cache/README.md#get_set_key) - Sets an entry in the cache and returns the previous value if exists
* [list](docs/cache/README.md#list) - Lists all the caches for the given project
* [list_keys](docs/cache/README.md#list_keys) - Lists all the key for this cache
* [set_key](docs/cache/README.md#set_key) - Sets an entry in the cache

### [channel](docs/channel/README.md)

* [get](docs/channel/README.md#get) - Get the details about a channel
* [get_messages](docs/channel/README.md#get_messages) - Get all messages for a channel
* [list](docs/channel/README.md#list) - Get all channels for your application project
* [list_subscriptions](docs/channel/README.md#list_subscriptions) - Get the subscriptions details about a channel
* [push_messages](docs/channel/README.md#push_messages) - push messages to a single channel
* [realtime_presence](docs/channel/README.md#realtime_presence) - Presence about the channel

### [collection](docs/collection/README.md)

* [create](docs/collection/README.md#create) - Create or update a collection
* [delete_documents](docs/collection/README.md#delete_documents) - Delete Documents
* [describe](docs/collection/README.md#describe) - Describe Collection
* [drop](docs/collection/README.md#drop) - Drop Collection
* [import_documents](docs/collection/README.md#import_documents) - Import Documents
* [insert_documents](docs/collection/README.md#insert_documents) - Insert Documents
* [read_documents](docs/collection/README.md#read_documents) - Read Documents
* [replace_documents](docs/collection/README.md#replace_documents) - Insert or Replace Documents
* [search_documents](docs/collection/README.md#search_documents) - Search Documents.
* [update_documents](docs/collection/README.md#update_documents) - Update Documents.

### [database](docs/database/README.md)

* [begin_transaction](docs/database/README.md#begin_transaction) - Begin a transaction
* [commit_transaction](docs/database/README.md#commit_transaction) - Commit a Transaction
* [create_branch](docs/database/README.md#create_branch) - Create a database branch
* [delete_branch](docs/database/README.md#delete_branch) - Delete a database branch
* [describe](docs/database/README.md#describe) - Describe database
* [list_collections](docs/database/README.md#list_collections) - List Collections
* [rollback_transaction](docs/database/README.md#rollback_transaction) - Rollback a transaction
* [tigris_list_branches](docs/database/README.md#tigris_list_branches) - List database branches

### [namespace](docs/namespace/README.md)

* [create](docs/namespace/README.md#create) - Creates a Namespace
* [get](docs/namespace/README.md#get) - Describe the details of all namespaces
* [get_metadata](docs/namespace/README.md#get_metadata) - Reads the Namespace Metadata
* [insert_metadata](docs/namespace/README.md#insert_metadata) - Inserts Namespace Metadata
* [list](docs/namespace/README.md#list) - Lists all Namespaces
* [update_metadata](docs/namespace/README.md#update_metadata) - Updates Namespace Metadata

### [project](docs/project/README.md)

* [create](docs/project/README.md#create) - Create Project
* [delete_project](docs/project/README.md#delete_project) - Delete Project and all resources under project
* [list](docs/project/README.md#list) - List Projects

### [search](docs/search/README.md)

* [create_document](docs/search/README.md#create_document) - Create a single document
* [create_documents](docs/search/README.md#create_documents) - Create multiple documents
* [delete_documents](docs/search/README.md#delete_documents) - Delete documents by ids
* [delete_index](docs/search/README.md#delete_index) - Deletes search index
* [find_documents](docs/search/README.md#find_documents) - Search Documents.
* [get_documents](docs/search/README.md#get_documents) - Get a single or multiple documents
* [get_index](docs/search/README.md#get_index) - Get information about a search index
* [list_indexes](docs/search/README.md#list_indexes) - List search indexes
* [query_delete_documents](docs/search/README.md#query_delete_documents) - Delete documents by query
* [replace_documents](docs/search/README.md#replace_documents) - Create or replace documents in an index
* [update_documents](docs/search/README.md#update_documents) - Update documents in an index
* [update_index](docs/search/README.md#update_index) - Creates or updates search index

### [system](docs/system/README.md)

* [get_health](docs/system/README.md#get_health) - Health Check
* [get_server_info](docs/system/README.md#get_server_info) - Information about the server
* [observability_quota_usage](docs/system/README.md#observability_quota_usage) - Queries current namespace quota usage
* [query_quota_limits](docs/system/README.md#query_quota_limits) - Queries current namespace quota limits
* [query_time_series_metrics](docs/system/README.md#query_time_series_metrics) - Queries time series metrics

### [user](docs/user/README.md)

* [get_metadata](docs/user/README.md#get_metadata) - Reads the User Metadata
* [insert_metadata](docs/user/README.md#insert_metadata) - Inserts User Metadata
* [update_metadata](docs/user/README.md#update_metadata) - Updates User Metadata
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
