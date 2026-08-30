# MissouriFields

State-specific fields for Missouri portal registration import (MyTax Missouri).


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `registration_type`                                                        | [models.MissouriRegistrationType](../models/missouriregistrationtype.md)   | :heavy_check_mark:                                                         | N/A                                                                        |
| `business_name`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | State-registered business name as shown in MyTax Missouri.                 |
| `mo_state_tax_id`                                                          | *str*                                                                      | :heavy_check_mark:                                                         | Missouri state-issued tax identification number (MO State Tax ID).         |
| `third_party_access_enabled`                                               | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Whether third-party access has been granted to Kintsugi in MyTax Missouri. |