<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from kintsugi_tax_platform_sdk import SDK, models


with SDK() as sdk:

    res = sdk.address_validation.search(security=models.SearchV1AddressValidationSearchPostSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), phone="555-123-4567", street_1="1600 Amphitheatre Parkway", street_2="Building 40", city="Mountain View", county="Santa Clara", state="CA", postal_code="94043", country=models.CountryCodeEnum.US, full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043")

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

    async with SDK() as sdk:

        res = await sdk.address_validation.search_async(security=models.SearchV1AddressValidationSearchPostSecurity(
            api_key_header="<YOUR_API_KEY_HERE>",
        ), phone="555-123-4567", street_1="1600 Amphitheatre Parkway", street_2="Building 40", city="Mountain View", county="Santa Clara", state="CA", postal_code="94043", country=models.CountryCodeEnum.US, full_address="1600 Amphitheatre Parkway, Mountain View, CA 94043")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->