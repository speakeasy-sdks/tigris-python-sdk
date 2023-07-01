# ReplaceRequest


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `branch`                                                                        | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Optionally specify a database branch name to perform operation on               |
| `documents`                                                                     | list[[ReplaceRequestDocuments](../../models/shared/replacerequestdocuments.md)] | :heavy_minus_sign:                                                              | Array of documents to be replaced. Each document is a JSON object.              |
| `options`                                                                       | [Optional[ReplaceRequestOptions]](../../models/shared/replacerequestoptions.md) | :heavy_minus_sign:                                                              | Additional options for replace requests.                                        |