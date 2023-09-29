# TigrisReadRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `read_request`                                                         | [Optional[shared.ReadRequest]](undefined/models/shared/readrequest.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `collection`                                                           | *Optional[str]*                                                        | :heavy_check_mark:                                                     | Collection name to read documents from.                                |
| `project`                                                              | *Optional[str]*                                                        | :heavy_check_mark:                                                     | Project name whose db is under target to read documents from.          |