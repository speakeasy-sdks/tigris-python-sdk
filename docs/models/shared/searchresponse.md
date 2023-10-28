# SearchResponse

Response struct for search


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `facets`                                                          | Dict[str, [SearchFacet](../../models/shared/searchfacet.md)]      | :heavy_minus_sign:                                                | N/A                                                               |
| `hits`                                                            | List[[SearchHit](../../models/shared/searchhit.md)]               | :heavy_minus_sign:                                                | N/A                                                               |
| `meta`                                                            | [Optional[SearchMetadata]](../../models/shared/searchmetadata.md) | :heavy_minus_sign:                                                | N/A                                                               |