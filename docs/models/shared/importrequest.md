# ImportRequest


## Fields

| Field                                                                                                                                                                                                              | Type                                                                                                                                                                                                               | Required                                                                                                                                                                                                           | Description                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `autogenerated`                                                                                                                                                                                                    | list[*str*]                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                 | The list of autogenerated fields of the collection                                                                                                                                                                 |
| `branch`                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                 | Optionally specify a database branch name to perform operation on                                                                                                                                                  |
| `create_collection`                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                 | Allow to create collection if it doesn't exists                                                                                                                                                                    |
| `documents`                                                                                                                                                                                                        | list[[ImportRequestDocuments](../../models/shared/importrequestdocuments.md)]                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                 | Array of documents to import. Each document is a JSON object.                                                                                                                                                      |
| `options`                                                                                                                                                                                                          | [Optional[ImportRequestOptions]](../../models/shared/importrequestoptions.md)                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                 | additional options for import requests.                                                                                                                                                                            |
| `primary_key`                                                                                                                                                                                                      | list[*str*]                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                 | List of fields which constitutes primary key of the collection If not specified and field with name 'id' is present, it's used as a primary key, further if inferred type is UUID, then it's set as autogenerated. |