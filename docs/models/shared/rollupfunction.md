# RollupFunction

Rollup function aggregates the slices of metrics returned by original query and lets you operate on the slices using aggregator and constructs the bigger slice of your choice of interval (specified in seconds).


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `aggregator`                                                     | [Optional[shared.Aggregator]](../../models/shared/aggregator.md) | :heavy_minus_sign:                                               | N/A                                                              |
| `interval`                                                       | *Optional[int]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |