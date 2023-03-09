from __future__ import annotations
import dataclasses
from ..shared import metricseries as shared_metricseries
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class QueryTimeSeriesMetricsResponse:
    r"""QueryTimeSeriesMetricsResponse
    QueryTimeSeriesMetric responds with this type.
    """
    
    from_: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'exclude': lambda f: f is None }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query'), 'exclude': lambda f: f is None }})
    series: Optional[list[shared_metricseries.MetricSeries]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('series'), 'exclude': lambda f: f is None }})
    to: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to'), 'exclude': lambda f: f is None }})
    