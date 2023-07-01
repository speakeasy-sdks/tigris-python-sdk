# Message


## Fields

| Field                                                                                                                                                                           | Type                                                                                                                                                                            | Required                                                                                                                                                                        | Description                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `id`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | an optional id if idempotency is needed to ensure only a single time message is published during retries. If not specified then server will automatically add an id to message. |
| `name`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `sequence`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |