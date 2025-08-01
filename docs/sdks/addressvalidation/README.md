# AddressValidation
(*address_validation*)

## Overview

### Available Operations

* [search](#search) - Search
* [suggestions](#suggestions) - Suggestions

## search

This API validates and enriches address information
    submitted by the user. It ensures that the address is standardized, accurate,
    and compliant with geographical and postal standards.
    The API also adds additional fields, such as county, when possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="search_v1_address_validation_search_post" method="post" path="/v1/address_validation/search" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK() as sdk:

    res = sdk.address_validation.search(security=models.SearchV1AddressValidationSearchPostSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), phone="555-123-4567", street_1="1600 Amphitheatre Parkway", street_2="Building 40", city="Mountain View", county="Santa Clara", state="CA", postal_code="94043", country=models.CountryCodeEnum.US, full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                        | [models.SearchV1AddressValidationSearchPostSecurity](../../models/searchv1addressvalidationsearchpostsecurity.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `phone`                                                                                                           | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | Phone number associated with the address.                                                                         |
| `street_1`                                                                                                        | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | Primary street address.                                                                                           |
| `street_2`                                                                                                        | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | Additional street address details, such as an apartment or suite number.                                          |
| `city`                                                                                                            | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | City where the customer resides.                                                                                  |
| `county`                                                                                                          | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | County or district of the customer.                                                                               |
| `state`                                                                                                           | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | State or province of the customer.                                                                                |
| `postal_code`                                                                                                     | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | ZIP or Postal code of the customer.                                                                               |
| `country`                                                                                                         | [Optional[models.CountryCodeEnum]](../../models/countrycodeenum.md)                                               | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `full_address`                                                                                                    | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | Complete address string of the customer, which can be used as an alternative to individual fields.                |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[List[models.AddressSearchResponse]](../../models/.md)**

### Errors

| Error Type                                                         | Status Code                                                        | Content Type                                                       |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| errors.ErrorResponse                                               | 401                                                                | application/json                                                   |
| errors.BackendSrcAddressValidationResponsesValidationErrorResponse | 422                                                                | application/json                                                   |
| errors.ErrorResponse                                               | 500                                                                | application/json                                                   |
| errors.APIError                                                    | 4XX, 5XX                                                           | \*/\*                                                              |

## suggestions

This API endpoint provides address suggestions based on
    partial input data. It helps users auto-complete and validate addresses efficiently
    by returning a list of suggested addresses that match the input criteria.
    This improves accuracy, increases speed, reduces errors,
    and streamlines the data entry process.

### Example Usage

<!-- UsageSnippet language="python" operationID="suggestions_v1_address_validation_suggestions_post" method="post" path="/v1/address_validation/suggestions" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.address_validation.suggestions(line1="1600 Amphitheatre Parkway", line2="", line3="", city="Mountain View", state="CA", country="US", postal_code="94043", id=215, county="", full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `line1`                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | Primary address line, such as street name and number                                                                                                                                                                                  |
| `line2`                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | Additional address details, such as an apartment or suite number                                                                                                                                                                      |
| `line3`                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | Additional address details for complex addresses                                                                                                                                                                                      |
| `city`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | The city or town name for the address                                                                                                                                                                                                 |
| `state`                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | State, province, or region of the address                                                                                                                                                                                             |
| `country`                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | Country code in ISO 3166-1 alpha-2 format (e.g., 'US' for the United States).<br/>        Defaults to 'US'.<br/>        should not be empty. Not validating here as the validation<br/>        structure can be different for different providers |
| `postal_code`                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | ZIP or postal code for the address. Can be empty for some locales.<br/>        Not validating here as the validation structure can be different for different providers                                                               |
| `id`                                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | Unique identifier for the request, if applicable                                                                                                                                                                                      |
| `county`                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | County or district name for the address                                                                                                                                                                                               |
| `full_address`                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | A complete address string that can be used as an alternative to providing individual fields.                                                                                                                                          |
| `retries`                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                   |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                                                         | Status Code                                                        | Content Type                                                       |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| errors.ErrorResponse                                               | 401                                                                | application/json                                                   |
| errors.BackendSrcAddressValidationResponsesValidationErrorResponse | 422                                                                | application/json                                                   |
| errors.ErrorResponse                                               | 500                                                                | application/json                                                   |
| errors.APIError                                                    | 4XX, 5XX                                                           | \*/\*                                                              |