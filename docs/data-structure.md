# Data Structure

## Expenses Sheet

| Field | Description |
|---|---|
| Record_ID | Unique transaction ID |
| Month | Month in `YYYY-MM` format |
| Date | Transaction date |
| Original_Text | Optional raw text from bank statement or notes |
| Merchant / Description | Transaction description |
| Amount | Negative number for expense |
| Currency | Currency code, e.g. CAD or USD |
| Direction | Expense / Transfer / Investment |
| Main_Category | High-level category |
| Sub_Category | Detailed category |
| Fixed_or_Variable | Fixed / Variable / One-time |
| Essential_or_Discretionary | Essential / Discretionary |
| Analysis_Treatment | Personal_Expense / Property_Cashflow / Investment / Internal_Transfer / Excluded |
| Confidence_Level | High / Medium / Low |
| Notes | Additional comments |

## Income Sheet

| Field | Description |
|---|---|
| Month | Month in `YYYY-MM` format |
| Date | Income date |
| Source | Income source |
| Description | Income description |
| Amount | Positive number for income |
| Currency | Currency code |
| Notes | Additional comments |

## Input Settings

Stores manual assumptions such as current cash, emergency months, minimum reserve, and monthly housing baseline.
