# SearchIndexResponse

Response struct for search


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `facets`                                                                 | Dict[str, [shared.SearchFacet](../../models/shared/searchfacet.md)]      | :heavy_minus_sign:                                                       | N/A                                                                      |
| `hits`                                                                   | List[[shared.IndexDoc](../../models/shared/indexdoc.md)]                 | :heavy_minus_sign:                                                       | N/A                                                                      |
| `meta`                                                                   | [Optional[shared.SearchMetadata]](../../models/shared/searchmetadata.md) | :heavy_minus_sign:                                                       | N/A                                                                      |