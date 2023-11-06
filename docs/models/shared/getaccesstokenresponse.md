# GetAccessTokenResponse

The response of GetAccessToken which contains access_token and optionally refresh_token.


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `access_token`                              | *Optional[str]*                             | :heavy_minus_sign:                          | An Access Token.                            |
| `expires_in`                                | *Optional[int]*                             | :heavy_minus_sign:                          | Access token expiration timeout in seconds. |
| `refresh_token`                             | *Optional[str]*                             | :heavy_minus_sign:                          | The Refresh Token.                          |