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

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/tigris-python-sdk.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.CacheCreateCacheRequest(
    create_cache_request=shared.CreateCacheRequest(),
    name='string',
    project='string',
)

res = s.cache.create(req)

if res.create_cache_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [auth](docs/sdks/auth/README.md)

* [get](docs/sdks/auth/README.md#get) - Access Token

### [system](docs/sdks/system/README.md)

* [get_health](docs/sdks/system/README.md#get_health) - Health Check
* [get_server_info](docs/sdks/system/README.md#get_server_info) - Information about the server
* [observability_quota_usage](docs/sdks/system/README.md#observability_quota_usage) - Queries current namespace quota usage
* [query_quota_limits](docs/sdks/system/README.md#query_quota_limits) - Queries current namespace quota limits
* [query_time_series_metrics](docs/sdks/system/README.md#query_time_series_metrics) - Queries time series metrics

### [namespace](docs/sdks/namespace/README.md)

* [create](docs/sdks/namespace/README.md#create) - Creates a Namespace
* [get](docs/sdks/namespace/README.md#get) - Describe the details of all namespaces
* [get_metadata](docs/sdks/namespace/README.md#get_metadata) - Reads the Namespace Metadata
* [insert_metadata](docs/sdks/namespace/README.md#insert_metadata) - Inserts Namespace Metadata
* [list](docs/sdks/namespace/README.md#list) - Lists all Namespaces
* [update_metadata](docs/sdks/namespace/README.md#update_metadata) - Updates Namespace Metadata

### [user](docs/sdks/user/README.md)

* [get_metadata](docs/sdks/user/README.md#get_metadata) - Reads the User Metadata
* [insert_metadata](docs/sdks/user/README.md#insert_metadata) - Inserts User Metadata
* [update_metadata](docs/sdks/user/README.md#update_metadata) - Updates User Metadata

### [project](docs/sdks/project/README.md)

* [create](docs/sdks/project/README.md#create) - Create Project
* [delete_project](docs/sdks/project/README.md#delete_project) - Delete Project and all resources under project
* [list](docs/sdks/project/README.md#list) - List Projects

### [app_key](docs/sdks/appkey/README.md)

* [delete](docs/sdks/appkey/README.md#delete) - Deletes the app key
* [list](docs/sdks/appkey/README.md#list) - List all the app keys
* [rotate](docs/sdks/appkey/README.md#rotate) - Rotates the app key secret
* [tigris_create_app_key](docs/sdks/appkey/README.md#tigris_create_app_key) - Creates the app key
* [update](docs/sdks/appkey/README.md#update) - Updates the description of the app key

### [cache](docs/sdks/cache/README.md)

* [create](docs/sdks/cache/README.md#create) - Creates the cache
* [delete](docs/sdks/cache/README.md#delete) - Deletes the cache
* [delete_keys](docs/sdks/cache/README.md#delete_keys) - Deletes an entry from cache
* [get_key](docs/sdks/cache/README.md#get_key) - Reads an entry from cache
* [get_set_key](docs/sdks/cache/README.md#get_set_key) - Sets an entry in the cache and returns the previous value if exists
* [list](docs/sdks/cache/README.md#list) - Lists all the caches for the given project
* [list_keys](docs/sdks/cache/README.md#list_keys) - Lists all the key for this cache
* [set_key](docs/sdks/cache/README.md#set_key) - Sets an entry in the cache

### [database](docs/sdks/database/README.md)

* [begin_transaction](docs/sdks/database/README.md#begin_transaction) - Begin a transaction
* [commit_transaction](docs/sdks/database/README.md#commit_transaction) - Commit a Transaction
* [create_branch](docs/sdks/database/README.md#create_branch) - Create a database branch
* [delete_branch](docs/sdks/database/README.md#delete_branch) - Delete a database branch
* [describe](docs/sdks/database/README.md#describe) - Describe database
* [list_collections](docs/sdks/database/README.md#list_collections) - List Collections
* [rollback_transaction](docs/sdks/database/README.md#rollback_transaction) - Rollback a transaction
* [tigris_list_branches](docs/sdks/database/README.md#tigris_list_branches) - List database branches

### [collection](docs/sdks/collection/README.md)

* [create](docs/sdks/collection/README.md#create) - Create or update a collection
* [delete_documents](docs/sdks/collection/README.md#delete_documents) - Delete Documents
* [describe](docs/sdks/collection/README.md#describe) - Describe Collection
* [drop](docs/sdks/collection/README.md#drop) - Drop Collection
* [import_documents](docs/sdks/collection/README.md#import_documents) - Import Documents
* [insert_documents](docs/sdks/collection/README.md#insert_documents) - Insert Documents
* [read_documents](docs/sdks/collection/README.md#read_documents) - Read Documents
* [replace_documents](docs/sdks/collection/README.md#replace_documents) - Insert or Replace Documents
* [search_documents](docs/sdks/collection/README.md#search_documents) - Search Documents.
* [update_documents](docs/sdks/collection/README.md#update_documents) - Update Documents.

### [channel](docs/sdks/channel/README.md)

* [get](docs/sdks/channel/README.md#get) - Get the details about a channel
* [get_messages](docs/sdks/channel/README.md#get_messages) - Get all messages for a channel
* [list](docs/sdks/channel/README.md#list) - Get all channels for your application project
* [list_subscriptions](docs/sdks/channel/README.md#list_subscriptions) - Get the subscriptions details about a channel
* [push_messages](docs/sdks/channel/README.md#push_messages) - push messages to a single channel
* [realtime_presence](docs/sdks/channel/README.md#realtime_presence) - Presence about the channel

### [search](docs/sdks/search/README.md)

* [create_document](docs/sdks/search/README.md#create_document) - Create a single document
* [create_documents](docs/sdks/search/README.md#create_documents) - Create multiple documents
* [delete_documents](docs/sdks/search/README.md#delete_documents) - Delete documents by ids
* [delete_index](docs/sdks/search/README.md#delete_index) - Deletes search index
* [find_documents](docs/sdks/search/README.md#find_documents) - Search Documents.
* [get_documents](docs/sdks/search/README.md#get_documents) - Get a single or multiple documents
* [get_index](docs/sdks/search/README.md#get_index) - Get information about a search index
* [list_indexes](docs/sdks/search/README.md#list_indexes) - List search indexes
* [query_delete_documents](docs/sdks/search/README.md#query_delete_documents) - Delete documents by query
* [replace_documents](docs/sdks/search/README.md#replace_documents) - Create or replace documents in an index
* [update_documents](docs/sdks/search/README.md#update_documents) - Update documents in an index
* [update_index](docs/sdks/search/README.md#update_index) - Creates or updates search index
<!-- End Available Resources and Operations [operations] -->





<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

```python
import tigris
from tigris.models import errors

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = None
try:
    res = s.auth.get()
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.get_access_token_response is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.preview.tigrisdata.cloud` | None |
| 1 | `http://localhost:8081` | None |

#### Example

```python
import tigris

s = tigris.Tigris(
    server_idx=1,
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.get()

if res.get_access_token_response is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import tigris

s = tigris.Tigris(
    server_url="https://api.preview.tigrisdata.cloud",
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.get()

if res.get_access_token_response is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import tigris
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = tigris.Tigris(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import tigris

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.get()

if res.get_access_token_response is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
