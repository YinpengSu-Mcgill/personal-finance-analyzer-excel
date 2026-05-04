# Personal Finance Analyzer Excel Template

A bilingual Excel-based personal finance analyzer for tracking expenses, summarizing monthly cash flow, estimating emergency funds, and calculating investable cash.

This project uses a **three-layer spreadsheet architecture**:

```text
Input Sheets → Calculation Hub → Dashboard / Summary Sheets
```

It is designed as a reusable template for personal finance tracking, financial modeling practice, and data analysis portfolio demonstration.

---

## Templates

| File | Language | Purpose |
|---|---|---|
| `templates/Personal_Finance_Analyzer_Template_2026_English_Public.xlsx` | English | Main public GitHub template |
| `templates/个人财务分析模板_2026全年续用_公开版.xlsx` | Chinese | Chinese public template |

Both templates contain no personal financial data.

---

## Features

- Expense and income tracking
- Monthly cash flow summary
- Category-level spending breakdown
- Annual expense projection
- Emergency fund calculation
- Investable cash estimation
- Formula hub architecture
- Chinese and English templates
- Public sample version with no personal/private data

---

## Workbook Structure

| Sheet | Purpose |
|---|---|
| `Expenses` / `总支出` | Root data source for all expense records |
| `Income` / `总收入` | Root data source for all income records |
| `Input_Settings` / `输入设置` | Manual assumptions such as current cash and emergency fund months |
| `Calculation_Hub` / `公式枢纽` | Central formula layer that calculates all key metrics |
| `Dashboard` / `总览_简洁` | Simplified visual summary |
| `Monthly_Summary` / `每月总结` | Monthly income, expense, and cash flow summary |
| `Category_Summary` / `各类别总结` | Spending breakdown by category |
| `Annual_Projection` / `年度消费预测` | Lean, Normal, and Conservative annual expense scenarios |
| `Emergency_Fund` / `保障金分析` | 3-month, 6-month, 12-month, and custom emergency fund calculations |
| `Investable_Cash` / `可投资资金` | Cash reserve and investable cash guidance |
| `Formula_Guide` / `公式说明与维护规则` | Formula explanation and maintenance rules |

---

## How to Use

1. Add expense records to the `Expenses` sheet.
2. Add income records to the `Income` sheet.
3. Update assumptions in `Input_Settings`.
4. Review the results in `Dashboard`.
5. Use `Calculation_Hub` and `Formula_Guide` to understand the formula logic.

---

## Data Rules

- Expenses should be entered as negative numbers.
- Income should be entered as positive numbers.
- Personal living expenses should use `Analysis_Treatment = Personal_Expense`.
- Transfers, investments, and property-related cash flows should be separated from personal expenses.
- The dashboard is driven by formulas, so users only need to update the input sheets.

---

## Formula Logic

The main Excel formulas include:

| Formula | Purpose |
|---|---|
| `SUMIFS` | Conditional aggregation by month, category, and treatment |
| `IF` | Rule-based logic |
| `IFERROR` | Error handling |
| `INDEX + MATCH` | Month-based lookup from input settings |
| `MAX` | Emergency reserve and investable cash calculation |

More details are available in [`docs/formula-guide.md`](docs/formula-guide.md).

---

## Privacy

This template contains no personal financial data. All calculations are performed locally in Excel.

---

## Disclaimer

This project is for educational and personal finance tracking purposes only. It does not provide personalized investment, tax, legal, or accounting advice.

---

## Future Plan

The next stage is to convert this Excel model into a browser-based web app:

```text
Upload Excel / CSV → Parse data locally → Generate dashboard → Export summary
```

See [`docs/roadmap-web-app.md`](docs/roadmap-web-app.md).
