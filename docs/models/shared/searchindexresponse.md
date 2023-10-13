# SearchIndexResponse

Response struct for search


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `facets`                                                          | dict[str, [SearchFacet](../../models/shared/searchfacet.md)]      | :heavy_minus_sign:                                                | N/A                                                               |
| `hits`                                                            | list[[IndexDoc](../../models/shared/indexdoc.md)]                 | :heavy_minus_sign:                                                | N/A                                                               |
| `meta`                                                            | [Optional[SearchMetadata]](../../models/shared/searchmetadata.md) | :heavy_minus_sign:                                                | N/A                                                               |