from __future__ import annotations
import dataclasses
from ..shared import rollupfunction as shared_rollupfunction
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AdditionalFunction:
    r"""AdditionalFunction
    Additional function to apply on metrics query
    """
    
    rollup: Optional[shared_rollupfunction.RollupFunction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rollup'), 'exclude': lambda f: f is None }})
    