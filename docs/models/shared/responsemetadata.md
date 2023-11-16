# ResponseMetadata

Has metadata related to the documents stored.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `created_at`                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                             | :heavy_minus_sign:                                                                               | Time at which the document was inserted/replaced. Measured in nano-seconds since the Unix epoch. |
| `deleted_at`                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                             | :heavy_minus_sign:                                                                               | Time at which the document was deleted. Measured in nano-seconds since the Unix epoch.           |
| `updated_at`                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                             | :heavy_minus_sign:                                                                               | Time at which the document was updated. Measured in nano-seconds since the Unix epoch.           |