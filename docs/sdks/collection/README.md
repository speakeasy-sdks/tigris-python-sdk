# Collection
(*collection*)

## Overview

The Collections section provide APIs that can be used to manage collections. A collection can have one or more documents.

### Available Operations

* [create](#create) - Create or update a collection
* [delete_documents](#delete_documents) - Delete Documents
* [describe](#describe) - Describe Collection
* [drop](#drop) - Drop Collection
* [import_documents](#import_documents) - Import Documents
* [insert_documents](#insert_documents) - Insert Documents
* [read_documents](#read_documents) - Read Documents
* [replace_documents](#replace_documents) - Insert or Replace Documents
* [search_documents](#search_documents) - Search Documents.
* [update_documents](#update_documents) - Update Documents.

## create

Creates a new collection or atomically upgrades the collection to the new schema provided in the request.
 Schema changes are applied atomically and immediately without any downtime.
 Tigris Offers two types of collections: <p></p>
    <li> `DOCUMENTS`: Offers rich CRUD APIs.
    <li> `MESSAGES`: Offers event streaming APIs.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisCreateOrUpdateCollectionRequest(
    create_or_update_collection_request=shared.CreateOrUpdateCollectionRequest(
        options=shared.CollectionOptions(),
        schema=shared.CreateOrUpdateCollectionRequestSchema(),
    ),
    collection='Electric pirouette',
    project='Sausages ASCII',
)

res = s.collection.create(req)

if res.create_or_update_collection_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.TigrisCreateOrUpdateCollectionRequest](../../models/operations/tigriscreateorupdatecollectionrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.TigrisCreateOrUpdateCollectionResponse](../../models/operations/tigriscreateorupdatecollectionresponse.md)**


## delete_documents

Delete a range of documents in the collection using the condition provided in the filter.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisDeleteRequest(
    delete_request=shared.DeleteRequest(
        filter=shared.DeleteRequestFilter(),
        options=shared.DeleteRequestOptions(
            collation=shared.Collation(),
            write_options=shared.WriteOptions(),
        ),
    ),
    collection='Convertible consequently female',
    project='Card',
)

res = s.collection.delete_documents(req)

if res.delete_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.TigrisDeleteRequest](../../models/operations/tigrisdeleterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.TigrisDeleteResponse](../../models/operations/tigrisdeleteresponse.md)**


## describe

Returns the information related to the collection. This can be used to retrieve the schema or size of the collection.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisDescribeCollectionRequest(
    describe_collection_request=shared.DescribeCollectionRequest(
        options=shared.CollectionOptions(),
    ),
    collection='morph Pickup',
    project='Home',
)

res = s.collection.describe(req)

if res.describe_collection_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.TigrisDescribeCollectionRequest](../../models/operations/tigrisdescribecollectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.TigrisDescribeCollectionResponse](../../models/operations/tigrisdescribecollectionresponse.md)**


## drop

Drops the collection inside this project. This API deletes all of the
 documents inside this collection and any metadata associated with it.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisDropCollectionRequest(
    drop_collection_request=shared.DropCollectionRequest(
        options=shared.CollectionOptions(),
    ),
    collection='Tricycle Cummings',
    project='reboot Northern',
)

res = s.collection.drop(req)

if res.drop_collection_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.TigrisDropCollectionRequest](../../models/operations/tigrisdropcollectionrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.TigrisDropCollectionResponse](../../models/operations/tigrisdropcollectionresponse.md)**


## import_documents

Imports documents into the collection.

 It automatically:
  * Detects the schema of the documents in the batch
  * Evolves the schema as soon as it's backward compatible
  * Creates collection with inferred schema (if requested)

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisImportRequest(
    import_request=shared.ImportRequest(
        autogenerated=[
            'voyage',
        ],
        documents=[
            shared.ImportRequestDocuments(),
        ],
        options=shared.ImportRequestOptions(
            write_options=shared.WriteOptions(),
        ),
        primary_key=[
            'calmly',
        ],
    ),
    collection='Sedan Peru',
    project='wherever Designer',
)

res = s.collection.import_documents(req)

if res.import_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.TigrisImportRequest](../../models/operations/tigrisimportrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.TigrisImportResponse](../../models/operations/tigrisimportresponse.md)**


## insert_documents

Inserts new documents in the collection and returns an AlreadyExists error if any of the documents
 in the request already exists. Insert provides idempotency by returning an error if the document
 already exists. To replace documents, use REPLACE API instead of INSERT.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisInsertRequest(
    insert_request=shared.InsertRequest(
        documents=[
            shared.InsertRequestDocuments(),
        ],
        options=shared.InsertRequestOptions(
            write_options=shared.WriteOptions(),
        ),
    ),
    collection='magnetic Hong National',
    project='Lemke',
)

res = s.collection.insert_documents(req)

if res.insert_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.TigrisInsertRequest](../../models/operations/tigrisinsertrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.TigrisInsertResponse](../../models/operations/tigrisinsertresponse.md)**


## read_documents

Reads a range of documents from the collection, or messages from a collection in case of event streaming. Tigris does not require you to
 index any fields and automatically index all the fields which means you can filter by any field in the document.
 An empty filter will trigger reading all the documents inside this collection. The API supports pagination that
 can be used by passing `Limit/Skip` parameters. The `skip` parameter skips the number of documents from the start and
 the `limit` parameter is used to specify the number of documents to read. You can find more detailed documentation
 of the Read API <a href="https://docs.tigrisdata.com/overview/query" title="here">here</a>.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisReadRequest(
    read_request=shared.ReadRequest(
        fields_=shared.ReadRequestFields(),
        filter=shared.ReadRequestFilter(),
        options=shared.ReadRequestOptions(
            collation=shared.Collation(),
        ),
    ),
    collection='West farad',
    project='Books yellow',
)

res = s.collection.read_documents(req)

if res.streaming_read_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.TigrisReadRequest](../../models/operations/tigrisreadrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.TigrisReadResponse](../../models/operations/tigrisreadresponse.md)**


## replace_documents

Inserts the documents or replaces the existing documents in the collections.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisReplaceRequest(
    replace_request=shared.ReplaceRequest(
        documents=[
            shared.ReplaceRequestDocuments(),
        ],
        options=shared.ReplaceRequestOptions(
            write_options=shared.WriteOptions(),
        ),
    ),
    collection='female West Southeast',
    project='Total phew',
)

res = s.collection.replace_documents(req)

if res.replace_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.TigrisReplaceRequest](../../models/operations/tigrisreplacerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.TigrisReplaceResponse](../../models/operations/tigrisreplaceresponse.md)**


## search_documents

Searches a collection for the documents matching the query, or messages in case of event streaming. A search can be
 a term search or a phrase search. Search API allows filtering the result set using filters as documented <a href="https://docs.tigrisdata.com/overview/query#specification-1" title="here">here</a>.
 You can also perform a faceted search by passing the fields in the facet parameter.
 You can find more detailed documentation of the Search API with multiple examples <a href="https://docs.tigrisdata.com/overview/search" title="here">here</a>.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisSearchRequest(
    search_request=shared.SearchRequest(
        collation=shared.Collation(),
        exclude_fields=[
            'California',
        ],
        facet=shared.SearchRequestFacet(),
        fields_=shared.SearchRequestFields(),
        filter=shared.SearchRequestFilter(),
        include_fields=[
            'Engineer',
        ],
        search_fields=[
            'teal',
        ],
        sort=shared.SearchRequestSort(),
    ),
    collection='blue Intranet Germanium',
    project='Books degree Cambridgeshire',
)

res = s.collection.search_documents(req)

if res.streaming_search_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.TigrisSearchRequest](../../models/operations/tigrissearchrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.TigrisSearchResponse](../../models/operations/tigrissearchresponse.md)**


## update_documents

Update a range of documents in the collection using the condition provided in the filter.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisUpdateRequest(
    update_request=shared.UpdateRequest(
        fields_=shared.UpdateRequestFields(),
        filter=shared.UpdateRequestFilter(),
        options=shared.UpdateRequestOptions(
            collation=shared.Collation(),
            write_options=shared.WriteOptions(),
        ),
    ),
    collection='Northwest',
    project='West',
)

res = s.collection.update_documents(req)

if res.update_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.TigrisUpdateRequest](../../models/operations/tigrisupdaterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.TigrisUpdateResponse](../../models/operations/tigrisupdateresponse.md)**

