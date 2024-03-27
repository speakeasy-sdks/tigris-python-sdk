# QuotaLimitsResponse

Contains current quota limits


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `read_units`                             | *Optional[int]*                          | :heavy_minus_sign:                       | Number of allowed read units per second  |
| `storage_size`                           | *Optional[int]*                          | :heavy_minus_sign:                       | Maximum number of bytes allowed to store |
| `write_units`                            | *Optional[int]*                          | :heavy_minus_sign:                       | Number of allowed write units per second |