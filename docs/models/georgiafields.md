# GeorgiaFields

State-specific fields for Georgia GTC registration import.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `registration_type`                                                        | [models.GeorgiaRegistrationType](../models/georgiaregistrationtype.md)     | :heavy_check_mark:                                                         | N/A                                                                        |
| `mfa_completed`                                                            | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Whether the customer has completed MFA setup in their Georgia GTC account. |
| `business_name`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | Business name as registered with the state of Georgia.                     |
| `sales_tax_id`                                                             | *str*                                                                      | :heavy_check_mark:                                                         | Georgia State Tax ID.                                                      |
| `zip_code`                                                                 | *str*                                                                      | :heavy_check_mark:                                                         | Georgia ZIP code on file with the Georgia Department of Revenue.           |
| `last_payment_to_state`                                                    | *str*                                                                      | :heavy_check_mark:                                                         | Last payment amount made to the state ('0.00' if no payments made).        |