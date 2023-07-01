# DeleteByQueryRequest


## Fields

| Field                                                                                                                                | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `filter`                                                                                                                             | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | A filter is required to delete matching documents. To delete document by id, you can pass the filter as follows ```{"id": "test"}``` |
| `index`                                                                                                                              | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | The index name of the documents that needs deletion.                                                                                 |
| `project`                                                                                                                            | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | The project name.                                                                                                                    |