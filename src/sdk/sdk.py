__doc__ = """ SDK Documentation: # Overview
This section is organized around HTTP APIs. The APIs accepts JSON requests and returns JSON-encoded responses.The APIs conforms to standard HTTP status codes.

# Errors
Tigris uses conventional HTTP response codes to indicate the success or failure of an API request.The response will  contain an error code or other information that reveals the reason of the error. 
The error response is in JSON format and is structured like this:
```
 {
   "error": {
     "code": "ALREADY_EXISTS",
     "message": "row already exists"
   }
 }

```

## Status 2xx

  HTTP Code  | Reason
  ----------------|-------------
  200 - OK | Everything worked as expected.


## Status 4xx
Status codes in the `400-499` range indicate errors that have been caused by the requesting application (e.g., a malformed request body has been sent).
Retrying such requests with the same request body is pointless and _will_ result in the same status code again. Some `4xx` errors can be handled programmatically. Change the request accordingly before retrying. Below you can find the most frequent 4XX errors and how to fix them.

  HTTP Code  | Tigris Code | Reason
  ----------------|-------------|---------
  400 - Bad Request | INVALID_ARGUMENT | The request was unacceptable, often due to missing a required parameter. <br>Examples: <li>Missing documents for write request</li><li>Collection or Database name is not following the allowed characters</li>
  401 - Unauthorized | UNAUTHENTICATED | No valid API key provided. Check that your `api_key` and `api_secret` are correct.
  403 - Forbidden | PERMISSION_DENIED | The API key doesn't have permissions to perform the request.
  404 - Not Found | NOT_FOUND | The requested resource doesn't exist. <br>Examples: <li>Database or Collection doesn't exists</li><li>Access Token missing in the request header</li>
  409 - Conflict | ALREADY_EXISTS | TThe request conflicts with another request (perhaps due to using the same idempotent key). <br>Examples: <li>Trying to insert document again for the primary key that already exists</li><li>Creating a database that already exists</li>
  429 - Too Many Requests | RESOURCE_EXHAUSTED | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
  
  
  
## Status 5xx
The 5xx range indicate an error with Tigris servers (these are rare).

  HTTP Code  | Tigris Code | Reason
  ----------------|-------------|---------
  500 - Internal Server Error | UNKNOWN | Something went wrong on Tigris server side.                    
  501 - Not Implemented       | UNIMPLEMENTED | Not supported by the Tigris server and cannot be handled. 
  502 - Bad Gateway           | BAD_GATEWAY | The API key doesn't have permissions to perform the request.
  503 - Service Unavailable   | UNAVAILABLE | The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded.
  504 - Gateway Timeout       | DEADLINE_EXCEEDED | Tigris server is unable to process the request timely. Common causes are that request is expensive, or server is overloaded.
  
# Idempotent Requests
  
  Tigris provides idempotency guarantees when an API call is disrupted and either no response is returned or an HTTP 
  Status code `429,500,501,502,503` is returned. These errors ensure that the request is not committed and retrying the same request will have the same effect.


# Limitations
<li>Do not rely on case to distinguish between databases or collections names.</li> <li>Database Name and Collection Name cannot be empty and can only have the characters matches the regex: <code>^[a-zA-Z]+[a-zA-Z0-9_]+$</code>.</li> <li>Duplicate field names are not allowed. </li> <li>The maximum allowed document size is 100KB.</li> <li>The maximum allowed transaction size is 10MB.</li>
"""
import requests as requests_http
from . import utils
from .appkey import AppKey
from .auth import Auth
from .cache import Cache
from .channel import Channel
from .collection import Collection
from .database import Database
from .namespace import Namespace
from .project import Project
from .search import Search
from .system import System
from .user import User
from sdk.models import shared

SERVERS = [
	"https://api.preview.tigrisdata.cloud",
	"http://localhost:8081",
]

class SDK:
    r"""SDK Documentation: # Overview
    This section is organized around HTTP APIs. The APIs accepts JSON requests and returns JSON-encoded responses.The APIs conforms to standard HTTP status codes.
    
    # Errors
    Tigris uses conventional HTTP response codes to indicate the success or failure of an API request.The response will  contain an error code or other information that reveals the reason of the error. 
    The error response is in JSON format and is structured like this:
    ```
     {
       \"error\": {
         \"code\": \"ALREADY_EXISTS\",
         \"message\": \"row already exists\"
       }
     }
    
    ```
    
    ## Status 2xx
    
      HTTP Code  | Reason
      ----------------|-------------
      200 - OK | Everything worked as expected.
    
    
    ## Status 4xx
    Status codes in the `400-499` range indicate errors that have been caused by the requesting application (e.g., a malformed request body has been sent).
    Retrying such requests with the same request body is pointless and _will_ result in the same status code again. Some `4xx` errors can be handled programmatically. Change the request accordingly before retrying. Below you can find the most frequent 4XX errors and how to fix them.
    
      HTTP Code  | Tigris Code | Reason
      ----------------|-------------|---------
      400 - Bad Request | INVALID_ARGUMENT | The request was unacceptable, often due to missing a required parameter. <br>Examples: <li>Missing documents for write request</li><li>Collection or Database name is not following the allowed characters</li>
      401 - Unauthorized | UNAUTHENTICATED | No valid API key provided. Check that your `api_key` and `api_secret` are correct.
      403 - Forbidden | PERMISSION_DENIED | The API key doesn't have permissions to perform the request.
      404 - Not Found | NOT_FOUND | The requested resource doesn't exist. <br>Examples: <li>Database or Collection doesn't exists</li><li>Access Token missing in the request header</li>
      409 - Conflict | ALREADY_EXISTS | TThe request conflicts with another request (perhaps due to using the same idempotent key). <br>Examples: <li>Trying to insert document again for the primary key that already exists</li><li>Creating a database that already exists</li>
      429 - Too Many Requests | RESOURCE_EXHAUSTED | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
      
      
      
    ## Status 5xx
    The 5xx range indicate an error with Tigris servers (these are rare).
    
      HTTP Code  | Tigris Code | Reason
      ----------------|-------------|---------
      500 - Internal Server Error | UNKNOWN | Something went wrong on Tigris server side.                    
      501 - Not Implemented       | UNIMPLEMENTED | Not supported by the Tigris server and cannot be handled. 
      502 - Bad Gateway           | BAD_GATEWAY | The API key doesn't have permissions to perform the request.
      503 - Service Unavailable   | UNAVAILABLE | The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded.
      504 - Gateway Timeout       | DEADLINE_EXCEEDED | Tigris server is unable to process the request timely. Common causes are that request is expensive, or server is overloaded.
      
    # Idempotent Requests
      
      Tigris provides idempotency guarantees when an API call is disrupted and either no response is returned or an HTTP 
      Status code `429,500,501,502,503` is returned. These errors ensure that the request is not committed and retrying the same request will have the same effect.
    
    
    # Limitations
    <li>Do not rely on case to distinguish between databases or collections names.</li> <li>Database Name and Collection Name cannot be empty and can only have the characters matches the regex: <code>^[a-zA-Z]+[a-zA-Z0-9_]+$</code>.</li> <li>Duplicate field names are not allowed. </li> <li>The maximum allowed document size is 100KB.</li> <li>The maximum allowed transaction size is 10MB.</li>
    """
    app_key: AppKey
    auth: Auth
    cache: Cache
    channel: Channel
    collection: Collection
    database: Database
    namespace: Namespace
    project: Project
    search: Search
    system: System
    user: User
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _security: shared.Security
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.0.2"
    _gen_version: str = "1.9.2"

    def __init__(self) -> None:
        self._client = requests_http.Session()
        self._security_client = requests_http.Session()
        self._init_sdks()

    def config_server_url(self, server_url: str, params: dict[str, str] = None):
        if params is not None:
            self._server_url = utils.template_url(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    
    

    def config_client(self, client: requests_http.Session):
        self._client = client
        
        if self._security is not None:
            self._security_client = utils.configure_security_client(self._client, self._security)
        self._init_sdks()
    
    def config_security(self, security: shared.Security):
        self._security = security
        self._security_client = utils.configure_security_client(self._client, security)
        self._init_sdks()
    
    def _init_sdks(self):
        self.app_key = AppKey(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.auth = Auth(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.cache = Cache(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.channel = Channel(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.collection = Collection(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.database = Database(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.namespace = Namespace(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.project = Project(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.search = Search(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.system = System(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.user = User(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    