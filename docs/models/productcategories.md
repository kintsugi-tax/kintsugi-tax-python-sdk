# ProductCategories


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `name`                                                                                     | *str*                                                                                      | :heavy_check_mark:                                                                         | Name of the product category<br/>            (e.g., PHYSICAL, SERVICE, DIGITAL, MISCELLANEOUS) |
| `subcategories`                                                                            | List[[models.ProductSubCategory](../models/productsubcategory.md)]                         | :heavy_check_mark:                                                                         | List of subcategories associated with the product category                                 |