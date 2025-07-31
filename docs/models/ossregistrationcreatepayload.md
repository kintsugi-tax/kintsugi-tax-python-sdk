# OSSRegistrationCreatePayload


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `registration_import_type`                                         | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Specifies this is an OSS registration import.                      |
| `password_plain_text`                                              | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The plaintext password for accessing the tax registration account. |
| `password_metadata_plain_text`                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Metadata related to the password.                                  |
| `member_state_of_identification_code`                              | [Optional[models.CountryCodeEnum]](../models/countrycodeenum.md)   | :heavy_minus_sign:                                                 | N/A                                                                |
| `imported`                                                         | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Whether the registration was imported from another system.         |