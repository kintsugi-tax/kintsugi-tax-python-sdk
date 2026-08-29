# UpdateCustomerV1CustomersCustomerIDPutRequest


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   | Example                                                       |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `customer_id`                                                 | *str*                                                         | :heavy_check_mark:                                            | Unique identifier of the customer to be retrieved.            |                                                               |
| `x_organization_id`                                           | *Nullable[str]*                                               | :heavy_check_mark:                                            | The unique identifier for the organization making the request | org_12345                                                     |
| `customer_update`                                             | [models.CustomerUpdate](../models/customerupdate.md)          | :heavy_check_mark:                                            | N/A                                                           |                                                               |