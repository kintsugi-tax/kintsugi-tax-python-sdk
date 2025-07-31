# Filings
(*filings*)

## Overview

### Available Operations

* [get_all](#get_all) - Get Filings
* [get](#get) - Get Filing By Id
* [get_by_registration_id](#get_by_registration_id) - Get Filings By Registration Id

## get_all

The Get Filings API retrieves a paginated list of filings based on
    filters such as dates, jurisdiction, Country, status, etc. This helps track
    and manage tax filings efficiently across multiple jurisdictions.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_filings_v1_filings_get" method="get" path="/v1/filings" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.filings.get_all(status_in="FILED,FILING,UNFILED", start_date="2024-01-01", end_date="2024-12-31", date_filed_gte="2024-01-01", date_filed_lte="2024-12-31", order_by="status,start_date,end_date,amount", state_code="CA", country_code=[

    ], page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `status_in`                                                             | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Filter filings by status                                                | FILED,FILING,UNFILED                                                    |
| `start_date`                                                            | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Filter filings with a start date greater than or equal to this date.    | 2024-01-01                                                              |
| `end_date`                                                              | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Filter filings with an end date less than or equal to this date.        | 2024-12-31                                                              |
| `date_filed_gte`                                                        | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Filter filings filed on or after this date.                             | 2024-01-01                                                              |
| `date_filed_lte`                                                        | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Filter filings filed on or before this date.                            | 2024-12-31                                                              |
| `order_by`                                                              | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Comma-separated list of fields to sort the results.                     | status,start_date,end_date,amount                                       |
| `state_code`                                                            | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Filter filings by state code (e.g., CA for California).                 | CA                                                                      |
| `country_code`                                                          | List[[models.CountryCodeEnum](../../models/countrycodeenum.md)]         | :heavy_minus_sign:                                                      | Filter filings by country code in ISO 3166-1 alpha-2 format (e.g., US). | US                                                                      |
| `page`                                                                  | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Page number                                                             |                                                                         |
| `size`                                                                  | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Page size                                                               |                                                                         |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |

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
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.filings.get(filing_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filing_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the filing to retrieve.                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FilingDetailsRead](../../models/filingdetailsread.md)**

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
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.filings.get_by_registration_id(registration_id="<id>", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `registration_id`                                                           | *str*                                                                       | :heavy_check_mark:                                                          | Unique identifier for the registration<br/>        associated with the filings. |
| `page`                                                                      | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | Page number                                                                 |
| `size`                                                                      | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | Page size                                                                   |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.PageFilingRead](../../models/pagefilingread.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| errors.ErrorResponse                                     | 401, 404                                                 | application/json                                         |
| errors.BackendSrcFilingsResponsesValidationErrorResponse | 422                                                      | application/json                                         |
| errors.ErrorResponse                                     | 500                                                      | application/json                                         |
| errors.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |