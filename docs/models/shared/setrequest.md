# SetRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `ex`                                               | *Optional[int]*                                    | :heavy_minus_sign:                                 | optional - ttl specific to this key in second      |
| `nx`                                               | *Optional[bool]*                                   | :heavy_minus_sign:                                 | set only if the key doesn't exist                  |
| `px`                                               | *Optional[int]*                                    | :heavy_minus_sign:                                 | optional - ttl specific to this key in millisecond |
| `value`                                            | *Optional[str]*                                    | :heavy_minus_sign:                                 | free form byte[] value                             |
| `xx`                                               | *Optional[bool]*                                   | :heavy_minus_sign:                                 | set only if the key exist                          |