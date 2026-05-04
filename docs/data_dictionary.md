# Data Dictionary / 数据字典

## Expense Input / 支出输入

| Field | Meaning | Notes |
|---|---|---|
| Record ID | Unique transaction ID | Example: EXP-0001 / 支出-0001 |
| Date | Transaction date | Use real Excel dates |
| Expense Description | Merchant or note | Keep it short and searchable |
| Expense Amount | Positive expense amount | Do not enter negative expenses |
| Main Category | Spending category | Housing, Food, Transport, Communication, etc. |
| Expense Type | Fixed / Variable / One-time | Used for reserve and spending judgment |
| Necessity | Essential / Discretionary | Used for lean scenario analysis |
| Analysis Scope | Personal / Property / Transfer / Investment | Prevents double counting |
| Tax Type | Taxable / Zero-rated / Exempt / Auto | Used for GST/QST estimate |
| Notes | Manual explanation | Good place for uncertainty flags |

## Income Input / 收入输入

| Field | Meaning | Notes |
|---|---|---|
| Record ID | Unique income ID | Example: INC-0001 / 收入-0001 |
| Date | Income date | Use real Excel dates |
| Income Source | Salary, refund, rent, etc. | Keep consistent naming |
| Income Amount | Positive income amount | Do not enter negative income |
| Income Type | Salary / Refund / Rental / Other | Used for monthly summary |
| Notes | Manual explanation | Optional |
