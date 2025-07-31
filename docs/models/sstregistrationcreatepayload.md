# SSTRegistrationCreatePayload


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `registration_import_type`                                         | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Specifies this is an SST registration import.                      |
| `password_plain_text`                                              | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The plaintext password for accessing the tax registration account. |
| `password_metadata_plain_text`                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Metadata related to the password.                                  |
| `username`                                                         | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Username for accessing the tax registration account.               |