from __future__ import annotations
import dataclasses
from ..shared import docstatus as shared_docstatus
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteDocumentResponse:
    status: Optional[list[shared_docstatus.DocStatus]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    