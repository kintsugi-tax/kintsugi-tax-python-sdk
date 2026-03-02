# CustomerTaxRegistrationRead


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `customer_id`                                                  | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `country_code`                                                 | [models.CountryCodeEnum](../models/countrycodeenum.md)         | :heavy_check_mark:                                             | N/A                                                            |
| `tax_type`                                                     | [models.CustomerTaxTypeEnum](../models/customertaxtypeenum.md) | :heavy_check_mark:                                             | Enum for customer tax registration types.                      |
| `tax_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `is_valid`                                                     | *bool*                                                         | :heavy_check_mark:                                             | N/A                                                            |