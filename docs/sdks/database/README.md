# Database
(*database*)

## Overview

The Database section provide APIs that can be used to interact with the database. A single Database can have one or more collections. A database is created automatically for you when you create a project.

### Available Operations

* [begin_transaction](#begin_transaction) - Begin a transaction
* [commit_transaction](#commit_transaction) - Commit a Transaction
* [create_branch](#create_branch) - Create a database branch
* [delete_branch](#delete_branch) - Delete a database branch
* [describe](#describe) - Describe database
* [list_collections](#list_collections) - List Collections
* [rollback_transaction](#rollback_transaction) - Rollback a transaction
* [tigris_list_branches](#tigris_list_branches) - List database branches

## begin_transaction

Starts a new transaction and returns a transactional object. All reads/writes performed
 within a transaction will run with serializable isolation. Tigris offers global transactions,
 with ACID properties and strict serializability.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.TigrisBeginTransactionRequest(
    begin_transaction_request=shared.BeginTransactionRequest(
        options=shared.TransactionOptions(),
    ),
    project='string',
)

res = s.database.begin_transaction(req)

if res.begin_transaction_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.TigrisBeginTransactionRequest](../../models/operations/tigrisbegintransactionrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.TigrisBeginTransactionResponse](../../models/operations/tigrisbegintransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## commit_transaction

Atomically commit all the changes performed in the context of the transaction. Commit provides all
 or nothing semantics by ensuring no partial updates are in the project due to a transaction failure.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.TigrisCommitTransactionRequest(
    commit_transaction_request=shared.CommitTransactionRequest(),
    project='string',
)

res = s.database.commit_transaction(req)

if res.commit_transaction_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.TigrisCommitTransactionRequest](../../models/operations/tigriscommittransactionrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.TigrisCommitTransactionResponse](../../models/operations/tigriscommittransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_branch

Creates a new database branch, if not already existing.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.TigrisCreateBranchRequest(
    create_branch_request=shared.CreateBranchRequest(),
    branch='string',
    project='string',
)

res = s.database.create_branch(req)

if res.create_branch_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.TigrisCreateBranchRequest](../../models/operations/tigriscreatebranchrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.TigrisCreateBranchResponse](../../models/operations/tigriscreatebranchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_branch

Deletes a database branch, if exists.
 Throws 400 Bad Request if "main" branch is being deleted

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.TigrisDeleteBranchRequest(
    delete_branch_request=shared.DeleteBranchRequest(),
    branch='string',
    project='string',
)

res = s.database.delete_branch(req)

if res.delete_branch_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.TigrisDeleteBranchRequest](../../models/operations/tigrisdeletebranchrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.TigrisDeleteBranchResponse](../../models/operations/tigrisdeletebranchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## describe

This API returns information related to the project along with all the collections inside the project.
 This can be used to retrieve the size of the project or to retrieve schemas, branches and the size of all the collections present in this project.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.TigrisDescribeDatabaseRequest(
    describe_database_request=shared.DescribeDatabaseRequest(),
    project='string',
)

res = s.database.describe(req)

if res.describe_database_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.TigrisDescribeDatabaseRequest](../../models/operations/tigrisdescribedatabaserequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.TigrisDescribeDatabaseResponse](../../models/operations/tigrisdescribedatabaseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_collections

List all the collections present in the project passed in the request.

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.TigrisListCollectionsRequest(
    project='string',
)

res = s.database.list_collections(req)

if res.list_collections_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.TigrisListCollectionsRequest](../../models/operations/tigrislistcollectionsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.TigrisListCollectionsResponse](../../models/operations/tigrislistcollectionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## rollback_transaction

Rollback transaction discards all the changes
 performed in the transaction

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.TigrisRollbackTransactionRequest(
    rollback_transaction_request=shared.RollbackTransactionRequest(),
    project='string',
)

res = s.database.rollback_transaction(req)

if res.rollback_transaction_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.TigrisRollbackTransactionRequest](../../models/operations/tigrisrollbacktransactionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.TigrisRollbackTransactionResponse](../../models/operations/tigrisrollbacktransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## tigris_list_branches

List database branches

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.TigrisListBranchesRequest(
    project='string',
)

res = s.database.tigris_list_branches(req)

if res.list_branches_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.TigrisListBranchesRequest](../../models/operations/tigrislistbranchesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.TigrisListBranchesResponse](../../models/operations/tigrislistbranchesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
