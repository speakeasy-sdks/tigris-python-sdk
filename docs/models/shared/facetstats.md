# FacetStats

Additional stats for faceted field


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `avg`                                                               | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Average of all values in a field. Only available for numeric fields |
| `count`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Total number of values in a field                                   |
| `max`                                                               | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Maximum of all values in a field. Only available for numeric fields |
| `min`                                                               | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Minimum of all values in a field. Only available for numeric fields |
| `sum`                                                               | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Sum of all values in a field. Only available for numeric fields     |