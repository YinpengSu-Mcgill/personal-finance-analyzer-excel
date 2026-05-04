# Formula Guide

This document explains the main formulas used in the Personal Finance Analyzer Excel Template.

## Architecture

```text
Expenses / Income / Input Settings
        ↓
Calculation Hub
        ↓
Dashboard / Monthly Summary / Category Summary / Annual Projection / Emergency Fund / Investable Cash
```

The workbook separates raw inputs, formula logic, and presentation pages. This makes the model easier to maintain and easier to convert into a web application later.

---

## Core Formula Types

### 1. SUMIFS

Used for conditional aggregation.

```excel
=SUMIFS(amount_range, condition_range_1, condition_1, condition_range_2, condition_2)
```

Example logic:

```text
Sum all personal expenses where:
- Month = selected month
- Analysis_Treatment = Personal_Expense
```

Because expenses are stored as negative numbers, the dashboard often uses:

```excel
=-SUMIFS(...)
```

This displays expenses as positive values in summaries.

---

### 2. IF

Used for rule-based logic.

```excel
=IF(condition, value_if_true, value_if_false)
```

Example:

```excel
=IF(active_month_count=0,0,total_expense/active_month_count)
```

This prevents division errors when no monthly data exists.

---

### 3. IFERROR

Used for error handling.

```excel
=IFERROR(formula, fallback_value)
```

Example:

```excel
=IFERROR(current_cash/average_monthly_expense,0)
```

If the denominator is zero, the result becomes 0 instead of an Excel error.

---

### 4. INDEX + MATCH

Used for month-based lookup.

```excel
=INDEX(value_range,1,MATCH(target_month,month_header_range,0))
```

Example logic:

```text
Find the monthly housing baseline for the selected month from Input Settings.
```

---

### 5. MAX

Used for reserve calculations and downside protection.

```excel
=MAX(0,current_cash-recommended_cash_reserve)
```

This ensures investable cash never displays as a negative number.

---

## Key Metrics

| Metric | Logic |
|---|---|
| Total Income | Sum income records by month |
| Personal Expense | Sum expenses with `Analysis_Treatment = Personal_Expense` |
| Average Monthly Expense | Total personal expense / active months |
| Essential Expense | Personal expenses marked as `Essential` |
| Discretionary Expense | Personal expenses marked as `Discretionary` |
| Annual Normal Projection | Average monthly expense × 12 |
| Annual Lean Projection | Average monthly essential expense × 12 |
| Annual Conservative Projection | Highest monthly expense × 12 |
| Recommended Cash Reserve | max(monthly expense × emergency months, minimum reserve) + extra buffer |
| Investable Cash | max(0, current cash - recommended cash reserve) |

---

## Spreadsheet-to-Web Mapping

Excel logic can be converted into JavaScript as follows:

| Excel | Web App Equivalent |
|---|---|
| `SUMIFS` | `filter()` + `reduce()` |
| `IF` | `if / else` or ternary operator |
| `IFERROR` | safe fallback logic |
| `INDEX + MATCH` | object lookup by month key |
| Dashboard sheet | React dashboard component |
| Calculation Hub | data calculation utility functions |

Example JavaScript equivalent of personal expense calculation:

```js
const personalExpense = expenses
  .filter(row => row.month === month && row.analysisTreatment === 'Personal_Expense')
  .reduce((sum, row) => sum + Math.abs(row.amount), 0);
```
