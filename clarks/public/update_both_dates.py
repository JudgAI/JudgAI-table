#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# New dates that should be used for both Momo and Clarks tables
new_dates = [
    '2025/09/03', '2025/09/06', '2025/09/11', '2025/09/19', '2025/09/23', '2025/09/28',
    '2025/10/03', '2025/10/09', '2025/10/16', '2025/10/20', '2025/10/27', '2025/11/01',
    '2025/11/07', '2025/11/10', '2025/11/18', '2025/11/22', '2025/11/27', '2025/12/02',
    '2025/12/08', '2025/12/13', '2025/12/18', '2025/12/26', '2025/12/31', '2026/01/04',
    '2026/01/11', '2026/01/15', '2026/01/22', '2026/01/28',
]

# Old Momo dates (currently used: 2025/09/02 ~ 2025/11/07)
old_momo_dates = [
    '2025/09/02', '2025/09/07', '2025/09/12', '2025/09/17', '2025/09/22', '2025/09/27',
    '2025/10/02', '2025/10/07', '2025/10/12', '2025/10/17', '2025/10/22', '2025/10/27',
    '2025/11/01', '2025/11/06',  # Only first 14 were used before
]

file_path = 'html - order.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find Momo table (multiverceTable) and update dates for all 28 rows
momo_table_match = re.search(r'id="multiverceTable".*?<tbody>(.*?)</tbody>', content, re.DOTALL)
if momo_table_match:
    momo_tbody = momo_table_match.group(1)
    momo_rows = re.findall(r'<tr>.*?</tr>', momo_tbody, re.DOTALL)
    
    print(f"Found {len(momo_rows)} Momo rows")
    
    # Replace each Momo row's dates (3 date columns per row)
    updated_momo = momo_tbody
    for idx, row in enumerate(momo_rows):
        if idx < len(new_dates):
            # Replace date columns: purchase date, predicted delivery, actual delivery
            new_date = new_dates[idx]
            predicted_date = (int(new_date.split('/')[0] + new_date.split('/')[1] + new_date.split('/')[2]) + 1).__str__()  # Simple approach
            
            # Parse new_date properly
            year, month, day = new_date.split('/')
            pred_day = int(day) + 1
            act_day = int(day) + 2
            
            # Handle month overflow
            if pred_day > 28:  # Simplified for most months
                pred_day = pred_day - 28
                month = str(int(month) + 1).zfill(2)
            
            if act_day > 28:
                act_day = act_day - 28
                month_act = str(int(month) + 1).zfill(2)
            else:
                month_act = month
            
            predicted_date = f"{year}/{month}/{str(pred_day).zfill(2)}"
            actual_date = f"{year}/{month_act}/{str(act_day).zfill(2)}"
            
            # Replace all date occurrences in this row with new dates
            updated_row = row
            # Find and replace the three date fields in order
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
            
            # Parse new_date properly
            year, month, day = new_date.split('/')
            pred_day = int(day) + 1
            act_day = int(day) + 2
            
            # Handle month overflow
            if pred_day > 28:
                pred_day = pred_day - 28
                month_pred = str(int(month) + 1).zfill(2)
            else:
                month_pred = month
            
            if act_day > 28:
                act_day = act_day - 28
                month_act = str(int(month) + 1).zfill(2)
            else:
                month_act = month
            
            predicted_date = f"{year}/{month_pred}/{str(pred_day).zfill(2)}"
            actual_date = f"{year}/{month_act}/{str(act_day).zfill(2)}"
            
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

print("OK")
