# InsertRequest


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `branch`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | Optionally specify a database branch name to perform operation on             |
| `documents`                                                                   | List[[InsertRequestDocuments](../../models/shared/insertrequestdocuments.md)] | :heavy_minus_sign:                                                            | Array of documents to insert. Each document is a JSON object.                 |
| `options`                                                                     | [Optional[InsertRequestOptions]](../../models/shared/insertrequestoptions.md) | :heavy_minus_sign:                                                            | additional options for insert requests.                                       |