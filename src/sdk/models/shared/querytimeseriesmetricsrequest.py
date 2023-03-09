from __future__ import annotations
import dataclasses
from ..shared import additionalfunction as shared_additionalfunction
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class QueryTimeSeriesMetricsRequestFunctionEnum(str, Enum):
    RATE = "RATE"
    COUNT = "COUNT"
    NONE = "NONE"

class QueryTimeSeriesMetricsRequestSpaceAggregationEnum(str, Enum):
    AVG = "AVG"
    MIN = "MIN"
    MAX = "MAX"
    SUM = "SUM"

class QueryTimeSeriesMetricsRequestTigrisOperationEnum(str, Enum):
    ALL = "ALL"
    READ = "READ"
    WRITE = "WRITE"
    METADATA = "METADATA"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class QueryTimeSeriesMetricsRequest:
    r"""QueryTimeSeriesMetricsRequest
    Requests the time series metrics
    """
    
    additional_functions: Optional[list[shared_additionalfunction.AdditionalFunction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalFunctions'), 'exclude': lambda f: f is None }})
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})
    collection: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection'), 'exclude': lambda f: f is None }})
    db: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('db'), 'exclude': lambda f: f is None }})
    from_: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'exclude': lambda f: f is None }})
    function: Optional[QueryTimeSeriesMetricsRequestFunctionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('function'), 'exclude': lambda f: f is None }})
    metric_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metric_name'), 'exclude': lambda f: f is None }})
    quantile: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantile'), 'exclude': lambda f: f is None }})
    space_aggregated_by: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('space_aggregated_by'), 'exclude': lambda f: f is None }})
    space_aggregation: Optional[QueryTimeSeriesMetricsRequestSpaceAggregationEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('space_aggregation'), 'exclude': lambda f: f is None }})
    tigris_operation: Optional[QueryTimeSeriesMetricsRequestTigrisOperationEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tigris_operation'), 'exclude': lambda f: f is None }})
    to: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to'), 'exclude': lambda f: f is None }})
    