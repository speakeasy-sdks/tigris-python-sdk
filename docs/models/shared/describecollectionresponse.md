# DescribeCollectionResponse

A detailed description of the collection. The description returns collection metadata and the schema.


## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `collection`                                                                                          | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Name of the collection.                                                                               |
| `metadata`                                                                                            | [Optional[CollectionMetadata]](../../models/shared/collectionmetadata.md)                             | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `schema`                                                                                              | [Optional[DescribeCollectionResponseSchema]](../../models/shared/describecollectionresponseschema.md) | :heavy_minus_sign:                                                                                    | Schema of this collection.                                                                            |
| `size`                                                                                                | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | The size of this collection in bytes.                                                                 |