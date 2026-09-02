# kintsugi-tax-platform-sdk

Developer-friendly & type-safe Python SDK specifically catered to leverage *kintsugi-tax-platform-sdk* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=kintsugi-tax-platform-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start Summary [summary] -->
## Summary

Kintsugi Customer API: Publicly documented Kintsugi Customer API endpoints. The source (openapi/_source/openapi-master.json) is the platform spec filtered to the documented customer surface (openapi/customer-endpoints.json); scripts/build-specs.mjs re-applies that filter here. Do not edit by hand.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [kintsugi-tax-platform-sdk](#kintsugi-tax-platform-sdk)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add kintsugi-tax-platform-sdk
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install kintsugi-tax-platform-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add kintsugi-tax-platform-sdk
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from kintsugi-tax-platform-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "kintsugi-tax-platform-sdk",
# ]
# ///

from kintsugi_tax_platform_sdk import SDK

sdk = SDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.address_validation.search(phone="555-123-4567", street_1="1600 Amphitheatre Parkway", street_2="Building 40", city="Mountain View", county="Santa Clara", state="CA", postal_code="94043", country=models.CountryCodeEnum.US, full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from kintsugi_tax_platform_sdk import SDK, models

async def main():

    async with SDK(
        api_key_header="<YOUR_API_KEY_HERE>",
    ) as sdk:

        res = await sdk.address_validation.search_async(phone="555-123-4567", street_1="1600 Amphitheatre Parkway", street_2="Building 40", city="Mountain View", county="Santa Clara", state="CA", postal_code="94043", country=models.CountryCodeEnum.US, full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name             | Type   | Scheme  |
| ---------------- | ------ | ------- |
| `api_key_header` | apiKey | API key |

To authenticate with the API the `api_key_header` parameter must be set when initializing the SDK client instance. For example:
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.address_validation.search(phone="555-123-4567", street_1="1600 Amphitheatre Parkway", street_2="Building 40", city="Mountain View", county="Santa Clara", state="CA", postal_code="94043", country=models.CountryCodeEnum.US, full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [AddressValidation](docs/sdks/addressvalidation/README.md)

* [search](docs/sdks/addressvalidation/README.md#search) - Search
* [suggestions](docs/sdks/addressvalidation/README.md#suggestions) - Suggestions

### [CustomerTaxRegistration](docs/sdks/customertaxregistration/README.md)

* [upsert_customer_tax_registration_v1_customers_customer_id_tax_registrations_post](docs/sdks/customertaxregistration/README.md#upsert_customer_tax_registration_v1_customers_customer_id_tax_registrations_post) - Upsert customer tax registration

### [Customers](docs/sdks/customers/README.md)

* [list](docs/sdks/customers/README.md#list) - Get customers
* [create](docs/sdks/customers/README.md#create) - Create customer
* [get_by_external_id](docs/sdks/customers/README.md#get_by_external_id) - Get customer by external id
* [get](docs/sdks/customers/README.md#get) - Get customer by id
* [update](docs/sdks/customers/README.md#update) - Update customer
* [get_transactions](docs/sdks/customers/README.md#get_transactions) - Get transactions by customer id
* [create_transaction](docs/sdks/customers/README.md#create_transaction) - Create transaction by customer id

### [Exemptions](docs/sdks/exemptions/README.md)

* [list](docs/sdks/exemptions/README.md#list) - Get exemptions
* [create](docs/sdks/exemptions/README.md#create) - Create exemption
* [get](docs/sdks/exemptions/README.md#get) - Get exemption by id
* [list_attachments](docs/sdks/exemptions/README.md#list_attachments) - Get attachments for exemption
* [upload_certificate](docs/sdks/exemptions/README.md#upload_certificate) - Upload exemption certificate

### [Filings](docs/sdks/filings/README.md)

* [get_all](docs/sdks/filings/README.md#get_all) - Get filings
* [get_by_registration_id](docs/sdks/filings/README.md#get_by_registration_id) - Get filings by registration id
* [get](docs/sdks/filings/README.md#get) - Get filing by id
* [approve_filing_v1_filings_filing_id_approve_put](docs/sdks/filings/README.md#approve_filing_v1_filings_filing_id_approve_put) - Approve filing

### [Nexus](docs/sdks/nexus/README.md)

* [get_all](docs/sdks/nexus/README.md#get_all) - Get nexus for org
* [get_physical](docs/sdks/nexus/README.md#get_physical) - Get physical nexus
* [create_physical](docs/sdks/nexus/README.md#create_physical) - Create physical nexus
* [get_physical_nexus_categories_v1_nexus_physical_nexus_categories_get](docs/sdks/nexus/README.md#get_physical_nexus_categories_v1_nexus_physical_nexus_categories_get) - Get physical nexus categories
* [delete_physical_nexus](docs/sdks/nexus/README.md#delete_physical_nexus) - Delete physical nexus
* [update_physical_nexus](docs/sdks/nexus/README.md#update_physical_nexus) - Update physical nexus
* [get_nexus_details_for_id_v1_nexus_nexus_id_get](docs/sdks/nexus/README.md#get_nexus_details_for_id_v1_nexus_nexus_id_get) - Get nexus details for id

### [Products](docs/sdks/products/README.md)

* [get_products_v1_products_get](docs/sdks/products/README.md#get_products_v1_products_get) - Get products
* [create_product_v1_products_post](docs/sdks/products/README.md#create_product_v1_products_post) - Create product
* [get_product_categories_v1_products_categories_get](docs/sdks/products/README.md#get_product_categories_v1_products_categories_get) - Get product categories
* [retrieve](docs/sdks/products/README.md#retrieve) - Get product by id
* [update](docs/sdks/products/README.md#update) - Update product

### [Registrations](docs/sdks/registrations/README.md)

* [get_all](docs/sdks/registrations/README.md#get_all) - Get registrations
* [create](docs/sdks/registrations/README.md#create) - Create registration
* [get_jurisdiction_specific_fields_v1_registrations_jurisdiction_specific_fields_get](docs/sdks/registrations/README.md#get_jurisdiction_specific_fields_v1_registrations_jurisdiction_specific_fields_get) - Get jurisdiction specific fields
* [list_registration_jurisdictions_v1_registrations_jurisdictions_get](docs/sdks/registrations/README.md#list_registration_jurisdictions_v1_registrations_jurisdictions_get) - List registration jurisdictions
* [get](docs/sdks/registrations/README.md#get) - Get registration by id
* [update](docs/sdks/registrations/README.md#update) - Update registration
* [upload_registration_attachment_v1_registrations_registration_id_attachments_post](docs/sdks/registrations/README.md#upload_registration_attachment_v1_registrations_registration_id_attachments_post) - Upload registration attachment
* [deregister](docs/sdks/registrations/README.md#deregister) - Deregister registration
* [get_oss_countries_for_registration_v1_registrations_registration_id_oss_countries_get](docs/sdks/registrations/README.md#get_oss_countries_for_registration_v1_registrations_registration_id_oss_countries_get) - Get oss countries for registration

### [TaxEstimation](docs/sdks/taxestimation/README.md)

* [estimate](docs/sdks/taxestimation/README.md#estimate) - Estimate tax

### [Transactions](docs/sdks/transactions/README.md)

* [list](docs/sdks/transactions/README.md#list) - Get transactions
* [create](docs/sdks/transactions/README.md#create) - Create transaction
* [archive_transaction_by_id_v1_transactions_archive_post](docs/sdks/transactions/README.md#archive_transaction_by_id_v1_transactions_archive_post) - Archive transaction by id
* [get_by_external_id](docs/sdks/transactions/README.md#get_by_external_id) - Get transaction by external id
* [get_by_filing_id](docs/sdks/transactions/README.md#get_by_filing_id) - Get transactions by filing id
* [create_credit_note](docs/sdks/transactions/README.md#create_credit_note) - Create credit note by transaction id
* [update_credit_note](docs/sdks/transactions/README.md#update_credit_note) - Update credit note by transaction id
* [get_by_id](docs/sdks/transactions/README.md#get_by_id) - Get transaction by id
* [update](docs/sdks/transactions/README.md#update) - Update transaction
* [set_transaction_tax_only_v1_transactions_transaction_id_tax_only_post](docs/sdks/transactions/README.md#set_transaction_tax_only_v1_transactions_transaction_id_tax_only_post) - Set transaction tax only

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from kintsugi_tax_platform_sdk import SDK, models
from kintsugi_tax_platform_sdk.utils import BackoffStrategy, RetryConfig


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.address_validation.search(phone="555-123-4567", street_1="1600 Amphitheatre Parkway", street_2="Building 40", city="Mountain View", county="Santa Clara", state="CA", postal_code="94043", country=models.CountryCodeEnum.US, full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from kintsugi_tax_platform_sdk import SDK, models
from kintsugi_tax_platform_sdk.utils import BackoffStrategy, RetryConfig


with SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.address_validation.search(phone="555-123-4567", street_1="1600 Amphitheatre Parkway", street_2="Building 40", city="Mountain View", county="Santa Clara", state="CA", postal_code="94043", country=models.CountryCodeEnum.US, full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SDKError`](./src/kintsugi_tax_platform_sdk/errors/sdkerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from kintsugi_tax_platform_sdk import SDK, errors, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:
    res = None
    try:

        res = sdk.address_validation.search(phone="555-123-4567", street_1="1600 Amphitheatre Parkway", street_2="Building 40", city="Mountain View", county="Santa Clara", state="CA", postal_code="94043", country=models.CountryCodeEnum.US, full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043")

        # Handle response
        print(res)


    except errors.SDKError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.ErrorResponse):
            print(e.data.detail)  # str
```

### Error Classes
**Primary error:**
* [`SDKError`](./src/kintsugi_tax_platform_sdk/errors/sdkerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (16)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SDKError`](./src/kintsugi_tax_platform_sdk/errors/sdkerror.py)**:
* [`ErrorResponse`](./src/kintsugi_tax_platform_sdk/errors/errorresponse.py): Applicable to 33 of 51 methods.*
* [`HTTPValidationError`](./src/kintsugi_tax_platform_sdk/errors/httpvalidationerror.py): Validation Error. Status code `422`. Applicable to 18 of 51 methods.*
* [`BackendSrcExemptionsResponsesValidationErrorResponse`](./src/kintsugi_tax_platform_sdk/errors/backendsrcexemptionsresponsesvalidationerrorresponse.py): Validation issues, such as missing required fields or invalid field values. Status code `422`. Applicable to 5 of 51 methods.*
* [`BackendSrcProductsSchemasResponsesValidationErrorResponse`](./src/kintsugi_tax_platform_sdk/errors/backendsrcproductsschemasresponsesvalidationerrorresponse.py): Validation error. Status code `422`. Applicable to 5 of 51 methods.*
* [`BackendSrcRegistrationsResponsesValidationErrorResponse`](./src/kintsugi_tax_platform_sdk/errors/backendsrcregistrationsresponsesvalidationerrorresponse.py): Validation error. Status code `422`. Applicable to 5 of 51 methods.*
* [`BackendSrcTransactionsResponsesValidationErrorResponse`](./src/kintsugi_tax_platform_sdk/errors/backendsrctransactionsresponsesvalidationerrorresponse.py): Status code `422`. Applicable to 5 of 51 methods.*
* [`BackendSrcNexusResponsesValidationErrorResponse`](./src/kintsugi_tax_platform_sdk/errors/backendsrcnexusresponsesvalidationerrorresponse.py): Validation error. Status code `422`. Applicable to 4 of 51 methods.*
* [`BackendSrcCustomersResponsesValidationErrorResponse`](./src/kintsugi_tax_platform_sdk/errors/backendsrccustomersresponsesvalidationerrorresponse.py): Query parameters failed validation, such as an out-of-range page number. Status code `422`. Applicable to 3 of 51 methods.*
* [`BackendSrcFilingsResponsesValidationErrorResponse`](./src/kintsugi_tax_platform_sdk/errors/backendsrcfilingsresponsesvalidationerrorresponse.py): Validation error. Status code `422`. Applicable to 3 of 51 methods.*
* [`BackendSrcAddressValidationResponsesValidationErrorResponse`](./src/kintsugi_tax_platform_sdk/errors/backendsrcaddressvalidationresponsesvalidationerrorresponse.py): Validation error - Address fields failed validation or are incomplete. Status code `422`. Applicable to 2 of 51 methods.*
* [`BackendSrcTaxEstimationResponsesValidationErrorResponse`](./src/kintsugi_tax_platform_sdk/errors/backendsrctaxestimationresponsesvalidationerrorresponse.py): Validation Error. Status code `422`. Applicable to 1 of 51 methods.*
* [`ResponseValidationError`](./src/kintsugi_tax_platform_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.trykintsugi.com",
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.address_validation.search(phone="555-123-4567", street_1="1600 Amphitheatre Parkway", street_2="Building 40", city="Mountain View", county="Santa Clara", state="CA", postal_code="94043", country=models.CountryCodeEnum.US, full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043")

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from kintsugi_tax_platform_sdk import SDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from kintsugi_tax_platform_sdk import SDK
from kintsugi_tax_platform_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SDK(async_client=CustomClient(httpx.AsyncClient()))
```
### httpx2 (Pydantic's httpx fork)

[httpx2](https://httpx2.pydantic.dev/) is Pydantic's maintained fork of `httpx`. To run this SDK on httpx2, call `alias_httpx()` at your program's entry point, before importing the SDK, so every `import httpx` — including the ones inside the SDK — resolves to `httpx2`:
```python
import httpx2

httpx2.alias_httpx()

from kintsugi_tax_platform_sdk import SDK

s = SDK()
```

An SDK can also be generated against httpx2 directly, so it depends on the fork instead of `httpx`, by setting `python.httpClientLibrary: httpx2` in `gen.yaml`.
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from kintsugi_tax_platform_sdk import SDK
def main():

    with SDK(
        api_key_header="<YOUR_API_KEY_HERE>",
    ) as sdk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SDK(
        api_key_header="<YOUR_API_KEY_HERE>",
    ) as sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from kintsugi_tax_platform_sdk import SDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SDK(debug_logger=logging.getLogger("kintsugi_tax_platform_sdk"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=kintsugi-tax-platform-sdk&utm_campaign=python)
