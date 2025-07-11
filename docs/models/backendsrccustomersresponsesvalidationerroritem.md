# BackendSrcCustomersResponsesValidationErrorItem


## Fields

| Field                    | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `type`                   | *str*                    | :heavy_check_mark:       | Type of validation error |
| `loc`                    | List[*str*]              | :heavy_check_mark:       | Location of error        |
| `msg`                    | *str*                    | :heavy_check_mark:       | Error message            |
| `input`                  | *Any*                    | :heavy_check_mark:       | Invalid input value      |
| `ctx`                    | Dict[str, *Any*]         | :heavy_check_mark:       | Additional context       |