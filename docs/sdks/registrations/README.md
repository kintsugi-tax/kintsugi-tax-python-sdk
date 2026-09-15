# Registrations

## Overview

### Available Operations

* [get_all](#get_all) - Get registrations
* [create](#create) - Create registration
* [get_jurisdiction_specific_fields_v1_registrations_jurisdiction_specific_fields_get](#get_jurisdiction_specific_fields_v1_registrations_jurisdiction_specific_fields_get) - Get jurisdiction specific fields
* [list_registration_jurisdictions_v1_registrations_jurisdictions_get](#list_registration_jurisdictions_v1_registrations_jurisdictions_get) - List registration jurisdictions
* [get](#get) - Get registration by id
* [update](#update) - Update registration
* [upload_registration_attachment_v1_registrations_registration_id_attachments_post](#upload_registration_attachment_v1_registrations_registration_id_attachments_post) - Upload registration attachment
* [deregister](#deregister) - Deregister registration
* [get_oss_countries_for_registration_v1_registrations_registration_id_oss_countries_get](#get_oss_countries_for_registration_v1_registrations_registration_id_oss_countries_get) - Get oss countries for registration

## get_all

The Get Registrations API retrieves a
    paginated list of registrations.
    This API helps in tracking and managing registrations efficiently across multiple
    jurisdictions.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_registrations_v1_registrations_get" method="get" path="/v1/registrations" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.get_all(x_organization_id="org_12345", status_in="REGISTERED,PROCESSING,UNREGISTERED,DEREGISTERING,DEREGISTERED,CANCELLED,VALIDATING,AWAITING_CLARIFICATION,SELF_MANAGED", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              | Example                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `x_organization_id`                                                                                                                      | *Nullable[str]*                                                                                                                          | :heavy_check_mark:                                                                                                                       | The unique identifier for the organization making the request                                                                            | org_12345                                                                                                                                |
| `status_in`                                                                                                                              | *Optional[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Filter registrations by status. Multiple statuses can be passed,<br/>        separated by commas.                                        |                                                                                                                                          |
| `state_code`                                                                                                                             | *Optional[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Filter registrations by state code.                                                                                                      |                                                                                                                                          |
| `filing_frequency_in`                                                                                                                    | *Optional[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Filter registrations by filing frequency. Multiple filing frequencies<br/>        can be passed, separated by commas.                    |                                                                                                                                          |
| `country_code_in`                                                                                                                        | List[[models.CountryCodeIn](../../models/countrycodein.md)]                                                                              | :heavy_minus_sign:                                                                                                                       | Filter registrations by country code in ISO 3166-1 alpha-2 format<br/>        (e.g., US, CA).                                            |                                                                                                                                          |
| `tax_type_in`                                                                                                                            | *OptionalNullable[str]*                                                                                                                  | :heavy_minus_sign:                                                                                                                       | Filter registrations by tax type. Multiple tax types can be<br/>        passed, separated by commas (SALES_TAX, USE_TAX, SALES_AND_USE_TAX). |                                                                                                                                          |
| `order_by`                                                                                                                               | *OptionalNullable[str]*                                                                                                                  | :heavy_minus_sign:                                                                                                                       | Order results by specified fields (comma-separated)                                                                                      |                                                                                                                                          |
| `page`                                                                                                                                   | *Optional[int]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Page number                                                                                                                              |                                                                                                                                          |
| `size`                                                                                                                                   | *Optional[int]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Page size                                                                                                                                |                                                                                                                                          |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |                                                                                                                                          |

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

### Example Usage: oss

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="oss" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "OSS",
        "password_plain_text": "oss_pass_fr",
        "password_metadata_plain_text": "{\"q\":\"a\"}",
        "member_state_of_identification_code": models.CountryCodeEnum.FR,
        "imported": True,
    })

    # Handle response
    print(res)

```
### Example Usage: regular_alabama

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_alabama" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "AL",
        "state_name": "Alabama",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "alabama_user",
        "amount_fees": 100.0,
        "jurisdiction_specific_fields": {
            "registration_type": models.AlabamaRegistrationType.SALES_TAX,
            "business_name": "Acme Corp",
            "sign_on_id": "acme_sign_on",
            "access_code": "abc123",
            "third_party_password": "tp_pass",
            "mfa_completed": True,
            "sales_tax_id": "ST-AL-EXAMPLE",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_arizona

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_arizona" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id=None, request_body={
        "registration_import_type": "REGULAR",
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.TD,
        "state_code": "<value>",
        "state_name": "<value>",
        "filing_frequency": models.FilingFrequencyEnum.FOUR_MONTHLY,
        "jurisdiction_specific_fields": {
            "registration_type": models.MississippiRegistrationType.SALES_AND_USE_TAX,
            "mfa_completed": False,
            "business_name": "<value>",
            "ms_state_tax_id": "<id>",
            "ms_account_type": models.MississippiAccountType.USE_TAX_LICENSE,
            "letter_id": "<id>",
            "third_party_access_enabled": False,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_arkansas

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_arkansas" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "AR",
        "state_name": "Arkansas",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "atap_user",
        "amount_fees": 100.0,
        "password_plain_text": "atap_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.ArkansasRegistrationType.REMOTE_SELLER,
            "business_name": "Acme Corp",
            "ar_account_id": "AR-123456789",
            "zip_code": "72201",
            "last_payment_to_state": "0.00",
            "mfa_completed": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_california

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_california" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "CA",
        "state_name": "California",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "cdtfa_user",
        "amount_fees": 100.0,
        "password_plain_text": "cdtfa_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.CaliforniaRegistrationType.REMOTE_SELLER,
            "mfa_completed": True,
            "business_name": "Acme Corp",
            "sales_tax_id": "CA-1234567890",
            "cdtfa_third_party_access_security_code": "sec-code-example",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_connecticut

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_connecticut" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "CT",
        "state_name": "Connecticut",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "ct_user",
        "amount_fees": 100.0,
        "password_plain_text": "ct_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.ConnecticutRegistrationType.SALES_TAX,
            "business_name": "Test Connecticut Biz",
            "ct_tax_registration_number": "CT-REG-999",
            "registration_id": "REG-123456",
            "last_payment_to_state": "0.00",
            "mfa_completed": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_district_of_columbia

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_district_of_columbia" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "DC",
        "state_name": "District of Columbia",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "mytax_dc_user",
        "amount_fees": 100.0,
        "password_plain_text": "mytax_dc_password",
        "jurisdiction_specific_fields": {
            "mfa_completed": True,
            "registration_type": models.DistrictOfColumbiaRegistrationType.SALES_AND_USE_TAX,
            "business_name": "Acme Corp District of Columbia",
            "dc_state_tax_id": "123456789012",
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_florida

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_florida" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "FL",
        "state_name": "Florida",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "florida_user",
        "amount_fees": 100.0,
        "password_plain_text": "florida_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_TAX",
            "business_name": "Acme Corp Florida",
            "fl_certificate_number": "78-8012345678-9",
            "business_partner_number": "0001234567",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_georgia

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_georgia" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "GA",
        "state_name": "Georgia",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "gtc_user",
        "amount_fees": 100.0,
        "password_plain_text": "gtc_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.GeorgiaRegistrationType.SALES_TAX,
            "mfa_completed": True,
            "business_name": "Acme Corp Georgia",
            "sales_tax_id": "GA-ST-12345",
            "zip_code": "30301",
            "last_payment_to_state": "0.00",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_hawaii

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_hawaii" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "HI",
        "state_name": "Hawaii",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "hawaii_user",
        "amount_fees": 100.0,
        "password_plain_text": "hawaii_password",
        "jurisdiction_specific_fields": {
            "registration_type": "GENERAL_EXCISE_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp Hawaii",
            "sales_tax_id": "HI-GE-12345",
            "letter_id": "LTR-HI-001",
            "last_payment_to_state": "0.00",
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_idaho

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_idaho" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "ID",
        "state_name": "Idaho",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "idaho_user",
        "amount_fees": 100.0,
        "password_plain_text": "idaho_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.IdahoRegistrationType.SALES_TAX,
            "mfa_completed": True,
            "business_name": "Acme Corp Idaho",
            "sales_tax_id": "ID-ST-12345",
            "access_code": "tap-code-example",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_illinois

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_illinois" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "IL",
        "state_name": "Illinois",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "illinois_user",
        "amount_fees": 100.0,
        "password_plain_text": "illinois_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.IllinoisRegistrationType.SALES_AND_USE_TAX,
            "mfa_completed": True,
            "business_name": "Acme Corp Illinois",
            "illinois_account_id": "IL-9876543210",
            "last_payment_to_state": "0.00",
            "first_name": "Jane",
            "last_name": "Smith",
            "business_phone": "217-555-9876",
            "st2_activated": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_indiana

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_indiana" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "IN",
        "state_name": "Indiana",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "indiana_user",
        "amount_fees": 100.0,
        "password_plain_text": "indiana_password",
        "jurisdiction_specific_fields": {
            "mfa_completed": True,
            "registration_type": "SALES_TAX",
            "business_name": "Acme Corp Indiana",
            "in_state_tax_id": "1234567890",
            "location_id": "LOC-IND-01",
            "sales_tax_account_number": "RST-0123456789",
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_iowa

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_iowa" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "IA",
        "state_name": "Iowa",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "iowa_user",
        "amount_fees": 100.0,
        "password_plain_text": "iowa_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.IowaRegistrationType.SALES_TAX,
            "mfa_completed": True,
            "business_name": "Acme Corp Iowa",
            "ia_account_type": models.IowaAccountType.SALES_TAX_LICENSE,
            "ia_state_tax_permit_number": "IA-PERMIT-123",
            "idr_number": "1234567890",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_kansas

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_kansas" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "KS",
        "state_name": "Kansas",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "kansas_user",
        "amount_fees": 100.0,
        "password_plain_text": "kansas_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.KansasRegistrationType.RETAILERS_SALES_TAX,
            "business_name": "Acme Corp Kansas",
            "ks_state_tax_id": "KS-TAX-001",
            "access_code": "ks-access-secret",
            "third_party_access_enabled": False,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_kentucky

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_kentucky" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "KY",
        "state_name": "Kentucky",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "kentucky_user",
        "amount_fees": 100.0,
        "password_plain_text": "kentucky_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp Kentucky",
            "ky_state_tax_id": "KY-12345678",
            "registered_via_sst": False,
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_legacy

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_legacy" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "TX",
        "state_name": "Texas",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "comment": "Registering for monthly sales tax filings",
        "initial_sync": False,
        "amount_fees": 100.0,
    })

    # Handle response
    print(res)

```
### Example Usage: regular_louisiana

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_louisiana" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "LA",
        "state_name": "Louisiana",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "louisiana_user",
        "amount_fees": 100.0,
        "password_plain_text": "louisiana_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp Louisiana",
            "la_state_tax_id": "1234567890",
            "license_type": "DIRECT_MARKETER",
            "naics_code": "454110",
            "registered_email_address": "louisiana@domain.com",
            "last_payment_to_state": "0",
            "zip_code": "70802",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_maine

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_maine" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "ME",
        "state_name": "Maine",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "maine_user",
        "amount_fees": 100.0,
        "password_plain_text": "maine_password",
        "jurisdiction_specific_fields": {
            "mfa_completed": True,
            "registration_type": "SALES_AND_USE_TAX",
            "business_name": "Acme Corp Maine",
            "me_state_tax_id": "12345678",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_maryland

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_maryland" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "MD",
        "state_name": "Maryland",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "maryland_user",
        "amount_fees": 100.0,
        "password_plain_text": "maryland_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp Maryland",
            "md_state_tax_id": "MD-12345678",
            "marketplace_facilitator": False,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_massachusetts

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_massachusetts" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "MA",
        "state_name": "Massachusetts",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "massachusetts_user",
        "amount_fees": 100.0,
        "password_plain_text": "massachusetts_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.MassachusettsRegistrationType.SALES_TAX,
            "business_name": "Acme Corp Massachusetts",
            "ma_state_account_id": "MA-ACCT-001",
            "mfa_completed": True,
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_michigan

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_michigan" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id=None, request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "MI",
        "state_name": "Michigan",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "michigan_user",
        "amount_fees": 100.0,
        "password_plain_text": "michigan_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.MichiganRegistrationType.SALES_TAX,
            "business_name": "Acme Corp Michigan",
            "mi_state_tax_id": "MI-ACCT-001",
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_minnesota

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_minnesota" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "MN",
        "state_name": "Minnesota",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "minnesota_user",
        "amount_fees": 100.0,
        "password_plain_text": "minnesota_password",
        "jurisdiction_specific_fields": {
            "mfa_completed": True,
            "registration_type": "SALES_AND_USE_TAX",
            "business_name": "Acme Corp Minnesota",
            "mn_state_tax_id": "1234567",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_mississippi

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_mississippi" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "MS",
        "state_name": "Mississippi",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "mississippi_user",
        "amount_fees": 100.0,
        "password_plain_text": "mississippi_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.MississippiRegistrationType.SALES_AND_USE_TAX,
            "mfa_completed": True,
            "business_name": "Acme Corp Mississippi",
            "ms_state_tax_id": "12345678",
            "ms_account_type": models.MississippiAccountType.SALES_TAX_LICENSE,
            "letter_id": "LTR-MS-001",
            "third_party_access_enabled": False,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_missouri

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_missouri" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "MO",
        "state_name": "Missouri",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "missouri_user",
        "amount_fees": 100.0,
        "password_plain_text": "missouri_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.MissouriRegistrationType.SALES_TAX,
            "business_name": "Acme Corp Missouri",
            "mo_state_tax_id": "MO-ACCT-001",
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_nebraska

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_nebraska" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id=None, request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "NE",
        "state_name": "Nebraska",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "nebraska_user",
        "amount_fees": 100.0,
        "password_plain_text": "nebraska_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.NebraskaRegistrationType.SALES_TAX,
            "mfa_completed": True,
            "business_name": "Acme Corp Nebraska",
            "ne_user_id": "12345678",
        },
        "pin_plain_text": "12345",
    })

    # Handle response
    print(res)

```
### Example Usage: regular_nevada

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_nevada" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "NV",
        "state_name": "Nevada",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "nevada_user",
        "amount_fees": 100.0,
        "password_plain_text": "nevada_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp Nevada",
            "nv_state_tax_id": "12345678",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_new

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_new" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id=None, request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "TX",
        "state_name": "Texas",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "comment": "Registering for monthly sales tax filings",
        "initial_sync": False,
        "amount_fees": 100.0,
    })

    # Handle response
    print(res)

```
### Example Usage: regular_new_jersey

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_new_jersey" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.SZ,
        "state_code": "<value>",
        "state_name": "<value>",
        "filing_frequency": models.FilingFrequencyEnum.SEMI_MONTHLY,
        "jurisdiction_specific_fields": {
            "registration_type": models.TennesseeRegistrationType.USE_TAX,
            "mfa_completed": False,
            "business_name": "<value>",
            "tn_state_tax_id": "<id>",
            "zip_code": "43158-4492",
            "letter_id": "<id>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_new_mexico

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_new_mexico" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "NM",
        "state_name": "New Mexico",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "new_mexico_user",
        "amount_fees": 100.0,
        "password_plain_text": "new_mexico_password",
        "jurisdiction_specific_fields": {
            "registration_type": "GROSS_RECEIPTS_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp New Mexico",
            "nm_state_tax_id": "03-123456-001",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_new_york

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_new_york" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "NY",
        "state_name": "New York",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "new_york_user",
        "amount_fees": 100.0,
        "password_plain_text": "new_york_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "business_name": "Acme Corp New York",
            "ny_state_tax_id": "123456789",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_north_carolina

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_north_carolina" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "NC",
        "state_name": "North Carolina",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "north_carolina_user",
        "amount_fees": 100.0,
        "password_plain_text": "north_carolina_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "business_name": "Acme Corp North Carolina",
            "nc_state_tax_id": "NC-ACCT-001",
            "contact_name": "Jane Smith",
            "contact_email": "jane.smith@example.com",
            "contact_phone": "919-555-0100",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_north_dakota

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_north_dakota" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "ND",
        "state_name": "North Dakota",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "north_dakota_user",
        "amount_fees": 100.0,
        "password_plain_text": "north_dakota_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp North Dakota",
            "nd_state_tax_id": "ND-123456",
            "letter_id": "L9999999999",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_ohio

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_ohio" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "OH",
        "state_name": "Ohio",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "ohio_user",
        "amount_fees": 100.0,
        "password_plain_text": "ohio_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp Ohio",
            "oh_state_tax_id": "99-123456",
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_oklahoma

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_oklahoma" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "OK",
        "state_name": "Oklahoma",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "oklahoma_user",
        "amount_fees": 100.0,
        "password_plain_text": "oklahoma_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp Oklahoma",
            "ok_state_tax_id": "1234567890",
            "zip_code": "73102",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_pennsylvania

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_pennsylvania" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "PA",
        "state_name": "Pennsylvania",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "pennsylvania_user",
        "amount_fees": 100.0,
        "password_plain_text": "pennsylvania_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp Pennsylvania",
            "pa_state_tax_id": "12345678",
            "account_type": "ACCOUNT_ID",
            "account_id": "1234567890",
            "identification_type": "FEIN",
            "identification_number": "12-3456789",
            "account_validation_method": "LETTER_ID",
            "account_validation_value": "L1234567890",
            "sales_and_use_account_id": "12345678901",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_rhode_island

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_rhode_island" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "RI",
        "state_name": "Rhode Island",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "rhode_island_user",
        "amount_fees": 100.0,
        "password_plain_text": "rhode_island_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp Rhode Island",
            "ri_state_tax_id": "RI-123456",
            "ri_sales_filing_id": "123456789",
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_south_carolina

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_south_carolina" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "SC",
        "state_name": "South Carolina",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "south_carolina_user",
        "amount_fees": 100.0,
        "password_plain_text": "south_carolina_password",
        "jurisdiction_specific_fields": {
            "registration_type": "RETAIL_SALES_TAX",
            "mfa_completed": True,
            "business_name": "Acme Corp South Carolina",
            "sc_state_tax_id": "12345678",
            "sc_sid": "87654321",
            "letter_id": "L9999999999",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_south_dakota

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_south_dakota" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "SD",
        "state_name": "South Dakota",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "south_dakota_user",
        "amount_fees": 100.0,
        "password_plain_text": "south_dakota_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "business_name": "Acme Corp South Dakota",
            "sd_state_tax_id": "1234-5678-ST",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_tennessee

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_tennessee" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "TN",
        "state_name": "Tennessee",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "tennessee_user",
        "amount_fees": 100.0,
        "password_plain_text": "tennessee_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.TennesseeRegistrationType.SALES_TAX,
            "mfa_completed": True,
            "business_name": "Acme Corp Tennessee",
            "tn_state_tax_id": "TN-ACCT-001",
            "zip_code": "37201",
            "letter_id": "L1234567890",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_texas

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_texas" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "TX",
        "state_name": "Texas",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "texas_user",
        "amount_fees": 100.0,
        "password_plain_text": "texas_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.TexasRegistrationType.SALES_TAX,
            "mfa_completed": True,
            "business_name": "Acme Corp Texas",
            "texas_taxpayer_number": "12345678901",
            "webfile_number": "RT888777",
            "registered_location_number": "LOC-9",
            "registered_address": "400 W Commerce St, Dallas TX 75208",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_utah

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_utah" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id=None, request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "UT",
        "state_name": "Utah",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "utah_user",
        "amount_fees": 100.0,
        "password_plain_text": "utah_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.UtahRegistrationType.SALES_TAX,
            "mfa_completed": True,
            "business_name": "Acme Corp Utah",
            "ut_state_tax_id": "UT-9876543210",
        },
        "pin_plain_text": "654321",
    })

    # Handle response
    print(res)

```
### Example Usage: regular_vermont

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_vermont" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "VT",
        "state_name": "Vermont",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "vermont_user",
        "amount_fees": 100.0,
        "password_plain_text": "vermont_password",
        "jurisdiction_specific_fields": {
            "mfa_completed": True,
            "registration_type": models.VermontRegistrationType.SALES_TAX,
            "business_name": "Acme Corp Vermont",
            "vt_state_tax_id": "SUT-12345678",
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_virginia

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_virginia" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "VA",
        "state_name": "Virginia",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "virginia_user",
        "amount_fees": 100.0,
        "password_plain_text": "virginia_password",
        "jurisdiction_specific_fields": {
            "registration_type": models.VirginiaRegistrationType.RETAIL_SALES_TAX,
            "mfa_completed": True,
            "business_name": "Acme Corp Virginia",
            "va_state_tax_id": "54-9876543",
            "third_party_access_enabled": False,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_washington

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_washington" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "WA",
        "state_name": "Washington",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "washington_user",
        "amount_fees": 100.0,
        "password_plain_text": "washington_password",
        "jurisdiction_specific_fields": {
            "mfa_completed": True,
            "registration_type": "EXCISE_TAX",
            "business_name": "Acme Corp Washington",
            "wa_state_tax_id": "600123456",
            "litter_tax_required": False,
            "excise_account_linked": True,
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_west_virginia

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_west_virginia" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "WV",
        "state_name": "West Virginia",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "west_virginia_user",
        "amount_fees": 100.0,
        "password_plain_text": "west_virginia_password",
        "jurisdiction_specific_fields": {
            "mfa_completed": True,
            "registration_type": models.WestVirginiaRegistrationType.SALES_AND_USE_TAX,
            "business_name": "Acme Corp West Virginia",
            "wv_state_tax_id": "WV-12345678",
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_wisconsin

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_wisconsin" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "WI",
        "state_name": "Wisconsin",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "wisconsin_user",
        "amount_fees": 100.0,
        "password_plain_text": "wisconsin_password",
        "jurisdiction_specific_fields": {
            "mfa_completed": True,
            "registration_type": models.WisconsinRegistrationType.SALES_AND_USE_TAX,
            "business_name": "Acme Corp Wisconsin",
            "wi_state_tax_id": "WI-12345678",
            "third_party_access_enabled": True,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: regular_wyoming

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="regular_wyoming" -->
```python
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "REGULAR",
        "registration_date": date.fromisoformat("2025-02-01"),
        "registration_email": "example@domain.com",
        "auto_registered": True,
        "do_not_file": False,
        "country_code": models.CountryCodeEnum.US,
        "state_code": "WY",
        "state_name": "Wyoming",
        "filing_frequency": models.FilingFrequencyEnum.MONTHLY,
        "username": "wyoming_user",
        "amount_fees": 100.0,
        "password_plain_text": "wyoming_password",
        "jurisdiction_specific_fields": {
            "registration_type": "SALES_AND_USE_TAX",
            "business_name": "Acme Corp Wyoming",
            "wy_state_tax_id": "WY-ACCT-001",
        },
        "pin_plain_text": "wy-pin-1234",
    })

    # Handle response
    print(res)

```
### Example Usage: sst

<!-- UsageSnippet language="python" operationID="create_registration_v1_registrations_post" method="post" path="/v1/registrations" example="sst" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.create(x_organization_id="<id>", request_body={
        "registration_import_type": "SST",
        "password_plain_text": "sst_pass",
        "password_metadata_plain_text": "{\"q\":\"a\"}",
        "username": "sst_user",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `request_body`                                                      | [models.CreateRegistration](../../models/createregistration.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
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

## get_jurisdiction_specific_fields_v1_registrations_jurisdiction_specific_fields_get

Returns the JSON Schema and UI metadata for a state-specific registration form

### Example Usage

<!-- UsageSnippet language="python" operationID="get_jurisdiction_specific_fields_v1_registrations_jurisdiction_specific_fields_get" method="get" path="/v1/registrations/jurisdiction-specific-fields" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.get_jurisdiction_specific_fields_v1_registrations_jurisdiction_specific_fields_get(country_code="MH", state_code="<value>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `country_code`                                                      | *str*                                                               | :heavy_check_mark:                                                  | ISO 3166-1 alpha-2 country code (e.g., US).                         |                                                                     |
| `state_code`                                                        | *str*                                                               | :heavy_check_mark:                                                  | State/province code (e.g., AL, LA).                                 |                                                                     |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The unique identifier for the organization making the request       | org_12345                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.JurisdictionSpecificFieldsResponse](../../models/jurisdictionspecificfieldsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## list_registration_jurisdictions_v1_registrations_jurisdictions_get

Distinct registration jurisdictions (country + state) for filter dropdowns. Non-SST only. Default status__in matches GET /registrations (all statuses).

### Example Usage

<!-- UsageSnippet language="python" operationID="list_registration_jurisdictions_v1_registrations_jurisdictions_get" method="get" path="/v1/registrations/jurisdictions" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.list_registration_jurisdictions_v1_registrations_jurisdictions_get(x_organization_id="org_12345", status_in="REGISTERED,PROCESSING,UNREGISTERED,DEREGISTERING,DEREGISTERED,CANCELLED,VALIDATING,AWAITING_CLARIFICATION,SELF_MANAGED")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `x_organization_id`                                                          | *Nullable[str]*                                                              | :heavy_check_mark:                                                           | The unique identifier for the organization making the request                | org_12345                                                                    |
| `status_in`                                                                  | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Filter by registration status (comma-separated); same as GET /registrations. |                                                                              |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[List[models.RegistrationJurisdictionOptionRead]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

The Get Registration By ID API retrieves a single registration record
    based on its unique identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_registration_by_id_v1_registrations__registration_id__get" method="get" path="/v1/registrations/{registration_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.get(registration_id="<id>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `registration_id`                                                                      | *str*                                                                                  | :heavy_check_mark:                                                                     | The unique identifier of the<br/>                                registration to retrieve. |                                                                                        |
| `x_organization_id`                                                                    | *Nullable[str]*                                                                        | :heavy_check_mark:                                                                     | The unique identifier for the organization making the request                          | org_12345                                                                              |
| `reveal`                                                                               | *OptionalNullable[str]*                                                                | :heavy_minus_sign:                                                                     | Name of field to reveal                                                                |                                                                                        |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

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
from datetime import date
from kintsugi_tax_platform_sdk import SDK, models
from kintsugi_tax_platform_sdk.utils import parse_datetime


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.update(registration_id="<id>", x_organization_id="org_12345", registration_date=date.fromisoformat("2025-03-01"), registration_email="example@domain.com", registration_requested=parse_datetime("2025-02-18T19:43:32.684802"), auto_registered=True, registrations_regime=models.RegistrationsRegimeEnum.STANDARD, change_regime_status=models.ChangeRegimeStatusEnum.REQUESTED, do_not_file=False, username="User Name", filing_frequency=models.FilingFrequencyEnum.MONTHLY, create_filings_from=date.fromisoformat("2025-03-01"), is_approaching=False, comment="Updated registration for compliance", vda=False, create_back_filing=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `registration_id`                                                                           | *str*                                                                                       | :heavy_check_mark:                                                                          | The unique identifier of the registration to be updated.                                    |                                                                                             |
| `x_organization_id`                                                                         | *Nullable[str]*                                                                             | :heavy_check_mark:                                                                          | The unique identifier for the organization making the request                               | org_12345                                                                                   |
| `registration_date`                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                | :heavy_minus_sign:                                                                          | The date when the registration was created. Format: YYYY-MM-DD.                             |                                                                                             |
| `registration_email`                                                                        | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | Email address associated with the registration.                                             |                                                                                             |
| `registration_requested`                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                        | :heavy_minus_sign:                                                                          | Timestamp when the registration was requested.                                              |                                                                                             |
| `registration_completed`                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                        | :heavy_minus_sign:                                                                          | Timestamp when the registration was completed.                                              |                                                                                             |
| `deregistration_requested`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                        | :heavy_minus_sign:                                                                          | Timestamp when deregistration was requested.                                                |                                                                                             |
| `deregistration_completed`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                        | :heavy_minus_sign:                                                                          | Timestamp when the deregistration was completed.                                            |                                                                                             |
| `auto_registered`                                                                           | *OptionalNullable[bool]*                                                                    | :heavy_minus_sign:                                                                          | Indicates whether the registration was completed automatically.                             |                                                                                             |
| `registrations_regime`                                                                      | [OptionalNullable[models.RegistrationsRegimeEnum]](../../models/registrationsregimeenum.md) | :heavy_minus_sign:                                                                          | The tax registration regime (e.g., STANDARD, SIMPLIFIED).                                   |                                                                                             |
| `change_regime_status`                                                                      | [OptionalNullable[models.ChangeRegimeStatusEnum]](../../models/changeregimestatusenum.md)   | :heavy_minus_sign:                                                                          | N/A                                                                                         |                                                                                             |
| `third_party_enabled`                                                                       | *OptionalNullable[bool]*                                                                    | :heavy_minus_sign:                                                                          | Indicates whether third-party access is enabled for this registration.                      |                                                                                             |
| `do_not_file`                                                                               | *Optional[bool]*                                                                            | :heavy_minus_sign:                                                                          | If true, do not file for this registration (treated as False by default).                   |                                                                                             |
| `two_factor_enabled`                                                                        | *OptionalNullable[bool]*                                                                    | :heavy_minus_sign:                                                                          | Indicates whether two-factor authentication (2FA) is enabled for this registration.         |                                                                                             |
| `marked_collecting`                                                                         | *OptionalNullable[bool]*                                                                    | :heavy_minus_sign:                                                                          | Indicates whether the  registration is marked as collecting in shopify                      |                                                                                             |
| `encrypted_username`                                                                        | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | The encrypted username for the registration.                                                |                                                                                             |
| `username`                                                                                  | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | The username associated with the registration.                                              |                                                                                             |
| `filing_frequency`                                                                          | [OptionalNullable[models.FilingFrequencyEnum]](../../models/filingfrequencyenum.md)         | :heavy_minus_sign:                                                                          | The updated filing frequency (MONTHLY, QUARTERLY, etc.).                                    |                                                                                             |
| `create_filings_from`                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                | :heavy_minus_sign:                                                                          | The updated date from which filings should start (YYYY-MM-DD).                              |                                                                                             |
| `is_approaching`                                                                            | *OptionalNullable[bool]*                                                                    | :heavy_minus_sign:                                                                          | Indicates whether the registration is approaching an action (e.g., renewal).                |                                                                                             |
| `comment`                                                                                   | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | Additional notes or comments related to the registration.                                   |                                                                                             |
| `vda`                                                                                       | *OptionalNullable[bool]*                                                                    | :heavy_minus_sign:                                                                          | Indicates if the Voluntary Disclosure Agreement (VDA) applies.                              |                                                                                             |
| `tax_id`                                                                                    | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | Organization-level tax ID (e.g., VAT number, Canada Business Number).                       |                                                                                             |
| `ior_number`                                                                                | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | The Importer of Record (IOR) number for the registration.                                   |                                                                                             |
| `create_back_filing`                                                                        | *Optional[bool]*                                                                            | :heavy_minus_sign:                                                                          | Whether to also file the single period preceding the first filing period.                   |                                                                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.RegistrationRead](../../models/registrationread.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| errors.ErrorResponse                                           | 401                                                            | application/json                                               |
| errors.BackendSrcRegistrationsResponsesValidationErrorResponse | 422                                                            | application/json                                               |
| errors.ErrorResponse                                           | 500                                                            | application/json                                               |
| errors.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |

## upload_registration_attachment_v1_registrations_registration_id_attachments_post

Upload an attachment for a specific registration.

### Example Usage

<!-- UsageSnippet language="python" operationID="upload_registration_attachment_v1_registrations__registration_id__attachments_post" method="post" path="/v1/registrations/{registration_id}/attachments" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.upload_registration_attachment_v1_registrations_registration_id_attachments_post(registration_id="<id>", x_organization_id="org_12345", file="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `registration_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The unique identifier for the organization making the request       | org_12345                                                           |
| `file`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Attachment](../../models/attachment.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## deregister

Deregister an existing registration.

### Example Usage

<!-- UsageSnippet language="python" operationID="deregister_registration_v1_registrations__registration_id__deregister_post" method="post" path="/v1/registrations/{registration_id}/deregister" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.deregister(registration_id="regs_123456", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `registration_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the registration to deregister.            | regs_123456                                                         |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The unique identifier for the organization making the request       | org_12345                                                           |
| `request_id`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
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

## get_oss_countries_for_registration_v1_registrations_registration_id_oss_countries_get

Get all OSS countries for a specific registration. This endpoint returns
    a list of EU countries that are covered by the OSS registration.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_oss_countries_for_registration_v1_registrations__registration_id__oss_countries_get" method="get" path="/v1/registrations/{registration_id}/oss-countries" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.registrations.get_oss_countries_for_registration_v1_registrations_registration_id_oss_countries_get(registration_id="<id>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `registration_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the registration.                          |                                                                     |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The unique identifier for the organization making the request       | org_12345                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.OssRegistrationCountryRead]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |