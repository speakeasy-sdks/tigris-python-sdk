# system

## Overview

The Observability section has APIs that provides full visibility into the health, metrics, and monitoring of the Server.

### Available Operations

* [get_health](#get_health) - Health Check
* [get_server_info](#get_server_info) - Information about the server
* [observability_quota_usage](#observability_quota_usage) - Queries current namespace quota usage
* [query_quota_limits](#query_quota_limits) - Queries current namespace quota limits
* [query_time_series_metrics](#query_time_series_metrics) - Queries time series metrics

## get_health

This endpoint can be used to check the liveness of the server.

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.system.get_health()

if res.health_check_response is not None:
    # handle response
```

## get_server_info

Provides the information about the server. This information includes returning the server version, etc.

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.system.get_server_info()

if res.get_info_response is not None:
    # handle response
```

## observability_quota_usage

Returns current namespace quota limits

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = {
    "libero": 'illum',
    "soluta": 'accusantium',
}

res = s.system.observability_quota_usage(req)

if res.quota_usage_response is not None:
    # handle response
```

## query_quota_limits

Returns current namespace quota limits

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = {
    "sapiente": 'dicta',
    "ullam": 'reprehenderit',
}

res = s.system.query_quota_limits(req)

if res.quota_limits_response is not None:
    # handle response
```

## query_time_series_metrics

Queries time series metrics

### Example Usage

```python
import tigris
from tigris.models import shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.QueryTimeSeriesMetricsRequest(
    additional_functions=[
        shared.AdditionalFunction(
            rollup=shared.RollupFunction(
                aggregator=shared.RollupFunctionAggregatorEnum.ROLLUP_AGGREGATOR_COUNT,
                interval=16328,
            ),
        ),
        shared.AdditionalFunction(
            rollup=shared.RollupFunction(
                aggregator=shared.RollupFunctionAggregatorEnum.ROLLUP_AGGREGATOR_MIN,
                interval=185232,
            ),
        ),
    ],
    branch='quibusdam',
    collection='ex',
    db='deleniti',
    from_=929292,
    function=shared.QueryTimeSeriesMetricsRequestFunctionEnum.NONE,
    metric_name='architecto',
    quantile=6091.78,
    space_aggregated_by=[
        'quasi',
        'at',
        'et',
        'voluptate',
    ],
    space_aggregation=shared.QueryTimeSeriesMetricsRequestSpaceAggregationEnum.AVG,
    tigris_operation=shared.QueryTimeSeriesMetricsRequestTigrisOperationEnum.READ,
    to=86532,
)

res = s.system.query_time_series_metrics(req)

if res.query_time_series_metrics_response is not None:
    # handle response
```
