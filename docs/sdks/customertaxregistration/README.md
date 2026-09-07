# CustomerTaxRegistration

## Overview

### Available Operations

* [upsert_customer_tax_registration_v1_customers_customer_id_tax_registrations_post](#upsert_customer_tax_registration_v1_customers_customer_id_tax_registrations_post) - Upsert customer tax registration

## upsert_customer_tax_registration_v1_customers_customer_id_tax_registrations_post

Creates or updates a customer tax registration record. If a registration already exists
    for this customer with the same tax type and country code, it will be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="upsert_customer_tax_registration_v1_customers__customer_id__tax_registrations_post" method="post" path="/v1/customers/{customer_id}/tax-registrations" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.customer_tax_registration.upsert_customer_tax_registration_v1_customers_customer_id_tax_registrations_post(customer_id="<id>", x_organization_id="org_12345", tax_id="1234567890")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The unique identifier for the organization making the request       | org_12345                                                           |
| `tax_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomerTaxRegistrationRead](../../models/customertaxregistrationread.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |