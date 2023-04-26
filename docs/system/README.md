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
    "quasi": "a",
    "error": "sint",
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
    "possimus": "quia",
    "eveniet": "asperiores",
    "facere": "veritatis",
    "consequuntur": "quasi",
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
                aggregator="ROLLUP_AGGREGATOR_MAX",
                interval=398434,
            ),
        ),
        shared.AdditionalFunction(
            rollup=shared.RollupFunction(
                aggregator="ROLLUP_AGGREGATOR_AVG",
                interval=62713,
            ),
        ),
        shared.AdditionalFunction(
            rollup=shared.RollupFunction(
                aggregator="ROLLUP_AGGREGATOR_AVG",
                interval=424032,
            ),
        ),
    ],
    branch="in",
    collection="eius",
    db="libero",
    from_=849039,
    function="NONE",
    metric_name="accusantium",
    quantile=3069.86,
    space_aggregated_by=[
        "dicta",
        "ullam",
        "reprehenderit",
        "ullam",
    ],
    space_aggregation="MIN",
    tigris_operation="ALL",
    to=531849,
)

res = s.system.query_time_series_metrics(req)

if res.query_time_series_metrics_response is not None:
    # handle response
```
