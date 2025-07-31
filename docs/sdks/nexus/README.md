# Nexus
(*nexus*)

## Overview

### Available Operations

* [get_physical](#get_physical) - Get Physical Nexus
* [create_physical](#create_physical) - Create Physical Nexus
* [update_physical_nexus](#update_physical_nexus) - Update Physical Nexus
* [delete_physical_nexus](#delete_physical_nexus) - Delete Physical Nexus
* [get_all](#get_all) - Get Nexus For Org

## get_physical

Retrieve a paginated list of
    physical nexuses for a specific organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_physical_nexus_v1_nexus_physical_nexus_get" method="get" path="/v1/nexus/physical_nexus" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.nexus.get_physical(order_by="country_code,state_code,start_date,end_date", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `country_code`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `state_code`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `order_by`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number                                                         |
| `size`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page size                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PagePhysicalNexusRead](../../models/pagephysicalnexusread.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| errors.ErrorResponse                                   | 401, 404                                               | application/json                                       |
| errors.BackendSrcNexusResponsesValidationErrorResponse | 422                                                    | application/json                                       |
| errors.ErrorResponse                                   | 500                                                    | application/json                                       |
| errors.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |

## create_physical

The Create Physical Nexus API allows you to create a new physical
    nexus by specifying its attributes, including the location,
    start date, end date, etc.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_physical_nexus_v1_nexus_physical_nexus_post" method="post" path="/v1/nexus/physical_nexus" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.nexus.create_physical(country_code=models.CountryCodeEnum.US, state_code="CA", start_date=date.fromisoformat("2024-01-01"), category=models.PhysicalNexusCategory.PHYSICAL_BUSINESS_LOCATION, end_date="2025-01-01", external_id="ext_ABC123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `country_code`                                                                          | [models.CountryCodeEnum](../../models/countrycodeenum.md)                               | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `state_code`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | The state or province code in<br/>                            ISO 3166-2 format (e.g., CA). |
| `start_date`                                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)            | :heavy_check_mark:                                                                      | The date when the nexus became<br/>                            effective (YYYY-MM-DD).  |
| `category`                                                                              | [models.PhysicalNexusCategory](../../models/physicalnexuscategory.md)                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `end_date`                                                                              | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | The date when the<br/>                                        nexus ended, if applicable. |
| `external_id`                                                                           | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Optional<br/>                                        external identifier for the nexus. |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.PhysicalNexusRead](../../models/physicalnexusread.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| errors.ErrorResponse                                   | 401                                                    | application/json                                       |
| errors.BackendSrcNexusResponsesValidationErrorResponse | 422                                                    | application/json                                       |
| errors.ErrorResponse                                   | 500                                                    | application/json                                       |
| errors.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |

## update_physical_nexus

The Update Physical Nexus API allows you to modify the details of
    an existing physical nexus by its unique ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="update_physical_nexus_v1_nexus_physical_nexus__physical_nexus_id__put" method="put" path="/v1/nexus/physical_nexus/{physical_nexus_id}" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.nexus.update_physical_nexus(physical_nexus_id="<id>", start_date=date.fromisoformat("2024-01-01"), category=models.PhysicalNexusCategory.PHYSICAL_BUSINESS_LOCATION, end_date="2025-01-01")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `physical_nexus_id`                                                                               | *str*                                                                                             | :heavy_check_mark:                                                                                | The unique identifier of the physical<br/>                                nexus to update.        |
| `start_date`                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                      | :heavy_check_mark:                                                                                | The date when the nexus became<br/>                                effective (YYYY-MM-DD).        |
| `category`                                                                                        | [models.PhysicalNexusCategory](../../models/physicalnexuscategory.md)                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `end_date`                                                                                        | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | The date when the<br/>                                        nexus ends, if applicable (YYYY-MM-DD). |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.PhysicalNexusRead](../../models/physicalnexusread.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| errors.ErrorResponse                                   | 401, 404                                               | application/json                                       |
| errors.BackendSrcNexusResponsesValidationErrorResponse | 422                                                    | application/json                                       |
| errors.ErrorResponse                                   | 500                                                    | application/json                                       |
| errors.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |

## delete_physical_nexus

The Delete Physical Nexus API allows you to remove an existing
    physical nexus by its unique ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_physical_nexus_v1_nexus_physical_nexus__physical_nexus_id__delete" method="delete" path="/v1/nexus/physical_nexus/{physical_nexus_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.nexus.delete_physical_nexus(physical_nexus_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `physical_nexus_id`                                                                    | *str*                                                                                  | :heavy_check_mark:                                                                     | The unique identifier of the physical<br/>                                nexus to delete. |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| errors.ErrorResponse                                   | 401, 404                                               | application/json                                       |
| errors.BackendSrcNexusResponsesValidationErrorResponse | 422                                                    | application/json                                       |
| errors.ErrorResponse                                   | 500                                                    | application/json                                       |
| errors.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |

## get_all

Get a list of all nexuses for the organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_nexus_for_org_v1_nexus_get" method="get" path="/v1/nexus" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.nexus.get_all(status_in="APPROACHING,NOT_EXPOSED,PENDING_REGISTRATION,EXPOSED,APPROACHING,REGISTERED", order_by="state_code,country_code", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `status_in`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `state_code`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `country_code_in`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `order_by`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `collected_tax_nexus_met`                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number                                                         |
| `size`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page size                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PageNexusResponse](../../models/pagenexusresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |