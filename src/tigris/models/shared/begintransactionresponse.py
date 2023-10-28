"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import transactionctx as shared_transactionctx
from dataclasses_json import Undefined, dataclass_json
from tigris import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BeginTransactionResponse:
    r"""Start transaction returns transaction context  which uniquely identifies the transaction"""
    tx_ctx: Optional[shared_transactionctx.TransactionCtx] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tx_ctx'), 'exclude': lambda f: f is None }})
    r"""Contains ID which uniquely identifies transaction This context is returned by BeginTransaction request and should be passed in the metadata (headers) of subsequent requests in order to run them in the context of the same transaction."""
    

