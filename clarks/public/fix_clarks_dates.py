#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Clarks table dates mapping - replace old 2025/10/XX with new Clarks dates (2025/11/08 ~ 2026/01/30)
clarks_date_mapping = {
    '2025/10/01': '2025/11/08',
    '2025/10/02': '2025/11/13',
    '2025/10/03': '2025/11/18',
}

# For rows beyond first 3, need to update with varied dates
# Let's read file and apply proper Clarks date mapping
file_path = 'html - order.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Clarks table rows span from CW-207700001 to CW-207700028
# Each old row has format with 2025/10/01, 2025/10/02, 2025/10/03 repeating

# Create complete mapping for all 56 order rows (need to handle all variations)
clarks_dates = [
    '2025/11/08', '2025/11/13', '2025/11/18', '2025/11/23', '2025/11/28',
    '2025/12/03', '2025/12/08', '2025/12/13', '2025/12/18', '2025/12/23',
    '2025/12/28', '2026/01/02', '2026/01/07', '2026/01/12', '2026/01/17',
    '2026/01/22', '2026/01/27', '2025/11/09', '2025/11/14', '2025/11/19',
    '2025/11/24', '2025/11/29', '2025/12/04', '2025/12/09', '2025/12/14',
    '2025/12/19', '2025/12/24', '2025/12/29',
]

# Find Clarks table start and end
carrefour_start = content.find('id="carrefourTable"')
carrefour_tbody_start = content.find('<tbody>', carrefour_start)
carrefour_tbody_end = content.find('</tbody>', carrefour_tbody_start)

# Count rows in Clarks table to find exact positions
clarks_section = content[carrefour_tbody_start:carrefour_tbody_end]

# Replace row by row - for first 28 Clarks rows only
row_count = 0
temp_content = content[:carrefour_tbody_start]
pos = carrefour_tbody_start

# Find and replace each Clarks row's dates
import re

for i in range(28):  # 28 Clarks rows
    # Find next row opening tag
    row_start = content.find('<tr>', pos)
    row_end = content.find('</tr>', row_start)
    
    if row_start == -1 or row_start > carrefour_tbody_end:
        break
    
    row_content = content[pos:row_end+5]
    
    # Replace all date occurrences in this row with new Clarks date
    # This row should have 3 date columns
    date_pattern = r'2025/10/0[1-3]'
    new_date = clarks_dates[i]
    updated_row = re.sub(date_pattern, new_date, row_content, count=3)
    
    temp_content += updated_row
    pos = row_end + 5

# Add remaining content after Clarks table
temp_content += content[pos:]
content = temp_content

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("OK")
