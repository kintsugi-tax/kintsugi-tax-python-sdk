# Products
(*products*)

## Overview

### Available Operations

* [list](#list) - Get Products
* [create](#create) - Create Product
* [get](#get) - Get Product By Id
* [update](#update) - Update Product
* [list_categories](#list_categories) - Get Product Categories

## list

Retrieve a paginated list of products based on filters and search query.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_products_v1_products__get" method="get" path="/v1/products/" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.products.list(security=models.GetProductsV1ProductsGetSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), x_organization_id="org_12345", page=1, size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.GetProductsV1ProductsGetSecurity](../../models/getproductsv1productsgetsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |                                                                                             |
| `x_organization_id`                                                                         | *Nullable[str]*                                                                             | :heavy_check_mark:                                                                          | The unique identifier for the organization making the request                               | org_12345                                                                                   |
| `query`                                                                                     | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | Search term to filter products by name or other details.                                    |                                                                                             |
| `status_in`                                                                                 | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | Filter products by status (comma-separated)                                                 |                                                                                             |
| `product_category_in`                                                                       | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | Filter products by category (comma-separated)                                               |                                                                                             |
| `product_subcategory_in`                                                                    | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | Filter products by subcategory (comma-separated)                                            |                                                                                             |
| `source_in`                                                                                 | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | Filter products by source (comma-separated)                                                 |                                                                                             |
| `order_by`                                                                                  | *OptionalNullable[str]*                                                                     | :heavy_minus_sign:                                                                          | Order results by specified fields (comma-separated)                                         |                                                                                             |
| `page`                                                                                      | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Page number                                                                                 |                                                                                             |
| `size`                                                                                      | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Page size                                                                                   |                                                                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.PageProductRead](../../models/pageproductread.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.ErrorResponse                                      | 401, 404                                                  | application/json                                          |
| errors.BackendSrcProductsResponsesValidationErrorResponse | 422                                                       | application/json                                          |
| errors.ErrorResponse                                      | 500                                                       | application/json                                          |
| errors.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## create

The Create Product API allows users to manually create a new product
    in the system. This includes specifying product details such as category,
    subcategory, and tax exemption status, etc.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_product_v1_products__post" method="post" path="/v1/products/" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.products.create(security=models.CreateProductV1ProductsPostSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), x_organization_id="org_12345", external_id="prod_001", name="Sample Product", product_category=models.ProductCategoryEnum.PHYSICAL, product_subcategory=models.ProductSubCategoryEnum.GENERAL_CLOTHING, tax_exempt=False, description="A description of the product", status=models.ProductStatusEnum.APPROVED, source=models.SourceEnum.BIGCOMMERCE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.CreateProductV1ProductsPostSecurity](../../models/createproductv1productspostsecurity.md)     | :heavy_check_mark:                                                                                    | N/A                                                                                                   |                                                                                                       |
| `x_organization_id`                                                                                   | *Nullable[str]*                                                                                       | :heavy_check_mark:                                                                                    | The unique identifier for the organization making the request                                         | org_12345                                                                                             |
| `external_id`                                                                                         | *str*                                                                                                 | :heavy_check_mark:                                                                                    | A unique external identifier for the product.                                                         |                                                                                                       |
| `name`                                                                                                | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The name of the product.                                                                              |                                                                                                       |
| `product_category`                                                                                    | [models.ProductCreateManualProductCategory](../../models/productcreatemanualproductcategory.md)       | :heavy_check_mark:                                                                                    | The high-level category of the product.                                                               |                                                                                                       |
| `product_subcategory`                                                                                 | [models.ProductCreateManualProductSubcategory](../../models/productcreatemanualproductsubcategory.md) | :heavy_check_mark:                                                                                    | The subcategory of the product.                                                                       |                                                                                                       |
| `tax_exempt`                                                                                          | *bool*                                                                                                | :heavy_check_mark:                                                                                    | Specifies whether the product is tax-exempt.                                                          |                                                                                                       |
| `description`                                                                                         | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | A description of the product.                                                                         |                                                                                                       |
| `status`                                                                                              | [Optional[models.ProductStatusEnum]](../../models/productstatusenum.md)                               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |                                                                                                       |
| `source`                                                                                              | [Optional[models.SourceEnum]](../../models/sourceenum.md)                                             | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |                                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Response

**[models.ProductRead](../../models/productread.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.ErrorResponse                                      | 401                                                       | application/json                                          |
| errors.BackendSrcProductsResponsesValidationErrorResponse | 422                                                       | application/json                                          |
| errors.ErrorResponse                                      | 500                                                       | application/json                                          |
| errors.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## get

The Get Product By ID API retrieves detailed information about
    a single product by its unique ID. This API helps in viewing the specific details
    of a product, including its attributes, status, and categorization.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_product_by_id_v1_products__product_id__get" method="get" path="/v1/products/{product_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.products.get(security=models.GetProductByIDV1ProductsProductIDGetSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), product_id="<id>", x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         | Example                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                          | [models.GetProductByIDV1ProductsProductIDGetSecurity](../../models/getproductbyidv1productsproductidgetsecurity.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |                                                                                                                     |
| `product_id`                                                                                                        | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | The unique identifier for the product you want to retrieve.                                                         |                                                                                                                     |
| `x_organization_id`                                                                                                 | *Nullable[str]*                                                                                                     | :heavy_check_mark:                                                                                                  | The unique identifier for the organization making the request                                                       | org_12345                                                                                                           |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |                                                                                                                     |

### Response

**[models.ProductRead](../../models/productread.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.ErrorResponse                                      | 401                                                       | application/json                                          |
| errors.BackendSrcProductsResponsesValidationErrorResponse | 422                                                       | application/json                                          |
| errors.ErrorResponse                                      | 500                                                       | application/json                                          |
| errors.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## update

The Update Product API allows users to modify the details of
    an existing product identified by its unique product_id

### Example Usage

<!-- UsageSnippet language="python" operationID="update_product_v1_products__product_id__put" method="put" path="/v1/products/{product_id}" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.products.update(security=models.UpdateProductV1ProductsProductIDPutSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), product_id="<id>", x_organization_id="org_12345", request_body={
        "name": "Updated Product Name",
        "status": models.ProductStatusEnum.APPROVED,
        "product_category": "PHYSICAL",
        "product_subcategory": "GENERAL_CLOTHING",
        "tax_exempt": False,
        "external_id": "prod_001",
        "description": "An updated description for the product",
        "classification_failed": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       | Example                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                        | [models.UpdateProductV1ProductsProductIDPutSecurity](../../models/updateproductv1productsproductidputsecurity.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |                                                                                                                   |
| `product_id`                                                                                                      | *str*                                                                                                             | :heavy_check_mark:                                                                                                | Unique identifier of the product to be updated.                                                                   |                                                                                                                   |
| `x_organization_id`                                                                                               | *Nullable[str]*                                                                                                   | :heavy_check_mark:                                                                                                | The unique identifier for the organization making the request                                                     | org_12345                                                                                                         |
| `request_body`                                                                                                    | [models.Product](../../models/product.md)                                                                         | :heavy_check_mark:                                                                                                | N/A                                                                                                               |                                                                                                                   |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |                                                                                                                   |

### Response

**[models.ProductRead](../../models/productread.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.ErrorResponse                                      | 401                                                       | application/json                                          |
| errors.BackendSrcProductsResponsesValidationErrorResponse | 422                                                       | application/json                                          |
| errors.ErrorResponse                                      | 500                                                       | application/json                                          |
| errors.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## list_categories

The Get Product Categories API retrieves all
    product categories.  This endpoint helps users understand and select the
    appropriate categories for their products.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_product_categories_v1_products_categories__get" method="get" path="/v1/products/categories/" -->
```python
from kintsugi_tax_platform_sdk import SDK, models


with SDK(
    server_url="https://api.example.com",
) as sdk:

    res = sdk.products.list_categories(security=models.GetProductCategoriesV1ProductsCategoriesGetSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), x_organization_id="org_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       | Example                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                        | [models.GetProductCategoriesV1ProductsCategoriesGetSecurity](../../models/getproductcategoriesv1productscategoriesgetsecurity.md) | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |                                                                                                                                   |
| `x_organization_id`                                                                                                               | *Nullable[str]*                                                                                                                   | :heavy_check_mark:                                                                                                                | The unique identifier for the organization making the request                                                                     | org_12345                                                                                                                         |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |                                                                                                                                   |

### Response

**[List[models.ProductCategories]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |