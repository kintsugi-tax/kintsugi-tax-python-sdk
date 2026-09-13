# MassachusettsFields

State-specific fields for Massachusetts registration import (MassTaxConnect).


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `registration_type`                                                                 | [models.MassachusettsRegistrationType](../models/massachusettsregistrationtype.md)  | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `business_name`                                                                     | *str*                                                                               | :heavy_check_mark:                                                                  | Business name as registered with the Commonwealth of Massachusetts.                 |
| `ma_state_account_id`                                                               | *str*                                                                               | :heavy_check_mark:                                                                  | Massachusetts state tax account ID from MassTaxConnect.                             |
| `mfa_completed`                                                                     | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Whether the customer has completed MFA setup in their Massachusetts tax account.    |
| `third_party_access_enabled`                                                        | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Whether the customer has granted third-party access for Kintsugi in MassTaxConnect. |