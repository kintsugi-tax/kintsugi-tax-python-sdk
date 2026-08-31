# NebraskaFields

State-specific fields for a Nebraska registration import.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `registration_type`                                                            | [models.NebraskaRegistrationType](../models/nebraskaregistrationtype.md)       | :heavy_check_mark:                                                             | N/A                                                                            |
| `mfa_completed`                                                                | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | Whether the customer completed Kintsugi MFA setup on the Nebraska tax account. |
| `business_name`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | State-registered business name shown on the Nebraska tax account.              |
| `ne_user_id`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | Nebraska User ID shown on Form 10 from the Nebraska Department of Revenue.     |