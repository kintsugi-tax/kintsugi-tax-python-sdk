# Exemptions
(*exemptions*)

## Overview

### Available Operations

* [list](#list) - Get Exemptions
* [create](#create) - Create Exemption
* [get](#get) - Get Exemption By Id
* [upload_certificate](#upload_certificate) - Upload Exemption Certificate
* [get_attachments](#get_attachments) - Get Attachments For Exemption

## list

Retrieve a list of exemptions based on filters.

### Example Usage

```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.exemptions.list(security=models.GetExemptionsV1ExemptionsGetSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), x_organization_id="org_12345", search_query="John", country_code=[
        "U",
        "S",
    ], jurisdiction="CA", start_date=date.fromisoformat("2024-01-01"), end_date=date.fromisoformat("2024-01-01"), customer_id="cust_1234", transaction_id="trans_1234", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         | Example                                                                                             |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.GetExemptionsV1ExemptionsGetSecurity](../../models/getexemptionsv1exemptionsgetsecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |                                                                                                     |
| `x_organization_id`                                                                                 | *Nullable[str]*                                                                                     | :heavy_check_mark:                                                                                  | The unique identifier for the organization making the request                                       | org_12345                                                                                           |
| `search_query`                                                                                      | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Search term to filter exemptions by exemption ID, customer name, or customer email                  | John                                                                                                |
| `status_in`                                                                                         | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Filter exemptions by their status                                                                   |                                                                                                     |
| `country_code`                                                                                      | List[[models.CountryCode](../../models/countrycode.md)]                                             | :heavy_minus_sign:                                                                                  | Country code in ISO 3166-1 alpha-2 format                                                           | US                                                                                                  |
| `jurisdiction`                                                                                      | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Jurisdiction identifier                                                                             | CA                                                                                                  |
| `start_date`                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                        | :heavy_minus_sign:                                                                                  | Start date for filtering exemptions                                                                 | 2024-01-01                                                                                          |
| `end_date`                                                                                          | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                        | :heavy_minus_sign:                                                                                  | End date for filtering exemptions                                                                   | 2024-01-01                                                                                          |
| `customer_id`                                                                                       | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Customer ID to filter exemptions                                                                    | cust_1234                                                                                           |
| `transaction_id`                                                                                    | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Transaction ID to filter exemptions                                                                 | trans_1234                                                                                          |
| `order_by`                                                                                          | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Fields to sort by (comma-separated)                                                                 |                                                                                                     |
| `page`                                                                                              | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | Page number                                                                                         |                                                                                                     |
| `size`                                                                                              | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | Page size                                                                                           |                                                                                                     |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |                                                                                                     |

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

```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.exemptions.create(security=models.CreateExemptionV1ExemptionsPostSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), x_organization_id="org_12345", exemption_type=models.ExemptionType.WHOLESALE, start_date=date.fromisoformat("2024-01-01"), customer_id="cust_001", fein="12-3456789", sales_tax_id="ST-98765", status=models.ExemptionStatus.ACTIVE, jurisdiction="CA", country_code=models.CountryCodeEnum.US, end_date=date.fromisoformat("2026-01-01"), transaction_id="txn_123", reseller=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                | [models.CreateExemptionV1ExemptionsPostSecurity](../../models/createexemptionv1exemptionspostsecurity.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |                                                                                                           |
| `x_organization_id`                                                                                       | *Nullable[str]*                                                                                           | :heavy_check_mark:                                                                                        | The unique identifier for the organization making the request                                             | org_12345                                                                                                 |
| `exemption_type`                                                                                          | [models.ExemptionType](../../models/exemptiontype.md)                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |                                                                                                           |
| `start_date`                                                                                              | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                              | :heavy_check_mark:                                                                                        | Start date for the exemption validity period (YYYY-MM-DD format)                                          |                                                                                                           |
| `customer_id`                                                                                             | *str*                                                                                                     | :heavy_check_mark:                                                                                        | Unique identifier for the customer associated with the exemption                                          |                                                                                                           |
| `fein`                                                                                                    | *str*                                                                                                     | :heavy_check_mark:                                                                                        | Federal Employer Identification Number                                                                    |                                                                                                           |
| `sales_tax_id`                                                                                            | *str*                                                                                                     | :heavy_check_mark:                                                                                        | Sales tax ID for the exemption                                                                            |                                                                                                           |
| `status`                                                                                                  | [models.ExemptionStatus](../../models/exemptionstatus.md)                                                 | :heavy_check_mark:                                                                                        | N/A                                                                                                       |                                                                                                           |
| `jurisdiction`                                                                                            | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | The jurisdiction identifier for the exemption                                                             |                                                                                                           |
| `country_code`                                                                                            | [OptionalNullable[models.CountryCodeEnum]](../../models/countrycodeenum.md)                               | :heavy_minus_sign:                                                                                        | Country code in ISO 3166-1 alpha-2 format (e.g., 'US')                                                    |                                                                                                           |
| `end_date`                                                                                                | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                              | :heavy_minus_sign:                                                                                        | End date for the exemption validity period (YYYY-MM-DD format)                                            |                                                                                                           |
| `transaction_id`                                                                                          | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | Unique identifier for the transaction, if applicable                                                      |                                                                                                           |
| `reseller`                                                                                                | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | Indicates whether the exemption is for a reseller                                                         |                                                                                                           |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

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

```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.exemptions.get(security=models.GetExemptionByIDV1ExemptionsExemptionIDGetSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), exemption_id="<id>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     | Example                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                      | [models.GetExemptionByIDV1ExemptionsExemptionIDGetSecurity](../../models/getexemptionbyidv1exemptionsexemptionidgetsecurity.md) | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |                                                                                                                                 |
| `exemption_id`                                                                                                                  | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | The unique identifier for the exemption being retrieved.                                                                        |                                                                                                                                 |
| `x_organization_id`                                                                                                             | *Nullable[str]*                                                                                                                 | :heavy_check_mark:                                                                                                              | The unique identifier for the organization making the request                                                                   | org_12345                                                                                                                       |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |                                                                                                                                 |

### Response

**[models.BackendSrcExemptionsModelsExemptionRead](../../models/backendsrcexemptionsmodelsexemptionread.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.ErrorResponse                                        | 404                                                         | application/json                                            |
| errors.BackendSrcExemptionsResponsesValidationErrorResponse | 422                                                         | application/json                                            |
| errors.ErrorResponse                                        | 500                                                         | application/json                                            |
| errors.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## upload_certificate

The Upload Exemption Certificate API allows you
    to upload a file attachment (e.g., exemption certificate) for a specific exemption.
    This is primarily used to associate supporting documents with an exemption record
    to ensure compliance and facilitate verification.

### Example Usage

```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.exemptions.upload_certificate(security=models.UploadExemptionCertificateV1ExemptionsExemptionIDAttachmentsPostSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), exemption_id="<id>", x_organization_id="org_12345", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 | Example                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                  | [models.UploadExemptionCertificateV1ExemptionsExemptionIDAttachmentsPostSecurity](../../models/uploadexemptioncertificatev1exemptionsexemptionidattachmentspostsecurity.md) | :heavy_check_mark:                                                                                                                                                          | N/A                                                                                                                                                                         |                                                                                                                                                                             |
| `exemption_id`                                                                                                                                                              | *str*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The unique identifier for the exemption to which the attachment will be associated.                                                                                         |                                                                                                                                                                             |
| `x_organization_id`                                                                                                                                                         | *Nullable[str]*                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                          | The unique identifier for the organization making the request                                                                                                               | org_12345                                                                                                                                                                   |
| `file`                                                                                                                                                                      | [models.File](../../models/file.md)                                                                                                                                         | :heavy_check_mark:                                                                                                                                                          | The file to be uploaded. Supported format: PDF. Max size: 10 MB.                                                                                                            |                                                                                                                                                                             |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |                                                                                                                                                                             |

### Response

**[models.AttachmentRead](../../models/attachmentread.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.ErrorResponse                                        | 401                                                         | application/json                                            |
| errors.BackendSrcExemptionsResponsesValidationErrorResponse | 422                                                         | application/json                                            |
| errors.ErrorResponse                                        | 500                                                         | application/json                                            |
| errors.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## get_attachments

The Get Attachments for Exemption API retrieves all
    attachments associated with a specific exemption.
    This is used to view and manage supporting documents
    like exemption certificates uploaded for a particular exemption record.

### Example Usage

```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.exemptions.get_attachments(security=models.GetAttachmentsForExemptionV1ExemptionsExemptionIDAttachmentsGetSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), exemption_id="<id>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                 | Type                                                                                                                                                                      | Required                                                                                                                                                                  | Description                                                                                                                                                               | Example                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                | [models.GetAttachmentsForExemptionV1ExemptionsExemptionIDAttachmentsGetSecurity](../../models/getattachmentsforexemptionv1exemptionsexemptionidattachmentsgetsecurity.md) | :heavy_check_mark:                                                                                                                                                        | N/A                                                                                                                                                                       |                                                                                                                                                                           |
| `exemption_id`                                                                                                                                                            | *str*                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                        | The unique identifier for the exemption<br/>        whose attachments are being retrieved.                                                                                |                                                                                                                                                                           |
| `x_organization_id`                                                                                                                                                       | *Nullable[str]*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                        | The unique identifier for the organization making the request                                                                                                             | org_12345                                                                                                                                                                 |
| `retries`                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                          | :heavy_minus_sign:                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                       |                                                                                                                                                                           |

### Response

**[List[models.AttachmentRead]](../../models/.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.ErrorResponse                                        | 401                                                         | application/json                                            |
| errors.BackendSrcExemptionsResponsesValidationErrorResponse | 422                                                         | application/json                                            |
| errors.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |