# MichiganFields

State-specific fields for Michigan registration import (Michigan Treasury Online / MTO).


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `registration_type`                                                                        | [models.MichiganRegistrationType](../models/michiganregistrationtype.md)                   | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `business_name`                                                                            | *str*                                                                                      | :heavy_check_mark:                                                                         | State-registered business name as shown in Michigan Treasury Online (MTO).                 |
| `mi_state_tax_id`                                                                          | *str*                                                                                      | :heavy_check_mark:                                                                         | Michigan state-issued tax identification number (MI State Tax ID).                         |
| `third_party_access_enabled`                                                               | *Optional[bool]*                                                                           | :heavy_minus_sign:                                                                         | Whether third-party access has been granted to Kintsugi in Michigan Treasury Online (MTO). |