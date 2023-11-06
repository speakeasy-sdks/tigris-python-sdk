# ReadResponse


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `data`                                                                | [Optional[ReadResponseData]](../../models/shared/readresponsedata.md) | :heavy_minus_sign:                                                    | Object containing the collection document.                            |
| `metadata`                                                            | [Optional[ResponseMetadata]](../../models/shared/responsemetadata.md) | :heavy_minus_sign:                                                    | Has metadata related to the documents stored.                         |
| `resume_token`                                                        | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | An internal key, used for pagination.                                 |