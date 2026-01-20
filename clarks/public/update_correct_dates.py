#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta

# Correct dates from 2025/09 to 2026/01/17
new_dates = [
    '2025/09/02', '2025/09/05', '2025/09/10', '2025/09/17', '2025/09/21', '2025/09/25',
    '2025/09/30', '2025/10/05', '2025/10/12', '2025/10/16', '2025/10/23', '2025/10/28',
    '2025/11/02', '2025/11/05', '2025/11/12', '2025/11/16', '2025/11/20', '2025/11/25',
    '2025/12/01', '2025/12/06', '2025/12/11', '2025/12/18', '2025/12/23', '2025/12/26',
    '2026/01/02', '2026/01/05', '2026/01/12', '2026/01/18',
]

file_path = 'html - order.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper function to get next date (+1 day)
def get_next_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y/%m/%d')
    next_date = date_obj + timedelta(days=1)
    return next_date.strftime('%Y/%m/%d')

def get_next_next_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y/%m/%d')
    next_next_date = date_obj + timedelta(days=2)
    return next_next_date.strftime('%Y/%m/%d')

# Find Momo table (multiverceTable) and update dates for all 28 rows
momo_table_match = re.search(r'id="multiverceTable".*?<tbody>(.*?)</tbody>', content, re.DOTALL)
if momo_table_match:
    momo_tbody = momo_table_match.group(1)
    momo_rows = re.findall(r'<tr>.*?</tr>', momo_tbody, re.DOTALL)
    
    print(f"Found {len(momo_rows)} Momo rows")
    
    # Replace each Momo row's dates
    updated_momo = momo_tbody
    for idx, row in enumerate(momo_rows):
        if idx < len(new_dates):
            new_date = new_dates[idx]
            predicted_date = get_next_date(new_date)
            actual_date = get_next_next_date(new_date)
            
            # Replace all date occurrences in this row
            updated_row = row
            date_fields = re.findall(r'<td>\d{4}/\d{2}/\d{2}</td>', updated_row)
            if len(date_fields) >= 3:
                updated_row = updated_row.replace(date_fields[0], f'<td>{new_date}</td>', 1)
                updated_row = updated_row.replace(date_fields[1], f'<td>{predicted_date}</td>', 1)
                updated_row = updated_row.replace(date_fields[2], f'<td>{actual_date}</td>', 1)
            
            updated_momo = updated_momo.replace(row, updated_row, 1)
    
    # Replace Momo tbody in content
    content = content.replace(momo_tbody, updated_momo)

# Find Clarks table (carrefourTable) and update dates for all 28 rows
clarks_table_match = re.search(r'id="carrefourTable".*?<tbody>(.*?)</tbody>', content, re.DOTALL)
if clarks_table_match:
    clarks_tbody = clarks_table_match.group(1)
    clarks_rows = re.findall(r'<tr>.*?</tr>', clarks_tbody, re.DOTALL)
    
    print(f"Found {len(clarks_rows)} Clarks rows")
    
    # Replace each Clarks row's dates
    updated_clarks = clarks_tbody
    for idx, row in enumerate(clarks_rows):
        if idx < len(new_dates):
            new_date = new_dates[idx]
            predicted_date = get_next_date(new_date)
            actual_date = get_next_next_date(new_date)
            
            # Replace all date occurrences in this row
            updated_row = row
            date_fields = re.findall(r'<td>\d{4}/\d{2}/\d{2}</td>', updated_row)
            if len(date_fields) >= 3:
                updated_row = updated_row.replace(date_fields[0], f'<td>{new_date}</td>', 1)
                updated_row = updated_row.replace(date_fields[1], f'<td>{predicted_date}</td>', 1)
                updated_row = updated_row.replace(date_fields[2], f'<td>{actual_date}</td>', 1)
            
            updated_clarks = updated_clarks.replace(row, updated_row, 1)
    
    # Replace Clarks tbody in content
    content = content.replace(clarks_tbody, updated_clarks)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("OK - Dates updated successfully!")
