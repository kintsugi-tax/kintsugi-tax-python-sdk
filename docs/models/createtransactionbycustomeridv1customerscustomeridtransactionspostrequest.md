# CreateTransactionByCustomerIDV1CustomersCustomerIDTransactionsPostRequest


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   | Example                                                       |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `customer_id_param`                                           | *str*                                                         | :heavy_check_mark:                                            | N/A                                                           |                                                               |
| `x_organization_id`                                           | *Nullable[str]*                                               | :heavy_check_mark:                                            | The unique identifier for the organization making the request | org_12345                                                     |
| `transaction_create`                                          | [models.TransactionCreate](../models/transactioncreate.md)    | :heavy_check_mark:                                            | N/A                                                           |                                                               |