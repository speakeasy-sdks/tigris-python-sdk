from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class QuotaUsageResponse:
    r"""QuotaUsageResponse
    Contains current quota usage
    """
    
    read_units: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ReadUnits'), 'exclude': lambda f: f is None }})
    read_units_throttled: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ReadUnitsThrottled'), 'exclude': lambda f: f is None }})
    storage_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('StorageSize'), 'exclude': lambda f: f is None }})
    storage_size_throttled: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('StorageSizeThrottled'), 'exclude': lambda f: f is None }})
    write_units: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('WriteUnits'), 'exclude': lambda f: f is None }})
    write_units_throttled: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('WriteUnitsThrottled'), 'exclude': lambda f: f is None }})
    