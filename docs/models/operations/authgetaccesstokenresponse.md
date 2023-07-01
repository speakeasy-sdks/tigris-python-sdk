# AuthGetAccessTokenResponse


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `content_type`                                                                           | *str*                                                                                    | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `get_access_token_response`                                                              | [Optional[shared.GetAccessTokenResponse]](../../models/shared/getaccesstokenresponse.md) | :heavy_minus_sign:                                                                       | OK                                                                                       |
| `status`                                                                                 | [Optional[shared.Status]](../../models/shared/status.md)                                 | :heavy_minus_sign:                                                                       | Default error response                                                                   |
| `status_code`                                                                            | *int*                                                                                    | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `raw_response`                                                                           | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)    | :heavy_minus_sign:                                                                       | N/A                                                                                      |