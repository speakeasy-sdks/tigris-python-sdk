from __future__ import annotations
import dataclasses
from ..shared import projectinfo as shared_projectinfo
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListProjectsResponse:
    projects: Optional[list[shared_projectinfo.ProjectInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projects'), 'exclude': lambda f: f is None }})
    