# Products
(*products*)

## Overview

### Available Operations

* [get_products_v1_products_get](#get_products_v1_products_get) - Get Products
* [create_product_v1_products_post](#create_product_v1_products_post) - Create Product
* [get_product_by_id_v1_products_product_id_get](#get_product_by_id_v1_products_product_id_get) - Get Product By Id
* [update_product_v1_products_product_id_put](#update_product_v1_products_product_id_put) - Update Product
* [get_product_categories_v1_products_categories_get](#get_product_categories_v1_products_categories_get) - Get Product Categories

## get_products_v1_products_get

Retrieve a paginated list of products based on filters and search query.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_products_v1_products__get" method="get" path="/v1/products/" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.products.get_products_v1_products_get(page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search term to filter products by name or other details.            |
| `status_in`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter products by status (comma-separated)                         |
| `product_category_in`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter products by category (comma-separated)                       |
| `product_subcategory_in`                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter products by subcategory (comma-separated)                    |
| `source_in`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter products by source (comma-separated)                         |
| `order_by`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Order results by specified fields (comma-separated)                 |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number                                                         |
| `size`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page size                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PageProductRead](../../models/pageproductread.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.ErrorResponse                                      | 401, 404                                                  | application/json                                          |
| errors.BackendSrcProductsResponsesValidationErrorResponse | 422                                                       | application/json                                          |
| errors.ErrorResponse                                      | 500                                                       | application/json                                          |
| errors.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## create_product_v1_products_post

The Create Product API allows users to manually create a new product
    in the system. This includes specifying product details such as category,
    subcategory, and tax exemption status, etc.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_product_v1_products__post" method="post" path="/v1/products/" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.products.create_product_v1_products_post(external_id="prod_001", name="Sample Product", product_category=models.ProductCategoryEnum.PHYSICAL, product_subcategory=models.ProductSubCategoryEnum.GENERAL_CLOTHING, tax_exempt=False, description="A description of the product", status=models.ProductStatusEnum.APPROVED, source=models.SourceEnum.BIGCOMMERCE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `external_id`                                                           | *str*                                                                   | :heavy_check_mark:                                                      | A unique external identifier for the product.                           |
| `name`                                                                  | *str*                                                                   | :heavy_check_mark:                                                      | The name of the product.                                                |
| `product_category`                                                      | [models.ProductCategoryEnum](../../models/productcategoryenum.md)       | :heavy_check_mark:                                                      | N/A                                                                     |
| `product_subcategory`                                                   | [models.ProductSubCategoryEnum](../../models/productsubcategoryenum.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `tax_exempt`                                                            | *bool*                                                                  | :heavy_check_mark:                                                      | Specifies whether the product is tax-exempt.                            |
| `description`                                                           | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | A description of the product.                                           |
| `status`                                                                | [Optional[models.ProductStatusEnum]](../../models/productstatusenum.md) | :heavy_minus_sign:                                                      | N/A                                                                     |
| `source`                                                                | [Optional[models.SourceEnum]](../../models/sourceenum.md)               | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ProductRead](../../models/productread.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.ErrorResponse                                      | 401                                                       | application/json                                          |
| errors.BackendSrcProductsResponsesValidationErrorResponse | 422                                                       | application/json                                          |
| errors.ErrorResponse                                      | 500                                                       | application/json                                          |
| errors.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## get_product_by_id_v1_products_product_id_get

The Get Product By ID API retrieves detailed information about
    a single product by its unique ID. This API helps in viewing the specific details
    of a product, including its attributes, status, and categorization.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_product_by_id_v1_products__product_id__get" method="get" path="/v1/products/{product_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.products.get_product_by_id_v1_products_product_id_get(product_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier for the product you want to retrieve.         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProductRead](../../models/productread.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.ErrorResponse                                      | 401                                                       | application/json                                          |
| errors.BackendSrcProductsResponsesValidationErrorResponse | 422                                                       | application/json                                          |
| errors.ErrorResponse                                      | 500                                                       | application/json                                          |
| errors.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## update_product_v1_products_product_id_put

The Update Product API allows users to modify the details of
    an existing product identified by its unique product_id

### Example Usage

<!-- UsageSnippet language="python" operationID="update_product_v1_products__product_id__put" method="put" path="/v1/products/{product_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.products.update_product_v1_products_product_id_put(product_id="<id>", name="Updated Product Name", product_category=models.ProductCategoryEnum.PHYSICAL, product_subcategory=models.ProductSubCategoryEnum.GENERAL_CLOTHING, tax_exempt=False, external_id="prod_001", description="An updated description for the product", status=models.ProductStatusEnum.APPROVED, classification_failed=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `product_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | Unique identifier of the product to be updated.                                       |
| `name`                                                                                | *str*                                                                                 | :heavy_check_mark:                                                                    | Name of the product.                                                                  |
| `product_category`                                                                    | [models.ProductCategoryEnum](../../models/productcategoryenum.md)                     | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `product_subcategory`                                                                 | [models.ProductSubCategoryEnum](../../models/productsubcategoryenum.md)               | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `tax_exempt`                                                                          | *bool*                                                                                | :heavy_check_mark:                                                                    | Indicates whether the product is tax-exempt.                                          |
| `id`                                                                                  | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | The unique identifier of the product to be updated.                                   |
| `external_id`                                                                         | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | External identifier provided for the product,<br/>        typically by the source system. |
| `sku`                                                                                 | List[*str*]                                                                           | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `description`                                                                         | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Description of the product.                                                           |
| `status`                                                                              | [Optional[models.ProductStatusEnum]](../../models/productstatusenum.md)               | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `classification_failed`                                                               | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Indicates if the product classification failed.                                       |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ProductRead](../../models/productread.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.ErrorResponse                                      | 401                                                       | application/json                                          |
| errors.BackendSrcProductsResponsesValidationErrorResponse | 422                                                       | application/json                                          |
| errors.ErrorResponse                                      | 500                                                       | application/json                                          |
| errors.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## get_product_categories_v1_products_categories_get

The Get Product Categories API retrieves all
    product categories.  This endpoint helps users understand and select the
    appropriate categories for their products.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_product_categories_v1_products_categories__get" method="get" path="/v1/products/categories/" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    security=models.Security(
        api_key_header="<YOUR_API_KEY_HERE>",
        custom_header="<YOUR_API_KEY_HERE>",
    ),
) as sdk:

    res = sdk.products.get_product_categories_v1_products_categories_get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.ProductCategories]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |