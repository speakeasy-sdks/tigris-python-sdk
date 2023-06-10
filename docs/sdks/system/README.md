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
        bearer_auth="",
    ),
)


res = s.system.get_health()

if res.health_check_response is not None:
    # handle response
```


### Response

**[operations.HealthAPIHealthResponse](../../models/operations/healthapihealthresponse.md)**


## get_server_info

Provides the information about the server. This information includes returning the server version, etc.

### Example Usage

```python
import tigris


s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.system.get_server_info()

if res.get_info_response is not None:
    # handle response
```


### Response

**[operations.ObservabilityGetInfoResponse](../../models/operations/observabilitygetinforesponse.md)**


## observability_quota_usage

Returns current namespace quota limits

### Example Usage

```python
import tigris
from tigris.models import shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.QuotaUsageRequest()

res = s.system.observability_quota_usage(req)

if res.quota_usage_response is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.QuotaUsageRequest](../../models/shared/quotausagerequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.ObservabilityQuotaUsageResponse](../../models/operations/observabilityquotausageresponse.md)**


## query_quota_limits

Returns current namespace quota limits

### Example Usage

```python
import tigris
from tigris.models import shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.QuotaLimitsRequest()

res = s.system.query_quota_limits(req)

if res.quota_limits_response is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.QuotaLimitsRequest](../../models/shared/quotalimitsrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.ObservabilityQuotaLimitsResponse](../../models/operations/observabilityquotalimitsresponse.md)**


## query_time_series_metrics

Queries time series metrics

### Example Usage

```python
import tigris
from tigris.models import shared

s = tigris.Tigris(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.QueryTimeSeriesMetricsRequest(
    additional_functions=[
        shared.AdditionalFunction(
            rollup=shared.RollupFunction(
                aggregator=shared.RollupFunctionAggregator.ROLLUP_AGGREGATOR_SUM,
                interval=63955,
            ),
        ),
        shared.AdditionalFunction(
            rollup=shared.RollupFunction(
                aggregator=shared.RollupFunctionAggregator.ROLLUP_AGGREGATOR_MIN,
                interval=485628,
            ),
        ),
        shared.AdditionalFunction(
            rollup=shared.RollupFunction(
                aggregator=shared.RollupFunctionAggregator.ROLLUP_AGGREGATOR_MIN,
                interval=977496,
            ),
        ),
    ],
    branch='quisquam',
    collection='vero',
    db='omnis',
    from_=338159,
    function=shared.QueryTimeSeriesMetricsRequestFunction.RATE,
    metric_name='delectus',
    quantile=4551.69,
    space_aggregated_by=[
        'vero',
    ],
    space_aggregation=shared.QueryTimeSeriesMetricsRequestSpaceAggregation.SUM,
    tigris_operation=shared.QueryTimeSeriesMetricsRequestTigrisOperation.READ,
    to=941378,
)

res = s.system.query_time_series_metrics(req)

if res.query_time_series_metrics_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.QueryTimeSeriesMetricsRequest](../../models/shared/querytimeseriesmetricsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ObservabilityQueryTimeSeriesMetricsResponse](../../models/operations/observabilityquerytimeseriesmetricsresponse.md)**

