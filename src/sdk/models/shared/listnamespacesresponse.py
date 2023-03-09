from __future__ import annotations
import dataclasses
from ..shared import namespaceinfo as shared_namespaceinfo
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListNamespacesResponse:
    namespaces: Optional[list[shared_namespaceinfo.NamespaceInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaces'), 'exclude': lambda f: f is None }})
    