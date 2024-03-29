"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from tigris import utils
from typing import Optional

class RollupFunctionAggregatorEnum(str, Enum):
    ROLLUP_AGGREGATOR_SUM = 'ROLLUP_AGGREGATOR_SUM'
    ROLLUP_AGGREGATOR_COUNT = 'ROLLUP_AGGREGATOR_COUNT'
    ROLLUP_AGGREGATOR_MIN = 'ROLLUP_AGGREGATOR_MIN'
    ROLLUP_AGGREGATOR_MAX = 'ROLLUP_AGGREGATOR_MAX'
    ROLLUP_AGGREGATOR_AVG = 'ROLLUP_AGGREGATOR_AVG'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RollupFunction:
    r"""Rollup function aggregates the slices of metrics returned by original query and lets you operate on the slices using aggregator and constructs the bigger slice of your choice of interval (specified in seconds)."""
    
    aggregator: Optional[RollupFunctionAggregatorEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aggregator'), 'exclude': lambda f: f is None }})
    interval: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval'), 'exclude': lambda f: f is None }})
    