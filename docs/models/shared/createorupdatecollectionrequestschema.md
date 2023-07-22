# CreateOrUpdateCollectionRequestSchema

The schema specifications are same as JSON schema specification defined <a href="https://json-schema.org/specification.html" title="here">here</a>.<p></p> Schema example: `{  "title": "user",  "description": "Collection of documents with details of users",  "properties": {    "id": {      "description": "A unique identifier for the user",      "type": "integer"    },    "name": {      "description": "Name of the user",      "type": "string",      "maxLength": 128    },    "balance": {      "description": "User account balance",      "type": "number"    }  },  "primary_key": ["id"] }`


## Fields

| Field       | Type        | Required    | Description |
| ----------- | ----------- | ----------- | ----------- |