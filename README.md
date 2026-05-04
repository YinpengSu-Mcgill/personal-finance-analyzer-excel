# Personal Finance Analyzer Excel Template

A bilingual Excel-based personal finance analyzer for tracking expenses, summarizing monthly cash flow, estimating emergency funds, and calculating investable cash.

This project uses a three-layer spreadsheet architecture:

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
- Chinese and English Excel templates
- Public sample version with no personal/private data

---

## Workbook Structure

| Sheet | Purpose |
|---|---|
| `Expenses` / `总支出` | Root data source for all expense records |
| `Income` / `总收入` | Root data source for all income records |
| `Input_Settings` / `输入设置` | Manual assumptions such as current cash, extra buffer, emergency fund months, and housing baseline |
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
- The dashboard is formula-driven, so users only need to update the input sheets.

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

---

# 个人财务分析器 Excel 模板

一款基于 Excel 的双语个人财务分析工具，用于跟踪支出、汇总每月现金流、估算应急资金，并计算可投资现金。

本项目采用三层电子表格架构：

```text
输入表 → 公式枢纽 → 总览 / 汇总表
```

它被设计为一个可重复使用的模板，可用于个人财务跟踪、财务建模练习，以及数据分析作品集展示。

---

## 模板文件

| 文件 | 语言 | 用途 |
|---|---|---|
| `templates/Personal_Finance_Analyzer_Template_2026_English_Public.xlsx` | 英文 | 主要 GitHub 公开模板 |
| `templates/个人财务分析模板_2026全年续用_公开版.xlsx` | 中文 | 中文公开模板 |

两个模板均不包含任何个人财务数据。

---

## 功能特点

- 支出与收入记录
- 月度现金流汇总
- 按类别拆分支出结构
- 年度消费预测
- 应急资金测算
- 可投资现金估算
- 公式枢纽架构
- 中文与英文 Excel 模板
- 无个人隐私数据的公开示例版本

---

## 工作簿结构

| 工作表 | 用途 |
|---|---|
| `Expenses` / `总支出` | 所有支出记录的根数据源 |
| `Income` / `总收入` | 所有收入记录的根数据源 |
| `Input_Settings` / `输入设置` | 手动输入当前现金、额外缓冲、备用金月数、住房底盘等假设 |
| `Calculation_Hub` / `公式枢纽` | 统一计算所有关键指标的中央公式层 |
| `Dashboard` / `总览_简洁` | 简化后的可视化总览页 |
| `Monthly_Summary` / `每月总结` | 月度收入、支出与现金流汇总 |
| `Category_Summary` / `各类别总结` | 按类别划分的支出结构 |
| `Annual_Projection` / `年度消费预测` | Lean、Normal、Conservative 三种年度消费情景 |
| `Emergency_Fund` / `保障金分析` | 3个月、6个月、12个月以及自定义月份的备用金测算 |
| `Investable_Cash` / `可投资资金` | 现金储备、现金缺口与可投资资金判断 |
| `Formula_Guide` / `公式说明与维护规则` | 公式说明与维护规则 |

---

## 使用方式

1. 在 `Expenses` / `总支出` 表中追加支出记录。
2. 在 `Income` / `总收入` 表中追加收入记录。
3. 在 `Input_Settings` / `输入设置` 中更新现金、备用金月数等假设。
4. 在 `Dashboard` / `总览_简洁` 中查看结果。
5. 通过 `Calculation_Hub` / `公式枢纽` 和 `Formula_Guide` / `公式说明与维护规则` 理解公式逻辑。

---

## 数据规则

- 支出金额应输入为负数。
- 收入金额应输入为正数。
- 个人生活支出应使用 `Analysis_Treatment = Personal_Expense`。
- 转账、投资以及房产相关现金流应与个人生活支出分开。
- 仪表盘由公式驱动，用户只需要更新输入表。

---

## 公式逻辑

主要 Excel 公式包括：

| 公式 | 用途 |
|---|---|
| `SUMIFS` | 按月份、类别和分析口径进行条件汇总 |
| `IF` | 基于规则的逻辑判断 |
| `IFERROR` | 错误处理 |
| `INDEX + MATCH` | 从输入设置中按月份查找数据 |
| `MAX` | 计算备用金、现金储备和可投资资金 |

更多说明可查看 [`docs/formula-guide.md`](docs/formula-guide.md)。

---

## 隐私说明

本模板不包含任何个人财务数据。所有计算均在本地 Excel 中完成。

---

## 免责声明

本项目仅用于教育学习和个人财务跟踪，不提供个性化投资、税务、法律或会计建议。

---

## 后续计划

下一阶段计划将该 Excel 模型转换为基于浏览器的网页应用：

```text
上传 Excel / CSV → 本地解析数据 → 生成仪表盘 → 导出汇总结果
```

详情见 [`docs/roadmap-web-app.md`](docs/roadmap-web-app.md)。
