#!/usr/bin/env python3
"""Validate that the Chinese and English templates contain the expected sheets."""
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
ROOT = Path(__file__).resolve().parents[1]

EXPECTED = {
    'templates/Personal_Finance_Template_2026_ZH.xlsx': [
        '使用说明','总览','总支出','总收入','输入设置','税费设置','每月总结','各类别总结',
        '消费税分析','公式枢纽','税费计算明细','年度消费预测','保障金分析','可投资资金','公式说明','选项'
    ],
    'templates/Personal_Finance_Template_2026_EN.xlsx': [
        'Instructions','Dashboard','Expense_Input','Income_Input','Input_Settings','Sales_Tax_Settings',
        'Monthly_Summary','Category_Summary','Sales_Tax_Analysis','Formula_Hub','Sales_Tax_Detail',
        'Annual_Projection','Emergency_Fund','Investable_Cash','Formula_Notes','Lists'
    ],
}

def sheet_names(path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read('xl/workbook.xml'))
        return [sheet.attrib['name'] for sheet in root.find('main:sheets', NS)]

ok = True
for rel_path, expected in EXPECTED.items():
    path = ROOT / rel_path
    if not path.exists():
        print(f'MISSING: {rel_path}')
        ok = False
        continue
    actual = sheet_names(path)
    missing = [s for s in expected if s not in actual]
    extra = [s for s in actual if s not in expected]
    if missing or extra:
        print(f'CHECK FAILED: {rel_path}')
        print('  Missing:', missing)
        print('  Extra:', extra)
        ok = False
    else:
        print(f'OK: {rel_path}')

sys.exit(0 if ok else 1)
