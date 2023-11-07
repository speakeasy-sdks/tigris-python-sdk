# SearchResponse

Response struct for search


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `facets`                                                                 | Dict[str, [shared.SearchFacet](../../models/shared/searchfacet.md)]      | :heavy_minus_sign:                                                       | N/A                                                                      |
| `hits`                                                                   | List[[shared.SearchHit](../../models/shared/searchhit.md)]               | :heavy_minus_sign:                                                       | N/A                                                                      |
| `meta`                                                                   | [Optional[shared.SearchMetadata]](../../models/shared/searchmetadata.md) | :heavy_minus_sign:                                                       | N/A                                                                      |