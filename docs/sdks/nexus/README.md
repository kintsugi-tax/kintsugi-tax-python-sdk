# Nexus
(*nexus*)

## Overview

### Available Operations

* [list](#list) - Get Nexus For Org

## list

Get a list of all nexuses for the organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_nexus_for_org_v1_nexus_get" method="get" path="/v1/nexus" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.nexus.list(security=models.GetNexusForOrgV1NexusGetSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), x_organization_id="org_12345", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.GetNexusForOrgV1NexusGetSecurity](../../models/getnexusfororgv1nexusgetsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |                                                                                             |
| `x_organization_id`                                                                         | *Nullable[str]*                                                                             | :heavy_check_mark:                                                                          | The unique identifier for the organization making the request                               | org_12345                                                                                   |
| `status_in`                                                                                 | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |                                                                                             |
| `state_code`                                                                                | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |                                                                                             |
| `country_code_in`                                                                           | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |                                                                                             |
| `order_by`                                                                                  | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | N/A                                                                                         |                                                                                             |
| `collected_tax_nexus_met`                                                                   | *OptionalNullable[bool]*                                                                    | :heavy_minus_sign:                                                                          | N/A                                                                                         |                                                                                             |
| `page`                                                                                      | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Page number                                                                                 |                                                                                             |
| `size`                                                                                      | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Page size                                                                                   |                                                                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.PageNexusResponse](../../models/pagenexusresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |