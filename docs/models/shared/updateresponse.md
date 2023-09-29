# UpdateResponse


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `metadata`                                                                       | [Optional[shared.ResponseMetadata]](undefined/models/shared/responsemetadata.md) | :heavy_minus_sign:                                                               | Has metadata related to the documents stored.                                    |
| `modified_count`                                                                 | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | Returns the number of documents modified.                                        |
| `status`                                                                         | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | an enum with value set as "updated".                                             |