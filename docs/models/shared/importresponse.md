# ImportResponse

OK


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `keys`                                                                | list[*str*]                                                           | :heavy_minus_sign:                                                    | an array returns the value of the primary keys.                       |
| `metadata`                                                            | [Optional[ResponseMetadata]](../../models/shared/responsemetadata.md) | :heavy_minus_sign:                                                    | Has metadata related to the documents stored.                         |
| `status`                                                              | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | An enum with value set as "inserted"                                  |