# ArizonaFields

State-specific fields for Arizona TPT registration import.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `registration_type`                                                                | [models.ArizonaRegistrationType](../models/arizonaregistrationtype.md)             | :heavy_check_mark:                                                                 | N/A                                                                                |
| `mfa_completed`                                                                    | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Whether the customer has completed MFA setup in their Arizona AZTaxes.gov account. |
| `business_name`                                                                    | *str*                                                                              | :heavy_check_mark:                                                                 | Business name as registered with the state of Arizona.                             |
| `sales_tax_id`                                                                     | *str*                                                                              | :heavy_check_mark:                                                                 | Arizona state-issued sales tax number (AZ State Tax ID).                           |
| `location_id`                                                                      | *str*                                                                              | :heavy_check_mark:                                                                 | Business location ID as shown in AZTaxes.gov.                                      |