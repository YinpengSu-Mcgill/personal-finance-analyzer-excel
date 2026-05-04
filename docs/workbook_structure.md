# Workbook Structure / 工作簿结构

| Chinese Sheet | English Sheet | Purpose |
|---|---|---|
| `使用说明` | `Instructions` | How to use the workbook and monthly maintenance rules. |
| `总览` | `Dashboard` | Main dashboard for cash flow, spending, reserves and investable cash. |
| `总支出` | `Expense_Input` | Primary expense input table. Enter all expenses as positive amounts. |
| `总收入` | `Income_Input` | Primary income input table. Enter all income as positive amounts. |
| `输入设置` | `Input_Settings` | Manual settings such as current cash, reserve months and risk preference. |
| `税费设置` | `Sales_Tax_Settings` | GST/QST assumptions and taxability rules. |
| `每月总结` | `Monthly_Summary` | Monthly income, expense and cash-flow summary. |
| `各类别总结` | `Category_Summary` | Category-level monthly average, annualized amount and share of spending. |
| `消费税分析` | `Sales_Tax_Analysis` | Monthly GST/QST estimate and tax analysis. |
| `公式枢纽` | `Formula_Hub` | Central formula hub used by the dashboard and summary sheets. |
| `税费计算明细` | `Sales_Tax_Detail` | Line-by-line before-tax, GST, QST and after-tax calculation detail. |
| `年度消费预测` | `Annual_Projection` | Lean / Normal / Conservative annual spending projections. |
| `保障金分析` | `Emergency_Fund` | Emergency fund calculator for 3, 6 and 12 months. |
| `可投资资金` | `Investable_Cash` | Investable cash estimate after reserve requirements. |
| `公式说明` | `Formula_Notes` | Formula notes and maintenance rules. |
| `选项` | `Lists` | Dropdown lists and category dictionaries. |

## Design principle / 设计原则

- Input layer: expense, income and manual settings.
- Rule layer: dropdown lists, category dictionary and sales-tax assumptions.
- Calculation layer: formula hub and detailed tax calculation.
- Presentation layer: dashboard, monthly summary, category summary and reserve analysis.

---

- 输入层：支出、收入、手动设置。
- 规则层：下拉选项、类别字典、消费税假设。
- 计算层：公式枢纽与税费计算明细。
- 展示层：总览、每月总结、各类别总结和保障金分析。
