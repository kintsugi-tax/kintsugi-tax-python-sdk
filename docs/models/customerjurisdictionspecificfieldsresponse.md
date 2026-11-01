# CustomerJurisdictionSpecificFieldsResponse

Customer import fields, including the tax types that jurisdiction allows.

The partner and public jurisdiction-fields routes stay on the base response.
Allowed tax types depend on the organization, and those contracts do not.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `country_code`                                                                             | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `state_code`                                                                               | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `default_form`                                                                             | *bool*                                                                                     | :heavy_check_mark:                                                                         | True when no state-specific schema exists and the generic form should be used.             |
| `jurisdiction_fields_json_schema`                                                          | Dict[str, *Any*]                                                                           | :heavy_check_mark:                                                                         | JSON Schema for the jurisdiction-specific fields, or empty dict when default_form is True. |
| `metadata`                                                                                 | Dict[str, *Any*]                                                                           | :heavy_check_mark:                                                                         | UI metadata (help articles, portal URL, filing frequencies, etc.).                         |
| `tax_types`                                                                                | List[[models.TaxTypeEnum](../models/taxtypeenum.md)]                                       | :heavy_check_mark:                                                                         | Tax types that can be imported for this jurisdiction.                                      |