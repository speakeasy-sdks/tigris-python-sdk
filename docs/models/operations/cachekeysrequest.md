# CacheKeysRequest


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `name`                                                            | *str*                                                             | :heavy_check_mark:                                                | cache name                                                        |
| `project`                                                         | *str*                                                             | :heavy_check_mark:                                                | Tigris project name                                               |
| `count`                                                           | *Optional[int]*                                                   | :heavy_minus_sign:                                                | optional - count of keys to return a stream response line.        |
| `cursor`                                                          | *Optional[int]*                                                   | :heavy_minus_sign:                                                | optional - cursor - skip this argument if no cursor is associated |
| `pattern`                                                         | *Optional[str]*                                                   | :heavy_minus_sign:                                                | optional key pattern                                              |