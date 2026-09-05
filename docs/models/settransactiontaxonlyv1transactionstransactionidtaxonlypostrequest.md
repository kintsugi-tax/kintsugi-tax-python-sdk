# SetTransactionTaxOnlyV1TransactionsTransactionIDTaxOnlyPostRequest


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   | Example                                                       |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `transaction_id`                                              | *str*                                                         | :heavy_check_mark:                                            | N/A                                                           |                                                               |
| `x_organization_id`                                           | *Nullable[str]*                                               | :heavy_check_mark:                                            | The unique identifier for the organization making the request | org_12345                                                     |
| `tax_only_update`                                             | [models.TaxOnlyUpdate](../models/taxonlyupdate.md)            | :heavy_check_mark:                                            | N/A                                                           |                                                               |