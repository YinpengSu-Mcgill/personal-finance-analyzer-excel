# User Guide

## 1. Download a Template

Use either the English or Chinese version from the `templates/` folder.

## 2. Fill Expense Records

Add records to the `Expenses` / `总支出` sheet.

Required rules:

- Expenses should be negative numbers.
- Personal expenses should use `Analysis_Treatment = Personal_Expense`.
- Transfers and investments should be separated from daily spending.

Example:

| Month | Date | Description | Amount | Main_Category | Analysis_Treatment |
|---|---|---|---:|---|---|
| 2026-01 | 2026-01-01 | Rent | -1200 | Housing | Personal_Expense |

## 3. Fill Income Records

Add records to the `Income` / `总收入` sheet.

Required rules:

- Income should be positive numbers.
- The `Month` format should be `YYYY-MM`.

## 4. Update Input Settings

Update current cash, emergency fund months, minimum cash reserve, and monthly housing baseline if needed.

## 5. Review Dashboard

Use the dashboard sheet as the main viewing page.

## 6. Refresh Formulas

If Excel does not update formulas automatically, use:

```text
Ctrl + Alt + F9
```

on Windows Excel to force recalculation.
