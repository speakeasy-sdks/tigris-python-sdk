from __future__ import annotations
import dataclasses
from ..shared import describenamespacesdata as shared_describenamespacesdata
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DescribeNamespacesResponse:
    data: Optional[shared_describenamespacesdata.DescribeNamespacesData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    