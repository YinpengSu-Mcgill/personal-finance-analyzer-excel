# Personal Finance Excel BI Template

A bilingual Excel-based personal finance analysis project for monthly bookkeeping, spending analysis, Canadian GST/QST estimation, emergency fund planning and investable cash judgment.

![Dashboard overview](screenshots/01_dashboard_overview.png)

## What this project does

This repository turns a personal Excel workbook into a reusable finance-analysis template. It is designed for people who want to keep the input process simple while still getting dashboard-style outputs.

Core functions:

- record monthly expenses and income with positive amounts;
- separate personal expenses, rental-property cash flow, transfers and investment-related movements;
- summarize monthly cash flow and category spending;
- estimate annual spending under Lean, Normal and Conservative scenarios;
- calculate emergency-fund requirements;
- estimate investable cash after keeping a safety reserve;
- estimate Canadian GST/QST impact for daily consumption categories.

## Templates included

| File | Language | Use |
|---|---|---|
| `templates/Personal_Finance_Template_2026_ZH.xlsx` | Chinese | Original Chinese template |
| `templates/Personal_Finance_Template_2026_EN.xlsx` | English | Fully translated English template |

## Example data

The workbook already includes **Month 1 and Month 2 sample data**. These sample records are provided as starter examples for personal data input. You can replace them with your own records, or keep them as a format reference.

CSV versions are also provided under:

```text
examples/sample_data_jan_feb/
```

![Input workflow](screenshots/02_input_workflow.png)

## Repository structure

![Repository structure](screenshots/03_folder_structure.png)

```text
personal-finance-excel-bi-template/
├── README.md
├── README.zh-CN.md
├── README.en.md
├── templates/
├── examples/sample_data_jan_feb/
├── screenshots/
├── docs/
└── scripts/
```

## Workbook modules

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

## Quick start

1. Download either the Chinese or English template from `templates/`.
2. Open the workbook in Excel.
3. Edit only the input sheets: Expense Input, Income Input, Input Settings and Sales Tax Settings.
4. Keep amounts positive in both income and expense tables.
5. Use Month 1 and Month 2 examples as input patterns.
6. Review the Dashboard, Monthly Summary, Category Summary, Emergency Fund and Investable Cash sheets.
7. When publishing this repository publicly, keep real personal transactions out of GitHub.

## Privacy note

Personal finance data is sensitive. This repository is structured to publish templates and anonymized examples only. Keep real bank records, tax documents, screenshots and account balances in a private folder outside the repository.

## Disclaimer

This workbook is a personal finance analysis tool. It is not professional tax, legal, accounting or investment advice. Verify tax treatment and investment decisions with qualified professionals when needed.
