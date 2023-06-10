"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from tigris import utils
from typing import Optional



@dataclasses.dataclass
class GetNamespaceMetadataResponseValue:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetNamespaceMetadataResponse:
    r"""Namespace metadata response"""
    metadata_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadataKey'), 'exclude': lambda f: f is None }})
    namespace_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceId'), 'exclude': lambda f: f is None }})
    value: Optional[GetNamespaceMetadataResponseValue] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    

