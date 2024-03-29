# collection

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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TigrisCreateOrUpdateCollectionRequest(
    create_or_update_collection_request=shared.CreateOrUpdateCollectionRequest(
        branch='eius',
        only_create=False,
        options={
            "deleniti": 'facilis',
            "in": 'architecto',
            "architecto": 'repudiandae',
            "ullam": 'expedita',
        },
        schema={
            "repellat": 'quibusdam',
            "sed": 'saepe',
        },
    ),
    collection='pariatur',
    project='accusantium',
)

res = s.collection.create(req)

if res.create_or_update_collection_response is not None:
    # handle response
```

## delete_documents

Delete a range of documents in the collection using the condition provided in the filter.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TigrisDeleteRequest(
    delete_request=shared.DeleteRequest(
        branch='consequuntur',
        filter={
            "natus": 'magni',
            "sunt": 'quo',
            "illum": 'pariatur',
        },
        options=shared.DeleteRequestOptions(
            collation=shared.Collation(
                case='maxime',
            ),
            limit=411397,
            write_options={
                "odit": 'ea',
                "accusantium": 'ab',
                "maiores": 'quidem',
            },
        ),
    ),
    collection='ipsam',
    project='voluptate',
)

res = s.collection.delete_documents(req)

if res.delete_response is not None:
    # handle response
```

## describe

Returns the information related to the collection. This can be used to retrieve the schema or size of the collection.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TigrisDescribeCollectionRequest(
    describe_collection_request=shared.DescribeCollectionRequest(
        branch='autem',
        collection='nam',
        options={
            "pariatur": 'nemo',
        },
        project='voluptatibus',
        schema_format='perferendis',
    ),
    collection='fugiat',
    project='amet',
)

res = s.collection.describe(req)

if res.describe_collection_response is not None:
    # handle response
```

## drop

Drops the collection inside this project. This API deletes all of the
 documents inside this collection and any metadata associated with it.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TigrisDropCollectionRequest(
    drop_collection_request=shared.DropCollectionRequest(
        branch='aut',
        options={
            "corporis": 'hic',
            "libero": 'nobis',
            "dolores": 'quis',
            "totam": 'dignissimos',
        },
    ),
    collection='eaque',
    project='quis',
)

res = s.collection.drop(req)

if res.drop_collection_response is not None:
    # handle response
```

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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TigrisImportRequest(
    import_request=shared.ImportRequest(
        autogenerated=[
            'eos',
        ],
        branch='perferendis',
        create_collection=False,
        documents=[
            {
                "quam": 'dolor',
                "vero": 'nostrum',
                "hic": 'recusandae',
                "omnis": 'facilis',
            },
        ],
        options=shared.ImportRequestOptions(
            write_options={
                "voluptatem": 'porro',
                "consequuntur": 'blanditiis',
                "error": 'eaque',
            },
        ),
        primary_key=[
            'rerum',
            'adipisci',
            'asperiores',
        ],
    ),
    collection='earum',
    project='modi',
)

res = s.collection.import_documents(req)

if res.import_response is not None:
    # handle response
```

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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TigrisInsertRequest(
    insert_request=shared.InsertRequest(
        branch='iste',
        documents=[
            {
                "pariatur": 'provident',
                "nobis": 'libero',
                "delectus": 'quaerat',
            },
            {
                "aliquid": 'dolorem',
                "dolorem": 'dolor',
                "qui": 'ipsum',
            },
            {
                "excepturi": 'cum',
                "voluptate": 'dignissimos',
                "reiciendis": 'amet',
                "dolorum": 'numquam',
            },
        ],
        options=shared.InsertRequestOptions(
            write_options={
                "ipsa": 'ipsa',
            },
        ),
    ),
    collection='iure',
    project='odio',
)

res = s.collection.insert_documents(req)

if res.insert_response is not None:
    # handle response
```

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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TigrisReadRequest(
    read_request=shared.ReadRequest(
        branch='quaerat',
        fields_={
            "quidem": 'voluptatibus',
            "voluptas": 'natus',
            "eos": 'atque',
            "sit": 'fugiat',
        },
        filter={
            "soluta": 'dolorum',
        },
        options=shared.ReadRequestOptions(
            collation=shared.Collation(
                case='iusto',
            ),
            limit=453697,
            offset='dolorum',
            skip=536579,
        ),
        sort='omnis',
    ),
    collection='necessitatibus',
    project='distinctio',
)

res = s.collection.read_documents(req)

if res.streaming_read_response is not None:
    # handle response
```

## replace_documents

Inserts the documents or replaces the existing documents in the collections.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TigrisReplaceRequest(
    replace_request=shared.ReplaceRequest(
        branch='asperiores',
        documents=[
            {
                "voluptate": 'id',
            },
            {
                "eius": 'aspernatur',
                "perferendis": 'amet',
                "optio": 'accusamus',
                "ad": 'saepe',
            },
        ],
        options=shared.ReplaceRequestOptions(
            write_options={
                "deserunt": 'provident',
                "minima": 'repellendus',
            },
        ),
    ),
    collection='totam',
    project='similique',
)

res = s.collection.replace_documents(req)

if res.replace_response is not None:
    # handle response
```

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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TigrisSearchRequest(
    search_request=shared.SearchRequest(
        branch='alias',
        collation=shared.Collation(
            case='at',
        ),
        exclude_fields=[
            'tempora',
            'vel',
        ],
        facet={
            "officiis": 'qui',
            "dolorum": 'a',
            "esse": 'harum',
            "iusto": 'ipsum',
        },
        fields_={
            "tenetur": 'amet',
            "tempore": 'accusamus',
            "numquam": 'enim',
            "dolorem": 'sapiente',
        },
        filter={
            "nihil": 'sit',
            "expedita": 'neque',
            "sed": 'vel',
        },
        include_fields=[
            'voluptas',
            'deserunt',
            'quam',
        ],
        page=214880,
        page_size=277628,
        q='qui',
        search_fields=[
            'maxime',
            'pariatur',
            'soluta',
        ],
        sort={
            "laborum": 'totam',
        },
    ),
    collection='incidunt',
    project='aspernatur',
)

res = s.collection.search_documents(req)

if res.streaming_search_response is not None:
    # handle response
```

## update_documents

Update a range of documents in the collection using the condition provided in the filter.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TigrisUpdateRequest(
    update_request=shared.UpdateRequest(
        branch='dolores',
        fields_={
            "facilis": 'aliquid',
            "quam": 'molestias',
            "temporibus": 'qui',
        },
        filter={
            "fugit": 'magni',
        },
        options=shared.UpdateRequestOptions(
            collation=shared.Collation(
                case='odio',
            ),
            limit=124833,
            write_options={
                "nam": 'hic',
                "voluptatem": 'cumque',
            },
        ),
    ),
    collection='soluta',
    project='nobis',
)

res = s.collection.update_documents(req)

if res.update_response is not None:
    # handle response
```
