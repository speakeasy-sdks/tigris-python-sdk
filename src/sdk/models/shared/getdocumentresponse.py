from __future__ import annotations
import dataclasses
from ..shared import indexdoc as shared_indexdoc
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDocumentResponse:
    documents: Optional[list[shared_indexdoc.IndexDoc]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documents'), 'exclude': lambda f: f is None }})
    