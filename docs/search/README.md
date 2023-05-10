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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.create_document(shared.CreateByIDRequest(
    document='quo',
    id='dca42519-04e5-423c-be0b-c7178e4796f2',
    index='deserunt',
    project='molestiae',
), 'accusantium', 'porro', 'eum')

if res.create_by_id_response is not None:
    # handle response
```

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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.create_documents(shared.CreateDocumentRequest(
    documents=[
        'praesentium',
        'consequuntur',
        'deleniti',
    ],
    index='fugit',
    project='fuga',
), 'mollitia', 'incidunt')

if res.create_document_response is not None:
    # handle response
```

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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.delete_documents(shared.DeleteDocumentRequest(
    ids=[
        'explicabo',
        'minima',
        'nisi',
    ],
    index='fugit',
    project='sapiente',
), 'consequuntur', 'ratione')

if res.delete_document_response is not None:
    # handle response
```

## delete_index

Deletes search index

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.delete_index(shared.DeleteIndexRequest(
    name='Kerry Mayert IV',
    project='eveniet',
), 'accusamus', 'veritatis')

if res.delete_index_response is not None:
    # handle response
```

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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.find_documents(shared.SearchIndexRequest(
    collation=shared.Collation(
        case='esse',
    ),
    exclude_fields=[
        'nam',
        'vero',
        'aliquid',
        'quasi',
    ],
    facet='saepe',
    filter='vel',
    include_fields=[
        'molestiae',
        'rerum',
        'occaecati',
    ],
    index='minima',
    page=716244,
    page_size=756779,
    project='sit',
    q='culpa',
    search_fields=[
        'adipisci',
        'cumque',
        'consequuntur',
    ],
    sort='consequatur',
), 'minus', 'quaerat')

if res.search_index_response is not None:
    # handle response
```

## get_documents

Retrieves one or more documents by id. The response is an array of documents in the same order it is requests.
 A null is returned for the documents that are not found.

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.get_documents('sapiente', 'consectetur', [
    'blanditiis',
    'provident',
])

if res.get_document_response is not None:
    # handle response
```

## get_index

Get information about a search index

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.get_index('a', 'nulla')

if res.get_index_response is not None:
    # handle response
```

## list_indexes

List search indexes

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.list_indexes('quas', 'esse', 'quasi', 'a')

if res.list_indexes_response is not None:
    # handle response
```

## query_delete_documents

DeleteByQuery is used to delete documents that match the filter. A filter is required. To delete document by id,
 you can pass the filter as follows ```{"id": "test"}```. Returns a count of number of documents deleted.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.query_delete_documents(shared.DeleteByQueryRequest(
    filter='error',
    index='sint',
    project='pariatur',
), 'possimus', 'quia')

if res.delete_by_query_response is not None:
    # handle response
```

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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.replace_documents(shared.CreateOrReplaceDocumentRequest(
    documents=[
        'asperiores',
        'facere',
        'veritatis',
        'consequuntur',
    ],
    index='quasi',
    project='similique',
), 'culpa', 'aliquid')

if res.create_or_replace_document_response is not None:
    # handle response
```

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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.update_documents(shared.UpdateDocumentRequest(
    documents=[
        'quae',
        'earum',
        'vel',
        'in',
    ],
    index='eius',
    project='libero',
), 'illum', 'soluta')

if res.update_document_response is not None:
    # handle response
```

## update_index

Creates or updates search index

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.search.update_index(shared.CreateOrUpdateIndexRequest(
    name='Mrs. Michele Williamson',
    only_create=False,
    project='ullam',
    schema='nisi',
), 'aut', 'voluptatum')

if res.create_or_update_index_response is not None:
    # handle response
```
