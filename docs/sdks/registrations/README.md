# Registrations
(*registrations*)

## Overview

### Available Operations

* [get_all](#get_all) - Get Registrations
* [create](#create) - Create Registration
* [get](#get) - Get Registration By Id
* [update](#update) - Update Registration
* [deregister](#deregister) - Deregister Registration

## get_all

The Get Registrations API retrieves a
    paginated list of registrations.
    This API helps in tracking and managing registrations efficiently across multiple
    jurisdictions.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_registrations_v1_registrations_get" method="get" path="/v1/registrations" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.registrations.get_all(status_in="REGISTERED,PROCESSING,UNREGISTERED,DEREGISTERING,DEREGISTERED,VALIDATING,AWAITING_CLARIFICATION", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `status_in`                                                                                                       | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | Filter registrations by status. Multiple statuses can be passed,<br/>        separated by commas.                 |
| `state_code`                                                                                                      | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | Filter registrations by state code.                                                                               |
| `filing_frequency_in`                                                                                             | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | Filter registrations by filing frequency. Multiple filing frequencies<br/>        can be passed, separated by commas. |
| `country_code_in`                                                                                                 | List[[models.CountryCodeEnum](../../models/countrycodeenum.md)]                                                   | :heavy_minus_sign:                                                                                                | Filter registrations by country code in ISO 3166-1 alpha-2 format<br/>        (e.g., US, CA).                     |
| `order_by`                                                                                                        | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | Order results by specified fields (comma-separated)                                                               |
| `page`                                                                                                            | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | Page number                                                                                                       |
| `size`                                                                                                            | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | Page size                                                                                                         |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.PageRegistrationReadWithPassword](../../models/pageregistrationreadwithpassword.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| errors.ErrorResponse                                           | 401, 404                                                       | application/json                                               |
| errors.BackendSrcRegistrationsResponsesValidationErrorResponse | 422                                                            | application/json                                               |
| errors.ErrorResponse                                           | 500                                                            | application/json                                               |
| errors.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |

## create

The Create Registration API allows users to create a new registration
    for tracking and managing tax filings efficiently across multiple jurisdictions.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.registrations.create(request={
        "registration_import_type": "OSS",
        "imported": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateRegistration](../../models/createregistration.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RegistrationRead](../../models/registrationread.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| errors.ErrorResponse                                           | 401, 409                                                       | application/json                                               |
| errors.BackendSrcRegistrationsResponsesValidationErrorResponse | 422                                                            | application/json                                               |
| errors.ErrorResponse                                           | 500                                                            | application/json                                               |
| errors.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |

## get

The Get Registration By ID API retrieves a single registration record
    based on its unique identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_registration_by_id_v1_registrations__registration_id__get" method="get" path="/v1/registrations/{registration_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.registrations.get(registration_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `registration_id`                                                                      | *str*                                                                                  | :heavy_check_mark:                                                                     | The unique identifier of the<br/>                                registration to retrieve. |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[models.RegistrationRead](../../models/registrationread.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| errors.ErrorResponse                                           | 401                                                            | application/json                                               |
| errors.BackendSrcRegistrationsResponsesValidationErrorResponse | 422                                                            | application/json                                               |
| errors.ErrorResponse                                           | 500                                                            | application/json                                               |
| errors.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |

## update

The Update Registration API allows you to modify
    an existing registration using its unique registration_id.

### Example Usage

<!-- UsageSnippet language="python" operationID="update_registration_v1_registrations__registration_id__put" method="put" path="/v1/registrations/{registration_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.registrations.update(registration_id="<id>", registration_date="2025-03-01", registration_email="example@domain.com", registration_key="REG-123456", registration_requested="2025-02-18T19:43:32.684802", auto_registered=True, registrations_regime=models.RegistrationsRegimeEnum.STANDARD, change_regime_status=models.ChangeRegimeStatusEnum.REQUESTED, third_party_enabled=False, username="User Name", filing_frequency=models.FilingFrequencyEnum.MONTHLY, create_filings_from="2025-03-01", is_approaching=False, comment="Updated registration for compliance", vda=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `registration_id`                                                                   | *str*                                                                               | :heavy_check_mark:                                                                  | The unique identifier of the registration to be updated.                            |
| `registration_date`                                                                 | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The date when the registration was created. Format: YYYY-MM-DD.                     |
| `registration_email`                                                                | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Email address associated with the registration.                                     |
| `registration_key`                                                                  | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | A unique key assigned to the registration.                                          |
| `deregistration_key`                                                                | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | A unique key assigned for deregistration.                                           |
| `registration_requested`                                                            | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Timestamp when the registration was requested.                                      |
| `registration_completed`                                                            | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Timestamp when the registration was completed.                                      |
| `deregistration_requested`                                                          | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Timestamp when deregistration was requested.                                        |
| `deregistration_completed`                                                          | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Timestamp when the deregistration was completed.                                    |
| `auto_registered`                                                                   | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Indicates whether the registration was completed automatically.                     |
| `registrations_regime`                                                              | [Optional[models.RegistrationsRegimeEnum]](../../models/registrationsregimeenum.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `change_regime_status`                                                              | [Optional[models.ChangeRegimeStatusEnum]](../../models/changeregimestatusenum.md)   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `third_party_enabled`                                                               | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Indicates whether third-party access is enabled for this registration.              |
| `marked_collecting`                                                                 | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Indicates whether the  registration is marked as collecting in shopify              |
| `username`                                                                          | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The username associated with the registration.                                      |
| `filing_frequency`                                                                  | [Optional[models.FilingFrequencyEnum]](../../models/filingfrequencyenum.md)         | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `create_filings_from`                                                               | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The updated date from which filings should start (YYYY-MM-DD).                      |
| `is_approaching`                                                                    | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Indicates whether the registration is approaching an action (e.g., renewal).        |
| `comment`                                                                           | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Additional notes or comments related to the registration.                           |
| `vda`                                                                               | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Indicates if the Voluntary Disclosure Agreement (VDA) applies.                      |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.RegistrationRead](../../models/registrationread.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| errors.ErrorResponse                                           | 401                                                            | application/json                                               |
| errors.BackendSrcRegistrationsResponsesValidationErrorResponse | 422                                                            | application/json                                               |
| errors.ErrorResponse                                           | 500                                                            | application/json                                               |
| errors.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |

## deregister

Deregister an existing registration.

### Example Usage

<!-- UsageSnippet language="python" operationID="deregister_registration_v1_registrations__registration_id__deregister_post" method="post" path="/v1/registrations/{registration_id}/deregister" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.registrations.deregister(registration_id="regs_123456")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `registration_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the registration to deregister.            | regs_123456                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RegistrationRead](../../models/registrationread.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| errors.ErrorResponse                                           | 401                                                            | application/json                                               |
| errors.BackendSrcRegistrationsResponsesValidationErrorResponse | 422                                                            | application/json                                               |
| errors.ErrorResponse                                           | 500                                                            | application/json                                               |
| errors.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |