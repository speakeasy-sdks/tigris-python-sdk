# CreateDocumentRequest


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `documents`                                                                      | List[*str*]                                                                      | :heavy_minus_sign:                                                               | An array of documents to be created or replaced. Each document is a JSON object. |
| `index`                                                                          | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | index name where to create documents.                                            |
| `project`                                                                        | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Tigris project name.                                                             |