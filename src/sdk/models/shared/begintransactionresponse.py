from __future__ import annotations
import dataclasses
from ..shared import transactionctx as shared_transactionctx
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BeginTransactionResponse:
    r"""BeginTransactionResponse
    Start transaction returns transaction context  which uniquely identifies the transaction
    """
    
    tx_ctx: Optional[shared_transactionctx.TransactionCtx] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tx_ctx'), 'exclude': lambda f: f is None }})
    