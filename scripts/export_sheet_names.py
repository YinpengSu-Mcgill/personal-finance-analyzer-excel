#!/usr/bin/env python3
"""Export sheet names from an .xlsx file without external dependencies."""
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

if len(sys.argv) < 2:
    print('Usage: python scripts/export_sheet_names.py <workbook.xlsx>')
    sys.exit(1)

path = sys.argv[1]
with zipfile.ZipFile(path) as z:
    root = ET.fromstring(z.read('xl/workbook.xml'))
    for sheet in root.find('main:sheets', NS):
        print(sheet.attrib['name'])
