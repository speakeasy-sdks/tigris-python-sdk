# SearchResponse

Response struct for search


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `facets`                                                                     | dict[str, [shared.SearchFacet](undefined/models/shared/searchfacet.md)]      | :heavy_minus_sign:                                                           | N/A                                                                          |
| `hits`                                                                       | list[[shared.SearchHit](undefined/models/shared/searchhit.md)]               | :heavy_minus_sign:                                                           | N/A                                                                          |
| `meta`                                                                       | [Optional[shared.SearchMetadata]](undefined/models/shared/searchmetadata.md) | :heavy_minus_sign:                                                           | N/A                                                                          |