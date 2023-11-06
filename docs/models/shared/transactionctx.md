# TransactionCtx

Contains ID which uniquely identifies transaction This context is returned by BeginTransaction request and should be passed in the metadata (headers) of subsequent requests in order to run them in the context of the same transaction.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `id`                                       | *Optional[str]*                            | :heavy_minus_sign:                         | Unique for a single transactional request. |
| `origin`                                   | *Optional[str]*                            | :heavy_minus_sign:                         | Serves as an internal identifier.          |