# Customers
(*customers*)

## Overview

### Available Operations

* [list](#list) - Get Customers
* [create](#create) - Create Customer
* [get](#get) - Get Customer By Id
* [update](#update) - Update Customer
* [get_by_external_id](#get_by_external_id) - Get Customer By External Id
* [get_transactions](#get_transactions) - Get Transactions By Customer Id
* [create_transaction](#create_transaction) - Create Transaction By Customer Id

## list

The Get Customers API retrieves
    a paginated list of customers based on specified filters.
    This API allows searching, filtering by country and state, and sorting the results.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_customers_v1" method="get" path="/v1/customers" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.customers.list(search_query="John", country=[

    ], state="CA", source_in="SHOPIFY,API", order_by="created_at,street_1,street_2,city,state,postal_code,country,status", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_query`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search term to filter customers by name or other details            | John                                                                |
| `country`                                                           | List[[models.CountryCodeEnum](../../models/countrycodeenum.md)]     | :heavy_minus_sign:                                                  | Country code in ISO 3166-1 alpha-2 format (e.g., 'US')              | US                                                                  |
| `state`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | State or province code to filter customers                          | CA                                                                  |
| `source_in`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter customers by source (comma-separated)                        | SHOPIFY,API                                                         |
| `order_by`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Comma-separated list of fields to sort results by.                  | created_at,street_1,street_2,city,state,postal_code,country,status  |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number                                                         |                                                                     |
| `size`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page size                                                           |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PageCustomerRead](../../models/pagecustomerread.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| errors.ErrorResponse                                       | 401, 404                                                   | application/json                                           |
| errors.BackendSrcCustomersResponsesValidationErrorResponse | 422                                                        | application/json                                           |
| errors.ErrorResponse                                       | 500                                                        | application/json                                           |
| errors.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## create

The Create Customer API enables the creation of a new customer record with essential
details like name, contact information, and address, along with optional metadata.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_customer_v1_customers_post" method="post" path="/v1/customers" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.customers.create(phone="987-654-3210", street_1="456 Elm St", street_2="Suite 202", city="Metropolis", county="Wayne", state="NY", postal_code="10001", country=models.CountryCodeEnum.US, name="Jane Smith", external_id="cust_002", status=models.StatusEnum.ARCHIVED, email="jane.smith@example.com", source=models.SourceEnum.SHOPIFY, address_status=models.AddressStatus.PARTIALLY_VERIFIED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `phone`                                                                                            | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Customer's phone number                                                                            |
| `street_1`                                                                                         | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Primary street address.                                                                            |
| `street_2`                                                                                         | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Additional street address details, such as an apartment or suite number.                           |
| `city`                                                                                             | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | City where the customer resides.                                                                   |
| `county`                                                                                           | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | County or district of the customer.                                                                |
| `state`                                                                                            | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | State or province of the customer.                                                                 |
| `postal_code`                                                                                      | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | ZIP or Postal code of the customer.                                                                |
| `country`                                                                                          | [Optional[models.CountryCodeEnum]](../../models/countrycodeenum.md)                                | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `full_address`                                                                                     | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Complete address string of the customer, which can be used as an alternative to individual fields. |
| `name`                                                                                             | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Name of the customer.                                                                              |
| `external_id`                                                                                      | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | External identifier associated with the customer.                                                  |
| `status`                                                                                           | [Optional[models.StatusEnum]](../../models/statusenum.md)                                          | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `email`                                                                                            | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Customer's email address                                                                           |
| `source`                                                                                           | [Optional[models.SourceEnum]](../../models/sourceenum.md)                                          | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `connection_id`                                                                                    | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Identifier for the connection source, if applicable.                                               |
| `address_status`                                                                                   | [Optional[models.AddressStatus]](../../models/addressstatus.md)                                    | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `registration_number`                                                                              | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Registration number of the customer.                                                               |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[models.CustomerRead](../../models/customerread.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| errors.ErrorResponse                                       | 401, 404                                                   | application/json                                           |
| errors.BackendSrcCustomersResponsesValidationErrorResponse | 422                                                        | application/json                                           |
| errors.ErrorResponse                                       | 500                                                        | application/json                                           |
| errors.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## get

The Get Customer By ID API retrieves the details of a single customer
    using their unique identifier. It returns customer-specific data,
    including contact information, address, name and metadata, etc.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_customer_by_id_v1_customers__customer_id__get" method="get" path="/v1/customers/{customer_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.customers.get(customer_id="cust_abc123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the customer                                   | cust_abc123                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomerRead](../../models/customerread.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

The Update Customer API allows you to modify an existing customer's
    information using their unique identifier,
    enabling updates to their details as needed.

### Example Usage

<!-- UsageSnippet language="python" operationID="update_customer_v1_customers__customer_id__put" method="put" path="/v1/customers/{customer_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.customers.update(customer_id="<id>", phone="987-654-3210", street_1="456 Elm St", street_2="Suite 202", city="Metropolis", county="Wayne", state="NY", postal_code="10001", country=models.CountryCodeEnum.US, full_address="456 Elm St, Suite 202, Metropolis, NY 10001, US", name="Jane Smith", status=models.StatusEnum.ACTIVE, email="john.doe@example.com", source=models.SourceEnum.SHOPIFY, address_status=models.AddressStatus.VERIFIED, external_id="cust_002")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `customer_id`                                                                                      | *str*                                                                                              | :heavy_check_mark:                                                                                 | Unique identifier of the customer to be retrieved.                                                 |
| `phone`                                                                                            | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Phone number associated with the customer.                                                         |
| `street_1`                                                                                         | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Primary street address.                                                                            |
| `street_2`                                                                                         | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Additional street address details, such as an apartment or suite number.                           |
| `city`                                                                                             | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | City where the customer resides.                                                                   |
| `county`                                                                                           | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | County or district of the customer.                                                                |
| `state`                                                                                            | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | State or province of the customer.                                                                 |
| `postal_code`                                                                                      | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | ZIP or Postal code of the customer.                                                                |
| `country`                                                                                          | [Optional[models.CountryCodeEnum]](../../models/countrycodeenum.md)                                | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `full_address`                                                                                     | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Complete address string of the customer, which can be used as an alternative to individual fields. |
| `name`                                                                                             | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Name of the customer.                                                                              |
| `status`                                                                                           | [Optional[models.StatusEnum]](../../models/statusenum.md)                                          | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `email`                                                                                            | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Email address of the customer.                                                                     |
| `source`                                                                                           | [Optional[models.SourceEnum]](../../models/sourceenum.md)                                          | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `address_status`                                                                                   | [Optional[models.AddressStatus]](../../models/addressstatus.md)                                    | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `external_id`                                                                                      | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | External identifier associated with the customer                                                   |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[models.CustomerRead](../../models/customerread.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| errors.ErrorResponse                                       | 401, 404                                                   | application/json                                           |
| errors.BackendSrcCustomersResponsesValidationErrorResponse | 422                                                        | application/json                                           |
| errors.ErrorResponse                                       | 500                                                        | application/json                                           |
| errors.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## get_by_external_id

The Get Customer By External ID API retrieves the details of a single customer using
their external identifier. This endpoint is useful for accessing customer data when only
an external ID is available.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_customer_by_external_id_v1_customers_external__external_id__get" method="get" path="/v1/customers/external/{external_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.customers.get_by_external_id(external_id="external_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `external_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The external identifier of the customer to retrieve.                | external_12345                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomerRead](../../models/customerread.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_transactions

Get a list of transactions for a customer by their unique ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_transactions_by_customer_id_v1_customers__customer_id__transactions_get" method="get" path="/v1/customers/{customer_id}/transactions" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.customers.get_transactions(customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.TransactionRead]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## create_transaction

Create a new transaction for a specific customer.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_transaction_by_customer_id_v1_customers__customer_id__transactions_post" method="post" path="/v1/customers/{customer_id}/transactions" -->
```python
from kintsugi_tax_platform_sdk import SDK, models
from kintsugi_tax_platform_sdk.utils import parse_datetime


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.customers.create_transaction(customer_id_param="<value>", organization_id="<id>", external_id="<id>", date_=parse_datetime("2023-02-16T04:36:50.697Z"), addresses=[], transaction_items=[
        models.TransactionItemCreateUpdate(
            organization_id="<id>",
            date_=parse_datetime("2024-05-13T04:49:24.946Z"),
            external_product_id="<id>",
            quantity=1,
            amount=0,
            tax_amount_imported=0,
            tax_rate_imported=0,
            tax_amount_calculated=0,
            tax_rate_calculated=0,
            taxable_amount=0,
        ),
    ], total_amount=0, marketplace=False, total_tax_amount_imported=0, tax_rate_imported=0, total_tax_amount_calculated=0, tax_rate_calculated=0, total_tax_liability_amount=0, taxable_amount=0, locked=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                         | Type                                                                                                                                                                                                              | Required                                                                                                                                                                                                          | Description                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer_id_param`                                                                                                                                                                                               | *str*                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `organization_id`                                                                                                                                                                                                 | *str*                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                | Unique identifier of the organization.                                                                                                                                                                            |
| `external_id`                                                                                                                                                                                                     | *str*                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                | External identifier of the transaction.                                                                                                                                                                           |
| `date_`                                                                                                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                | Transaction date and time                                                                                                                                                                                         |
| `addresses`                                                                                                                                                                                                       | List[[models.TransactionAddressBuilder](../../models/transactionaddressbuilder.md)]                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `transaction_items`                                                                                                                                                                                               | List[[models.TransactionItemCreateUpdate](../../models/transactionitemcreateupdate.md)]                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `requires_exemption`                                                                                                                                                                                              | [Optional[models.ExemptionRequired]](../../models/exemptionrequired.md)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `shop_date`                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Transaction date in the shop's local timezone                                                                                                                                                                     |
| `shop_date_tz`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Timezone of the shop                                                                                                                                                                                              |
| `status`                                                                                                                                                                                                          | [Optional[models.TransactionStatusEnum]](../../models/transactionstatusenum.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `description`                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Description of the transaction.                                                                                                                                                                                   |
| `refund_status`                                                                                                                                                                                                   | [Optional[models.TransactionRefundStatus]](../../models/transactionrefundstatus.md)                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                | Shopify has 2 order statuses for refund case: refunded and partially_refunded<br/>If the given order has different status from these 2, we will set the<br/>transaction's refund_status to PARTIALLY_REFUNDED by default. |
| `total_amount`                                                                                                                                                                                                    | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Total amount of the transaction.                                                                                                                                                                                  |
| `customer_id`                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Unique identifier of the customer.                                                                                                                                                                                |
| `marketplace`                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                | Indicates if transaction is marketplace-based.                                                                                                                                                                    |
| `exempt`                                                                                                                                                                                                          | [Optional[models.TransactionExemptStatusEnum]](../../models/transactionexemptstatusenum.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                | Based on transaction item exempt status.<br/>NOT EXEMPT: None of the items are NOT EXEMPT<br/>PARTIALLY EXEMPT: At least some of the items are NOT EXEMPT<br/>FULLY_EXEMPT: All items sold in the transaction are EXEMPT |
| `exemptions`                                                                                                                                                                                                      | List[[models.Exemption](../../models/exemption.md)]                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                | List of exemptions applied (if any).                                                                                                                                                                              |
| `related_to`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Related transaction identifier.                                                                                                                                                                                   |
| `secondary_external_id`                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Secondary External Identifier.                                                                                                                                                                                    |
| `secondary_source`                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Secondary source information                                                                                                                                                                                      |
| `external_friendly_id`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Friendly identifier of the original item.                                                                                                                                                                         |
| `total_tax_amount_imported`                                                                                                                                                                                       | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Imported tax amount.                                                                                                                                                                                              |
| `tax_rate_imported`                                                                                                                                                                                               | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Imported tax rate.                                                                                                                                                                                                |
| `total_tax_amount_calculated`                                                                                                                                                                                     | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Calculated tax amount.                                                                                                                                                                                            |
| `tax_rate_calculated`                                                                                                                                                                                             | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Calculated tax rate.                                                                                                                                                                                              |
| `total_tax_liability_amount`                                                                                                                                                                                      | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Total tax liability amount.                                                                                                                                                                                       |
| `tax_liability_source`                                                                                                                                                                                            | [Optional[models.TaxLiabilitySourceEnum]](../../models/taxliabilitysourceenum.md)                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `taxable_amount`                                                                                                                                                                                                  | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Taxable amount.                                                                                                                                                                                                   |
| `currency`                                                                                                                                                                                                        | [Optional[models.CurrencyEnum]](../../models/currencyenum.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `locked`                                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                | Transaction lock status.                                                                                                                                                                                          |
| `source`                                                                                                                                                                                                          | [Optional[models.SourceEnum]](../../models/sourceenum.md)                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `connection_id`                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Connection Identifier                                                                                                                                                                                             |
| `filing_id`                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Filing identifier.                                                                                                                                                                                                |
| `city`                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | City of the transaction address.                                                                                                                                                                                  |
| `county`                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | County of the transaction address.                                                                                                                                                                                |
| `state`                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | State of the transaction address.                                                                                                                                                                                 |
| `country`                                                                                                                                                                                                         | [Optional[models.CountryCodeEnum]](../../models/countrycodeenum.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `postal_code`                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Postal code of the transaction.                                                                                                                                                                                   |
| `tax_id`                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | Tax ID associated with the transaction                                                                                                                                                                            |
| `address_status`                                                                                                                                                                                                  | [Optional[models.AddressStatus]](../../models/addressstatus.md)                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `processing_status`                                                                                                                                                                                               | [Optional[models.ProcessingStatusEnum]](../../models/processingstatusenum.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                | Our transaction state, used to determine when/if a transaction needs additional<br/>processing.                                                                                                                   |
| `destination_currency`                                                                                                                                                                                            | [Optional[models.CurrencyEnum]](../../models/currencyenum.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `converted_total_amount`                                                                                                                                                                                          | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Converted total amount.                                                                                                                                                                                           |
| `converted_total_tax_amount_imported`                                                                                                                                                                             | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Converted imported tax amount.                                                                                                                                                                                    |
| `converted_total_tax_amount_calculated`                                                                                                                                                                           | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Converted calculated tax amount.                                                                                                                                                                                  |
| `conversion_rate`                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Currency conversion rate.                                                                                                                                                                                         |
| `converted_taxable_amount`                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Converted taxable amount.                                                                                                                                                                                         |
| `converted_total_discount`                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Converted total discount amount.                                                                                                                                                                                  |
| `converted_subtotal`                                                                                                                                                                                              | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Converted subtotal amount.                                                                                                                                                                                        |
| `converted_total_tax_liability_amount`                                                                                                                                                                            | *Optional[float]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | Converted total tax liability amount.                                                                                                                                                                             |
| `customer`                                                                                                                                                                                                        | [Optional[models.CustomerCreate]](../../models/customercreate.md)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                | N/A                                                                                                                                                                                                               |
| `retries`                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                               |

### Response

**[models.TransactionRead](../../models/transactionread.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |