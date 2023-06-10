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
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisCreateProjectRequest(
    create_project_request=shared.CreateProjectRequest(),
    project='error',
)

res = s.project.create(req)

if res.create_project_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.TigrisCreateProjectRequest](../../models/operations/tigriscreateprojectrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.TigrisCreateProjectResponse](../../models/operations/tigriscreateprojectresponse.md)**


## delete_project

Delete Project deletes all the collections in this project along with all of the documents, and associated metadata for these collections.

### Example Usage

```python
import tigris
from tigris.models import operations, shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TigrisDeleteProjectRequest(
    delete_project_request=shared.DeleteProjectRequest(),
    project='eaque',
)

res = s.project.delete_project(req)

if res.delete_project_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.TigrisDeleteProjectRequest](../../models/operations/tigrisdeleteprojectrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.TigrisDeleteProjectResponse](../../models/operations/tigrisdeleteprojectresponse.md)**


## list

List returns all the projects.

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.project.list()

if res.list_projects_response is not None:
    # handle response
```


### Response

**[operations.TigrisListProjectsResponse](../../models/operations/tigrislistprojectsresponse.md)**

