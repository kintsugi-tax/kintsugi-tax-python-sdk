# Products

## Overview

### Available Operations

* [get_products_v1_products_get](#get_products_v1_products_get) - Get products
* [create_product_v1_products_post](#create_product_v1_products_post) - Create product
* [get_product_categories_v1_products_categories_get](#get_product_categories_v1_products_categories_get) - Get product categories
* [retrieve](#retrieve) - Get product by id
* [update](#update) - Update product

## get_products_v1_products_get

Retrieve a paginated list of products based on filters and search query.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_products_v1_products_get" method="get" path="/v1/products" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.products.get_products_v1_products_get(x_organization_id="org_12345", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `x_organization_id`                                                                                       | *Nullable[str]*                                                                                           | :heavy_check_mark:                                                                                        | The unique identifier for the organization making the request                                             | org_12345                                                                                                 |
| `query`                                                                                                   | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | Search term to filter products by name or other details.                                                  |                                                                                                           |
| `status_in`                                                                                               | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | Filter products by status (comma-separated)                                                               |                                                                                                           |
| `product_category_in`                                                                                     | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | Filter products by category (comma-separated)                                                             |                                                                                                           |
| `product_subcategory_in`                                                                                  | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | Filter products by subcategory (comma-separated)                                                          |                                                                                                           |
| `source_in`                                                                                               | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | Filter products by source (comma-separated)                                                               |                                                                                                           |
| `connection_id_in`                                                                                        | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | Filter products by connection ID (comma-separated). Use __direct_api__ for products without a connection. |                                                                                                           |
| `order_by`                                                                                                | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | Order results by specified fields (comma-separated)                                                       |                                                                                                           |
| `page`                                                                                                    | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |                                                                                                           |
| `size`                                                                                                    | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |                                                                                                           |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Response

**[models.PageProductRead](../../models/pageproductread.md)**

### Errors

| Error Type                                                       | Status Code                                                      | Content Type                                                     |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| errors.ErrorResponse                                             | 401, 404                                                         | application/json                                                 |
| errors.BackendSrcProductsSchemasResponsesValidationErrorResponse | 422                                                              | application/json                                                 |
| errors.ErrorResponse                                             | 500                                                              | application/json                                                 |
| errors.APIError                                                  | 4XX, 5XX                                                         | \*/\*                                                            |

## create_product_v1_products_post

The Create Product API allows users to manually create a new product
    in the system. This includes specifying product details such as category,
    subcategory, and tax exemption status, etc. You can
    retrieve supported categories and subcategories from the
    [GET /products/categories endpoint](/reference/api/products/get-product-categories),
    or browse the full catalog with descriptions and examples in the
    [Product Categories guide](/docs/guides/product-categories)

### Example Usage

<!-- UsageSnippet language="python" operationID="create_product_v1_products_post" method="post" path="/v1/products" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.products.create_product_v1_products_post(x_organization_id="org_12345", external_id="prod_001", name="T-shirts", product_category=models.PublicProductCategoryEnum.PHYSICAL, product_subcategory="General Clothing", tax_exempt=False, description="Common items of everyday wearing apparel designed for human use, covering a wide variety of non-specialized garments.", status=models.ProductStatusEnum.APPROVED, source=models.SourceEnum.BIGCOMMERCE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `x_organization_id`                                                           | *Nullable[str]*                                                               | :heavy_check_mark:                                                            | The unique identifier for the organization making the request                 | org_12345                                                                     |
| `external_id`                                                                 | *str*                                                                         | :heavy_check_mark:                                                            | A unique external identifier for the product.                                 |                                                                               |
| `name`                                                                        | *str*                                                                         | :heavy_check_mark:                                                            | The name of the product.                                                      |                                                                               |
| `product_category`                                                            | [models.PublicProductCategoryEnum](../../models/publicproductcategoryenum.md) | :heavy_check_mark:                                                            | Top-level tax category for a product.                                         |                                                                               |
| `product_subcategory`                                                         | [models.ProductSubcategoryUnion](../../models/productsubcategoryunion.md)     | :heavy_check_mark:                                                            | The subcategory of the product.                                               |                                                                               |
| `tax_exempt`                                                                  | *bool*                                                                        | :heavy_check_mark:                                                            | Specifies whether the product is tax-exempt.                                  |                                                                               |
| `description`                                                                 | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | A description of the product.                                                 |                                                                               |
| `status`                                                                      | [Optional[models.ProductStatusEnum]](../../models/productstatusenum.md)       | :heavy_minus_sign:                                                            | N/A                                                                           |                                                                               |
| `source`                                                                      | [Optional[models.SourceEnum]](../../models/sourceenum.md)                     | :heavy_minus_sign:                                                            | N/A                                                                           |                                                                               |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |                                                                               |

### Response

**[models.ProductRead](../../models/productread.md)**

### Errors

| Error Type                                                       | Status Code                                                      | Content Type                                                     |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| errors.ErrorResponse                                             | 401                                                              | application/json                                                 |
| errors.BackendSrcProductsSchemasResponsesValidationErrorResponse | 422                                                              | application/json                                                 |
| errors.ErrorResponse                                             | 500                                                              | application/json                                                 |
| errors.APIError                                                  | 4XX, 5XX                                                         | \*/\*                                                            |

## get_product_categories_v1_products_categories_get

The Get Product Categories API retrieves all
    product categories.  This endpoint helps users understand and select the
    appropriate categories for their products.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_product_categories_v1_products_categories_get" method="get" path="/v1/products/categories" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.products.get_product_categories_v1_products_categories_get(x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The unique identifier for the organization making the request       | org_12345                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ProductCategoryRead](../../models/productcategoryread.md)**

### Errors

| Error Type                                                       | Status Code                                                      | Content Type                                                     |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| errors.ErrorResponse                                             | 401                                                              | application/json                                                 |
| errors.BackendSrcProductsSchemasResponsesValidationErrorResponse | 422                                                              | application/json                                                 |
| errors.ErrorResponse                                             | 500                                                              | application/json                                                 |
| errors.APIError                                                  | 4XX, 5XX                                                         | \*/\*                                                            |

## retrieve

The Get Product By ID API retrieves detailed information about
    a single product by its unique ID. This API helps in viewing the specific details
    of a product, including its attributes, status, and categorization.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_product_by_id_v1_products__product_id__get" method="get" path="/v1/products/{product_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.products.retrieve(product_id="<id>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier for the product you want to retrieve.         |                                                                     |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The unique identifier for the organization making the request       | org_12345                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ProductRead](../../models/productread.md)**

### Errors

| Error Type                                                       | Status Code                                                      | Content Type                                                     |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| errors.ErrorResponse                                             | 401                                                              | application/json                                                 |
| errors.BackendSrcProductsSchemasResponsesValidationErrorResponse | 422                                                              | application/json                                                 |
| errors.ErrorResponse                                             | 500                                                              | application/json                                                 |
| errors.APIError                                                  | 4XX, 5XX                                                         | \*/\*                                                            |

## update

The Update Product API allows users to modify the details of
    an existing product identified by its unique product_id. You can
    retrieve supported categories and subcategories from the
    [GET /products/categories endpoint](/reference/api/products/get-product-categories),
    or browse the full catalog with descriptions and examples in the
    [Product Categories guide](/docs/guides/product-categories)

### Example Usage

<!-- UsageSnippet language="python" operationID="update_product_v1_products__product_id__put" method="put" path="/v1/products/{product_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    api_key_header="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.products.update(product_id="<id>", x_organization_id="org_12345", request_body={
        "name": "Updated T-Shirt",
        "status": models.ProductStatusEnum.APPROVED,
        "product_category": "Physical",
        "product_subcategory": "General Clothing",
        "tax_exempt": False,
        "external_id": "prod_001",
        "description": "An updated description for the product",
        "classification_failed": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the product to be updated.                     |                                                                     |
| `x_organization_id`                                                 | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The unique identifier for the organization making the request       | org_12345                                                           |
| `request_body`                                                      | [models.Product](../../models/product.md)                           | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ProductRead](../../models/productread.md)**

### Errors

| Error Type                                                       | Status Code                                                      | Content Type                                                     |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| errors.ErrorResponse                                             | 401                                                              | application/json                                                 |
| errors.BackendSrcProductsSchemasResponsesValidationErrorResponse | 422                                                              | application/json                                                 |
| errors.ErrorResponse                                             | 500                                                              | application/json                                                 |
| errors.APIError                                                  | 4XX, 5XX                                                         | \*/\*                                                            |