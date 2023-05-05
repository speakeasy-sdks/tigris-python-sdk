# database

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
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.database.begin_transaction(shared.BeginTransactionRequest(
    branch='ipsa',
    options={
        "iure": 'odio',
    },
), 'quaerat')

if res.begin_transaction_response is not None:
    # handle response
```

## commit_transaction

Atomically commit all the changes performed in the context of the transaction. Commit provides all
 or nothing semantics by ensuring no partial updates are in the project due to a transaction failure.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.database.commit_transaction(shared.CommitTransactionRequest(
    branch='accusamus',
), 'quidem')

if res.commit_transaction_response is not None:
    # handle response
```

## create_branch

Creates a new database branch, if not already existing.

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.database.create_branch({
    "voluptas": 'natus',
    "eos": 'atque',
    "sit": 'fugiat',
    "ab": 'soluta',
}, 'dolorum', 'iusto')

if res.create_branch_response is not None:
    # handle response
```

## delete_branch

Deletes a database branch, if exists.
 Throws 400 Bad Request if "main" branch is being deleted

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.database.delete_branch({
    "dolorum": 'deleniti',
    "omnis": 'necessitatibus',
}, 'distinctio', 'asperiores')

if res.delete_branch_response is not None:
    # handle response
```

## describe

This API returns information related to the project along with all the collections inside the project.
 This can be used to retrieve the size of the project or to retrieve schemas, branches and the size of all the collections present in this project.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.database.describe(shared.DescribeDatabaseRequest(
    branch='nihil',
    project='ipsum',
    schema_format='voluptate',
), 'id')

if res.describe_database_response is not None:
    # handle response
```

## list_collections

List all the collections present in the project passed in the request.

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.database.list_collections('saepe', 'eius')

if res.list_collections_response is not None:
    # handle response
```

## rollback_transaction

Rollback transaction discards all the changes
 performed in the transaction

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.database.rollback_transaction(shared.RollbackTransactionRequest(
    branch='aspernatur',
), 'perferendis')

if res.rollback_transaction_response is not None:
    # handle response
```

## tigris_list_branches

List database branches

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.database.tigris_list_branches('amet')

if res.list_branches_response is not None:
    # handle response
```
