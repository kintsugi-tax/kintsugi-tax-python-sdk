# ProductUpdateV2


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `status`                                                   | [models.ProductStatusEnum](../models/productstatusenum.md) | :heavy_check_mark:                                         | N/A                                                        |
| `product_category`                                         | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `product_subcategory`                                      | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `tax_exempt`                                               | *bool*                                                     | :heavy_check_mark:                                         | N/A                                                        |
| `external_id`                                              | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `sku`                                                      | List[*str*]                                                | :heavy_minus_sign:                                         | N/A                                                        |
| `description`                                              | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `classification_failed`                                    | *OptionalNullable[bool]*                                   | :heavy_minus_sign:                                         | N/A                                                        |