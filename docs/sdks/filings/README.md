# Filings

## Overview

### Available Operations

* [get_all](#get_all) - Get filings
* [get_by_registration_id](#get_by_registration_id) - Get filings by registration id
* [get](#get) - Get filing by id
* [approve_filing_v1_filings_filing_id_approve_put](#approve_filing_v1_filings_filing_id_approve_put) - Approve filing

## get_all

The Get Filings API retrieves a paginated list of filings based on
    filters such as dates, jurisdiction, Country, status, etc. This helps track
    and manage tax filings efficiently across multiple jurisdictions.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_filings_v1_filings_get" method="get" path="/v1/filings" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.filings.get_all(x_organization_id="org_12345", status_in="FILED,FILING,UNFILED,PAUSED,CANCELLED,ISSUE,SKIPPED", start_date=date.fromisoformat("2024-01-01"), end_date=date.fromisoformat("2024-12-31"), date_filed_gte=date.fromisoformat("2024-01-01"), date_filed_lte=date.fromisoformat("2024-12-31"), order_by="status,start_date,end_date,amount", state_code="CA", country_code=[
        "U",
        "S",
    ], filing_category_in="REGULAR", tax_type_in="SALES_TAX,USE_TAX", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        | Example                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `x_organization_id`                                                                                                                | *Nullable[str]*                                                                                                                    | :heavy_check_mark:                                                                                                                 | The unique identifier for the organization making the request                                                                      | org_12345                                                                                                                          |
| `status_in`                                                                                                                        | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | Filter filings by status                                                                                                           | FILED,FILING,UNFILED,PAUSED,CANCELLED,ISSUE,SKIPPED                                                                                |
| `start_date`                                                                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                       | :heavy_minus_sign:                                                                                                                 | Filter filings with a start date greater than or equal to this date.                                                               | 2024-01-01                                                                                                                         |
| `end_date`                                                                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                       | :heavy_minus_sign:                                                                                                                 | Filter filings with an end date less than or equal to this date.                                                                   | 2024-12-31                                                                                                                         |
| `date_filed_gte`                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                       | :heavy_minus_sign:                                                                                                                 | Filter filings filed on or after this date.                                                                                        | 2024-01-01                                                                                                                         |
| `date_filed_lte`                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                       | :heavy_minus_sign:                                                                                                                 | Filter filings filed on or before this date.                                                                                       | 2024-12-31                                                                                                                         |
| `order_by`                                                                                                                         | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | Comma-separated list of fields to sort the results.                                                                                | status,start_date,end_date,amount                                                                                                  |
| `state_code`                                                                                                                       | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | Filter filings by state code (e.g., CA for California).                                                                            | CA                                                                                                                                 |
| `country_code`                                                                                                                     | List[[models.GetFilingsV1FilingsGetCountryCode](../../models/getfilingsv1filingsgetcountrycode.md)]                                | :heavy_minus_sign:                                                                                                                 | Filter filings by country code in ISO 3166-1 alpha-2 format (e.g., US).                                                            | US                                                                                                                                 |
| `filing_category_in`                                                                                                               | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | Filter filings by category (e.g., REGULAR, BACK_FILING, AMENDMENT).                                                                | REGULAR                                                                                                                            |
| `tax_type_in`                                                                                                                      | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | Filter filings by tax type. Multiple tax types can be<br/>        passed, separated by commas (SALES_TAX, USE_TAX, SALES_AND_USE_TAX). | SALES_TAX,USE_TAX                                                                                                                  |
| `page`                                                                                                                             | *Optional[int]*                                                                                                                    | :heavy_minus_sign:                                                                                                                 | Page number                                                                                                                        |                                                                                                                                    |
| `size`                                                                                                                             | *Optional[int]*                                                                                                                    | :heavy_minus_sign:                                                                                                                 | Page size                                                                                                                          |                                                                                                                                    |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |                                                                                                                                    |

### Response

**[models.PageFilingRead](../../models/pagefilingread.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| errors.ErrorResponse                                     | 401, 404                                                 | application/json                                         |
| errors.BackendSrcFilingsResponsesValidationErrorResponse | 422                                                      | application/json                                         |
| errors.ErrorResponse                                     | 500                                                      | application/json                                         |
| errors.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |

## get_by_registration_id

The Get Filings By Registration ID API
    retrieves all filings
    associated with a specific registration ID. This allows users to query detailed
    filing information tied to
    a specific registration record.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_filings_by_registration_id_v1_filings_registration__registration_id__get" method="get" path="/v1/filings/registration/{registration_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.filings.get_by_registration_id(registration_id="<id>", x_organization_id="org_12345", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `registration_id`                                                           | *str*                                                                       | :heavy_check_mark:                                                          | Unique identifier for the registration<br/>        associated with the filings. |                                                                             |
| `x_organization_id`                                                         | *Nullable[str]*                                                             | :heavy_check_mark:                                                          | The unique identifier for the organization making the request               | org_12345                                                                   |
| `page`                                                                      | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | Page number                                                                 |                                                                             |
| `size`                                                                      | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | Page size                                                                   |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.PageFilingRead](../../models/pagefilingread.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| errors.ErrorResponse                                     | 401, 404                                                 | application/json                                         |
| errors.BackendSrcFilingsResponsesValidationErrorResponse | 422                                                      | application/json                                         |
| errors.ErrorResponse                                     | 500                                                      | application/json                                         |
| errors.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |

## get

This API retrieves detailed information about a specific
    filing using its unique identifier (filing_id).

### Example Usage

<!-- UsageSnippet language="python" operationID="get_filing_by_id_v1_filings__filing_id__get" method="get" path="/v1/filings/{filing_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.filings.get(filing_id="<id>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filing_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the filing to retrieve.                       |                                                                     |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The unique identifier for the organization making the request       | org_12345                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.FilingDetailsRead](../../models/filingdetailsread.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| errors.ErrorResponse                                     | 401, 404                                                 | application/json                                         |
| errors.BackendSrcFilingsResponsesValidationErrorResponse | 422                                                      | application/json                                         |
| errors.ErrorResponse                                     | 500                                                      | application/json                                         |
| errors.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |

## approve_filing_v1_filings_filing_id_approve_put

Approve a specific filing by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="approve_filing_v1_filings__filing_id__approve_put" method="put" path="/v1/filings/{filing_id}/approve" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.filings.approve_filing_v1_filings_filing_id_approve_put(filing_id="<id>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `filing_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `x_organization_id`                                                  | *Nullable[str]*                                                      | :heavy_check_mark:                                                   | The unique identifier for the organization making the request        | org_12345                                                            |
| `back_filing_terms_id`                                               | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `back_filing_terms_accepted_at`                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.FilingRead](../../models/filingread.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |