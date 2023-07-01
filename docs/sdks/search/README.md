# search

## Overview

The search section provides you APIs that can be used to implement powerful apps with search experiences. You can manage storing documents on your own or you can simply integrate it with your database.

### Available Operations

* [create_document](#create_document) - Create a single document
* [create_documents](#create_documents) - Create multiple documents
* [delete_documents](#delete_documents) - Delete documents by ids
* [delete_index](#delete_index) - Deletes search index
* [find_documents](#find_documents) - Search Documents.
* [get_documents](#get_documents) - Get a single or multiple documents
* [get_index](#get_index) - Get information about a search index
* [list_indexes](#list_indexes) - List search indexes
* [query_delete_documents](#query_delete_documents) - Delete documents by query
* [replace_documents](#replace_documents) - Create or replace documents in an index
* [update_documents](#update_documents) - Update documents in an index
* [update_index](#update_index) - Creates or updates search index

## create_document

CreateById is used for indexing a single document. The API expects a single document. An "id" is optional
 and the server can automatically generate it for you in case it is missing. In cases an id is provided in
 the document and the document already exists then that document will not be indexed and an error is returned
 with HTTP status code 409.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchCreateByIDRequest(
    create_by_id_request=shared.CreateByIDRequest(
        document='occaecati',
        id='b3fe49a8-d9cb-4f48-a333-23f9b77f3a41',
        index='ipsa',
        project='ipsa',
    ),
    id='674ebf69-280d-41ba-b7a8-9ebf737ae420',
    index='amet',
    project='optio',
)

res = s.search.create_document(req)

if res.create_by_id_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.SearchCreateByIDRequest](../../models/operations/searchcreatebyidrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.SearchCreateByIDResponse](../../models/operations/searchcreatebyidresponse.md)**


## create_documents

Create is used for indexing a single or multiple documents. The API expects an array of documents.
 Each document is a JSON object. An "id" is optional and the server can automatically generate it for you in
 case it is missing. In cases when an id is provided in the document and the document already exists then that
 document will not be indexed and in the response there will be an error corresponding to that document id other
 documents will succeed. Returns an array of status indicating the status of each document.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchCreateRequest(
    create_document_request=shared.CreateDocumentRequest(
        documents=[
            'ad',
            'saepe',
            'suscipit',
            'deserunt',
        ],
        index='provident',
        project='minima',
    ),
    index='repellendus',
    project='totam',
)

res = s.search.create_documents(req)

if res.create_document_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.SearchCreateRequest](../../models/operations/searchcreaterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.SearchCreateResponse](../../models/operations/searchcreateresponse.md)**


## delete_documents

Delete one or more documents by id. Returns an array of status indicating the status of each document. Each status
 has an error field that is set to null in case document is deleted successfully otherwise it will non null with
 an error code and message.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchDeleteRequest(
    delete_document_request=shared.DeleteDocumentRequest(
        ids=[
            'alias',
            'at',
            'quaerat',
        ],
        index='tempora',
        project='vel',
    ),
    index='quod',
    project='officiis',
)

res = s.search.delete_documents(req)

if res.delete_document_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.SearchDeleteRequest](../../models/operations/searchdeleterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.SearchDeleteResponse](../../models/operations/searchdeleteresponse.md)**


## delete_index

Deletes search index

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchDeleteIndexRequest(
    delete_index_request=shared.DeleteIndexRequest(
        name='Jan Wilderman',
        project='iusto',
    ),
    name='Rosalie White',
    project='accusamus',
)

res = s.search.delete_index(req)

if res.delete_index_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.SearchDeleteIndexRequest](../../models/operations/searchdeleteindexrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.SearchDeleteIndexResponse](../../models/operations/searchdeleteindexresponse.md)**


## find_documents

Searches an index for the documents matching the query. A search can be a term search or a phrase search.
 Search API allows filtering the result set using filters as documented
 <a href="https://docs.tigrisdata.com/overview/query#specification-1" title="here">here</a>. You can also perform
 a faceted search by passing the fields in the facet parameter. You can find more detailed documentation of the
 Search API with multiple examples <a href="https://docs.tigrisdata.com/overview/search" title="here">here</a>.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchSearchRequest(
    search_index_request=shared.SearchIndexRequest(
        collation=shared.Collation(
            case='numquam',
        ),
        exclude_fields=[
            'dolorem',
            'sapiente',
        ],
        facet='totam',
        filter='nihil',
        include_fields=[
            'expedita',
        ],
        index='neque',
        page=153694,
        page_size=424685,
        project='libero',
        q='voluptas',
        search_fields=[
            'quam',
            'ipsum',
            'incidunt',
        ],
        sort='qui',
    ),
    index='cupiditate',
    project='maxime',
)

res = s.search.find_documents(req)

if res.search_index_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.SearchSearchRequest](../../models/operations/searchsearchrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.SearchSearchResponse](../../models/operations/searchsearchresponse.md)**


## get_documents

Retrieves one or more documents by id. The response is an array of documents in the same order it is requests.
 A null is returned for the documents that are not found.

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchGetRequest(
    ids=[
        'soluta',
        'dicta',
        'laborum',
        'totam',
    ],
    index='incidunt',
    project='aspernatur',
)

res = s.search.get_documents(req)

if res.get_document_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.SearchGetRequest](../../models/operations/searchgetrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.SearchGetResponse](../../models/operations/searchgetresponse.md)**


## get_index

Get information about a search index

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchGetIndexRequest(
    name='Verna Purdy',
    project='molestias',
)

res = s.search.get_index(req)

if res.get_index_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.SearchGetIndexRequest](../../models/operations/searchgetindexrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.SearchGetIndexResponse](../../models/operations/searchgetindexresponse.md)**


## list_indexes

List search indexes

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchListIndexesRequest(
    filter_branch='temporibus',
    filter_collection='qui',
    filter_type='neque',
    project='fugit',
)

res = s.search.list_indexes(req)

if res.list_indexes_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.SearchListIndexesRequest](../../models/operations/searchlistindexesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.SearchListIndexesResponse](../../models/operations/searchlistindexesresponse.md)**


## query_delete_documents

DeleteByQuery is used to delete documents that match the filter. A filter is required. To delete document by id,
 you can pass the filter as follows ```{"id": "test"}```. Returns a count of number of documents deleted.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchDeleteByQueryRequest(
    delete_by_query_request=shared.DeleteByQueryRequest(
        filter='magni',
        index='odio',
        project='sunt',
    ),
    index='ullam',
    project='nam',
)

res = s.search.query_delete_documents(req)

if res.delete_by_query_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.SearchDeleteByQueryRequest](../../models/operations/searchdeletebyqueryrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.SearchDeleteByQueryResponse](../../models/operations/searchdeletebyqueryresponse.md)**


## replace_documents

Creates or replaces one or more documents. Each document is a JSON object. A document is replaced
 if it already exists. An "id" is generated automatically in case it is missing in the document. The
 document is created if "id" doesn't exists otherwise it is replaced. Returns an array of status indicating
 the status of each document.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchCreateOrReplaceRequest(
    create_or_replace_document_request=shared.CreateOrReplaceDocumentRequest(
        documents=[
            'voluptatem',
            'cumque',
            'soluta',
            'nobis',
        ],
        index='et',
        project='saepe',
    ),
    index='ipsum',
    project='veritatis',
)

res = s.search.replace_documents(req)

if res.create_or_replace_document_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.SearchCreateOrReplaceRequest](../../models/operations/searchcreateorreplacerequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.SearchCreateOrReplaceResponse](../../models/operations/searchcreateorreplaceresponse.md)**


## update_documents

Updates one or more documents by "id". Each document is required to have the
 "id" field in it. Returns an array of status indicating the status of each document. Each status
 has an error field that is set to null in case document is updated successfully otherwise the error
 field is set with a code and message.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchUpdateRequest(
    update_document_request=shared.UpdateDocumentRequest(
        documents=[
            'quos',
            'tempore',
            'cupiditate',
        ],
        index='aperiam',
        project='delectus',
    ),
    index='dolorem',
    project='dolore',
)

res = s.search.update_documents(req)

if res.update_document_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.SearchUpdateRequest](../../models/operations/searchupdaterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.SearchUpdateResponse](../../models/operations/searchupdateresponse.md)**


## update_index

Creates or updates search index

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchCreateOrUpdateIndexRequest(
    create_or_update_index_request=shared.CreateOrUpdateIndexRequest(
        name='Mr. Josephine Pagac V',
        only_create=False,
        project='itaque',
        schema='consequatur',
    ),
    name='Marcos Schaden',
    project='facilis',
)

res = s.search.update_index(req)

if res.create_or_update_index_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.SearchCreateOrUpdateIndexRequest](../../models/operations/searchcreateorupdateindexrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.SearchCreateOrUpdateIndexResponse](../../models/operations/searchcreateorupdateindexresponse.md)**
