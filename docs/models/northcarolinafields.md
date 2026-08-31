# NorthCarolinaFields

State-specific fields for North Carolina (NCDOR) registration import.

North Carolina requires no 2FA/MFA setup, so there is no ``mfa_completed``
field, and it grants no customer-facing third-party access step, so there is no
``third_party_access_enabled`` field either — unlike most other portal states.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `registration_type`                                                        | *Literal["SALES_AND_USE_TAX"]*                                             | :heavy_check_mark:                                                         | Registration type for this North Carolina import: sales and use tax.       |
| `business_name`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | State-registered business name as shown on the North Carolina tax account. |
| `nc_state_tax_id`                                                          | *str*                                                                      | :heavy_check_mark:                                                         | North Carolina state-issued tax identification number (NC State Tax ID).   |
| `contact_name`                                                             | *str*                                                                      | :heavy_check_mark:                                                         | Primary contact name on the North Carolina tax account.                    |
| `contact_email`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | Primary contact email address on the North Carolina tax account.           |
| `contact_phone`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | Primary contact phone number on the North Carolina tax account.            |