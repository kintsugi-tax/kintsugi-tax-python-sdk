# Exemptions

## Overview

### Available Operations

* [list](#list) - Get exemptions
* [create](#create) - Create exemption
* [get](#get) - Get exemption by id
* [list_attachments](#list_attachments) - Get attachments for exemption
* [upload_certificate](#upload_certificate) - Upload exemption certificate

## list

Retrieve a list of exemptions based on filters.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_exemptions_v1_exemptions_get" method="get" path="/v1/exemptions" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.exemptions.list(x_organization_id="org_12345", search_query="John", status_in="ACTIVE,INACTIVE,EXPIRED", country_code=[
        "U",
        "S",
    ], jurisdiction="CA", start_date=date.fromisoformat("2024-01-01"), end_date=date.fromisoformat("2024-01-01"), customer_id="cust_1234", transaction_id="trans_1234", connection_id_in="conn_abc123,conn_def456", order_by="end_date,FEIN,sales_tax_id,status", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     | Example                                                                                                         |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `x_organization_id`                                                                                             | *Nullable[str]*                                                                                                 | :heavy_check_mark:                                                                                              | The unique identifier for the organization making the request                                                   | org_12345                                                                                                       |
| `search_query`                                                                                                  | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | Search term to filter exemptions by exemption ID, customer name, or customer email                              | John                                                                                                            |
| `status_in`                                                                                                     | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | Filter exemptions by their status                                                                               |                                                                                                                 |
| `country_code`                                                                                                  | List[[models.GetExemptionsV1ExemptionsGetCountryCode](../../models/getexemptionsv1exemptionsgetcountrycode.md)] | :heavy_minus_sign:                                                                                              | Country code in ISO 3166-1 alpha-2 format                                                                       | US                                                                                                              |
| `jurisdiction`                                                                                                  | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | Jurisdiction identifier                                                                                         | CA                                                                                                              |
| `start_date`                                                                                                    | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                    | :heavy_minus_sign:                                                                                              | Start date for filtering exemptions                                                                             | 2024-01-01                                                                                                      |
| `end_date`                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                    | :heavy_minus_sign:                                                                                              | End date for filtering exemptions                                                                               | 2024-01-01                                                                                                      |
| `customer_id`                                                                                                   | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | Customer ID to filter exemptions                                                                                | cust_1234                                                                                                       |
| `transaction_id`                                                                                                | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | Transaction ID to filter exemptions                                                                             | trans_1234                                                                                                      |
| `connection_id_in`                                                                                              | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | Filter exemptions by customer connection ID (comma-separated)                                                   | conn_abc123,conn_def456                                                                                         |
| `order_by`                                                                                                      | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | Fields to sort by (comma-separated)                                                                             |                                                                                                                 |
| `page`                                                                                                          | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Page number                                                                                                     |                                                                                                                 |
| `size`                                                                                                          | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Page size                                                                                                       |                                                                                                                 |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |                                                                                                                 |

### Response

**[models.FastapiPaginationDefaultPageExemptionRead2](../../models/fastapipaginationdefaultpageexemptionread2.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.ErrorResponse                                        | 401                                                         | application/json                                            |
| errors.BackendSrcExemptionsResponsesValidationErrorResponse | 422                                                         | application/json                                            |
| errors.ErrorResponse                                        | 500                                                         | application/json                                            |
| errors.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## create

The Create Exemption API allows you to create a new exemption record.
    This includes defining details such as exemption type, jurisdiction,
    Country, State, validity dates, etc.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_exemption_v1_exemptions_post" method="post" path="/v1/exemptions" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.exemptions.create(x_organization_id="org_12345", exemption_type=models.ExemptionType.WHOLESALE, start_date=date.fromisoformat("2024-01-01"), customer_id="cust_001", fein="12-3456789", sales_tax_id="ST-98765", status=models.ExemptionStatus.ACTIVE, jurisdiction="CA", country_code=models.CountryCodeEnum.US, end_date=date.fromisoformat("2026-01-01"), transaction_id="txn_123", reseller=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `x_organization_id`                                                          | *Nullable[str]*                                                              | :heavy_check_mark:                                                           | The unique identifier for the organization making the request                | org_12345                                                                    |
| `exemption_type`                                                             | [models.ExemptionType](../../models/exemptiontype.md)                        | :heavy_check_mark:                                                           | N/A                                                                          |                                                                              |
| `start_date`                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Start date for the exemption validity period (YYYY-MM-DD format)             |                                                                              |
| `customer_id`                                                                | *str*                                                                        | :heavy_check_mark:                                                           | Unique identifier for the customer associated with the exemption             |                                                                              |
| `fein`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | Federal Employer Identification Number                                       |                                                                              |
| `sales_tax_id`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | Sales tax ID for the exemption                                               |                                                                              |
| `status`                                                                     | [models.ExemptionStatus](../../models/exemptionstatus.md)                    | :heavy_check_mark:                                                           | N/A                                                                          |                                                                              |
| `jurisdiction`                                                               | *OptionalNullable[str]*                                                      | :heavy_minus_sign:                                                           | The jurisdiction identifier for the exemption                                |                                                                              |
| `country_code`                                                               | [OptionalNullable[models.CountryCodeEnum]](../../models/countrycodeenum.md)  | :heavy_minus_sign:                                                           | Country code in ISO 3166-1 alpha-2 format (e.g., 'US')                       |                                                                              |
| `end_date`                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | End date for the exemption validity period (YYYY-MM-DD format)               |                                                                              |
| `transaction_id`                                                             | *OptionalNullable[str]*                                                      | :heavy_minus_sign:                                                           | Unique identifier for the transaction, if applicable                         |                                                                              |
| `reseller`                                                                   | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Indicates whether the exemption is for a reseller                            |                                                                              |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[models.BackendSrcExemptionsSerializersExemptionRead](../../models/backendsrcexemptionsserializersexemptionread.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.ErrorResponse                                        | 401                                                         | application/json                                            |
| errors.BackendSrcExemptionsResponsesValidationErrorResponse | 422                                                         | application/json                                            |
| errors.ErrorResponse                                        | 500                                                         | application/json                                            |
| errors.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## get

The Get Exemption By ID API retrieves a specific exemption record by
    its unique ID. This API is useful for retrieving detailed information
    about a particular exemption, including its associated
    customer, organisation id, status, etc.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_exemption_by_id_v1_exemptions__exemption_id__get" method="get" path="/v1/exemptions/{exemption_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.exemptions.get(exemption_id="<id>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `exemption_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier for the exemption being retrieved.            |                                                                     |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The unique identifier for the organization making the request       | org_12345                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.BackendSrcExemptionsSchemasExemptionExemptionRead](../../models/backendsrcexemptionsschemasexemptionexemptionread.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.ErrorResponse                                        | 404                                                         | application/json                                            |
| errors.BackendSrcExemptionsResponsesValidationErrorResponse | 422                                                         | application/json                                            |
| errors.ErrorResponse                                        | 500                                                         | application/json                                            |
| errors.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## list_attachments

The Get Attachments for Exemption API retrieves all
    attachments associated with a specific exemption.
    This is used to view and manage supporting documents
    like exemption certificates uploaded for a particular exemption record.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_attachments_for_exemption_v1_exemptions__exemption_id__attachments_get" method="get" path="/v1/exemptions/{exemption_id}/attachments" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.exemptions.list_attachments(exemption_id="<id>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `exemption_id`                                                                         | *str*                                                                                  | :heavy_check_mark:                                                                     | The unique identifier for the exemption<br/>        whose attachments are being retrieved. |                                                                                        |
| `x_organization_id`                                                                    | *Nullable[str]*                                                                        | :heavy_check_mark:                                                                     | The unique identifier for the organization making the request                          | org_12345                                                                              |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[List[models.AttachmentRead]](../../models/.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.ErrorResponse                                        | 401                                                         | application/json                                            |
| errors.BackendSrcExemptionsResponsesValidationErrorResponse | 422                                                         | application/json                                            |
| errors.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## upload_certificate

The Upload Exemption Certificate API allows you
    to upload a file attachment (e.g., exemption certificate) for a specific exemption.
    This is primarily used to associate supporting documents with an exemption record
    to ensure compliance and facilitate verification.

### Example Usage

<!-- UsageSnippet language="python" operationID="upload_exemption_certificate_v1_exemptions__exemption_id__attachments_post" method="post" path="/v1/exemptions/{exemption_id}/attachments" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.exemptions.upload_certificate(exemption_id="<id>", x_organization_id="org_12345", file=open("example.file", "rb").read().decode("utf-8"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `exemption_id`                                                                      | *str*                                                                               | :heavy_check_mark:                                                                  | The unique identifier for the exemption to which the attachment will be associated. |                                                                                     |
| `x_organization_id`                                                                 | *Nullable[str]*                                                                     | :heavy_check_mark:                                                                  | The unique identifier for the organization making the request                       | org_12345                                                                           |
| `file`                                                                              | *str*                                                                               | :heavy_check_mark:                                                                  | The file to be uploaded. Supported format: PDF. Max size: 10 MB.                    |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.AttachmentRead](../../models/attachmentread.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.ErrorResponse                                        | 401                                                         | application/json                                            |
| errors.BackendSrcExemptionsResponsesValidationErrorResponse | 422                                                         | application/json                                            |
| errors.ErrorResponse                                        | 500                                                         | application/json                                            |
| errors.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |