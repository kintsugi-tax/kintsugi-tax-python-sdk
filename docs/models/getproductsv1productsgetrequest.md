# GetProductsV1ProductsGetRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `query`                                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | Search term to filter products by name or other details. |
| `status_in`                                              | *Optional[str]*                                          | :heavy_minus_sign:                                       | Filter products by status (comma-separated)              |
| `product_category_in`                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | Filter products by category (comma-separated)            |
| `product_subcategory_in`                                 | *Optional[str]*                                          | :heavy_minus_sign:                                       | Filter products by subcategory (comma-separated)         |
| `source_in`                                              | *Optional[str]*                                          | :heavy_minus_sign:                                       | Filter products by source (comma-separated)              |
| `order_by`                                               | *Optional[str]*                                          | :heavy_minus_sign:                                       | Order results by specified fields (comma-separated)      |
| `page`                                                   | *Optional[int]*                                          | :heavy_minus_sign:                                       | Page number                                              |
| `size`                                                   | *Optional[int]*                                          | :heavy_minus_sign:                                       | Page size                                                |