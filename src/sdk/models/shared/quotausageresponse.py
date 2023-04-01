"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class QuotaUsageResponse:
    r"""Contains current quota usage"""
    
    read_units: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ReadUnits'), 'exclude': lambda f: f is None }})
    r"""Number of read units used per second"""  
    read_units_throttled: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ReadUnitsThrottled'), 'exclude': lambda f: f is None }})
    r"""Number of read units throttled per second. Units which was rejected with \\"resource exhausted error\\"."""  
    storage_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('StorageSize'), 'exclude': lambda f: f is None }})
    r"""Number of bytes stored"""  
    storage_size_throttled: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('StorageSizeThrottled'), 'exclude': lambda f: f is None }})
    r"""Number of bytes throttled. Number of bytes which were attempted to write in excess of quota and were rejected."""  
    write_units: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('WriteUnits'), 'exclude': lambda f: f is None }})
    r"""Number of write units used per second"""  
    write_units_throttled: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('WriteUnitsThrottled'), 'exclude': lambda f: f is None }})
    r"""Number of write units throttled per second. Units which was rejected with \\"resource exhausted error\\"."""  
    