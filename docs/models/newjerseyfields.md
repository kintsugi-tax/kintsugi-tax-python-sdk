# NewJerseyFields

State-specific fields for New Jersey (Premier Business Services) registration import.

New Jersey requires no 2FA/MFA setup (mirroring Michigan MTO), so there is no
``mfa_completed`` field and no MFA/2FA help article in the metadata.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `registration_type`                                                              | *Literal["SALES_AND_USE_TAX"]*                                                   | :heavy_check_mark:                                                               | Registration type for this New Jersey import: sales and use tax.                 |
| `business_name`                                                                  | *str*                                                                            | :heavy_check_mark:                                                               | State-registered business name as shown in New Jersey Premier Business Services. |
| `nj_state_tax_id`                                                                | *str*                                                                            | :heavy_check_mark:                                                               | New Jersey state-issued taxpayer identification number (NJ State Taxpayer ID).   |
| `third_party_access_enabled`                                                     | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Whether third-party access has been granted to Kintsugi in New Jersey.           |