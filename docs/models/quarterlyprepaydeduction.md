# QuarterlyPrepayDeduction

A single monthly prepayment netted against a quarterly reconciliation filing.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `label`                                                     | *str*                                                       | :heavy_check_mark:                                          | Human-readable label, e.g. 'April prepayment'.              |
| `amount`                                                    | *str*                                                       | :heavy_check_mark:                                          | Prepayment tax liability subtracted from the quarter total. |
| `filing_id`                                                 | *str*                                                       | :heavy_check_mark:                                          | Identifier of the monthly prepayment filing.                |