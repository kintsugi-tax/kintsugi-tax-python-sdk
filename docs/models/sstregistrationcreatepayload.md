# SSTRegistrationCreatePayload


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `registration_import_type`                                         | *Optional[Literal["SST"]]*                                         | :heavy_minus_sign:                                                 | Specifies this is an SST registration import.                      |
| `password_plain_text`                                              | *OptionalNullable[str]*                                            | :heavy_minus_sign:                                                 | The plaintext password for accessing the tax registration account. |
| `password_metadata_plain_text`                                     | *OptionalNullable[str]*                                            | :heavy_minus_sign:                                                 | Metadata related to the password.                                  |
| `username`                                                         | *OptionalNullable[str]*                                            | :heavy_minus_sign:                                                 | Username for accessing the tax registration account.               |
| `request_id`                                                       | *OptionalNullable[str]*                                            | :heavy_minus_sign:                                                 | Optional client-minted id for this confirm attempt.                |