# SearchIndexResponse

Response struct for search


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `facets`                                                                     | dict[str, [shared.SearchFacet](undefined/models/shared/searchfacet.md)]      | :heavy_minus_sign:                                                           | N/A                                                                          |
| `hits`                                                                       | list[[shared.IndexDoc](undefined/models/shared/indexdoc.md)]                 | :heavy_minus_sign:                                                           | N/A                                                                          |
| `meta`                                                                       | [Optional[shared.SearchMetadata]](undefined/models/shared/searchmetadata.md) | :heavy_minus_sign:                                                           | N/A                                                                          |