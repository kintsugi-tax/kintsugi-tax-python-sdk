# IdahoFields

State-specific fields for Idaho TAP portal registration import.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `registration_type`                                                      | [models.IdahoRegistrationType](../models/idahoregistrationtype.md)       | :heavy_check_mark:                                                       | N/A                                                                      |
| `mfa_completed`                                                          | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | Whether the customer has completed MFA setup in their Idaho tax account. |
| `business_name`                                                          | *str*                                                                    | :heavy_check_mark:                                                       | Business name as registered with the Idaho State Tax Commission.         |
| `sales_tax_id`                                                           | *str*                                                                    | :heavy_check_mark:                                                       | Idaho State Tax ID.                                                      |
| `access_code`                                                            | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | Customers add this in registration credentials after the Idaho           |