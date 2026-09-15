# RegistrationJurisdictionOptionRead

One distinct (country, state) jurisdiction for listings and filters.


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `country_code`                                                | *str*                                                         | :heavy_check_mark:                                            | ISO 3166-1 alpha-2 country code (e.g. US, DE).                |
| `state_code`                                                  | *str*                                                         | :heavy_check_mark:                                            | State or province code (may be empty for country-level rows). |
| `state_name`                                                  | *str*                                                         | :heavy_check_mark:                                            | Display name for the state or province.                       |