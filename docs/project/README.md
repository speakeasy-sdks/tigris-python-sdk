# project

## Overview

Every Tigris projects comes with a transactional document database built on FoundationDB, one of the most resilient and battle-tested open source distributed key-value store. A database is created automatically for you when you create a project.

### Available Operations

* [create](#create) - Create Project
* [delete_project](#delete_project) - Delete Project and all resources under project
* [list](#list) - List Projects

## create

Creates a new project. Returns an AlreadyExists error with a status code 409 if the project already exists.

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.project.create({
    "praesentium": 'quisquam',
}, 'veritatis')

if res.create_project_response is not None:
    # handle response
```

## delete_project

Delete Project deletes all the collections in this project along with all of the documents, and associated metadata for these collections.

### Example Usage

```python
import tigris
from tigris.models import operations

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.project.delete_project({
    "id": 'quidem',
}, 'neque')

if res.delete_project_response is not None:
    # handle response
```

## list

List returns all the projects.

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.project.list()

if res.list_projects_response is not None:
    # handle response
```
