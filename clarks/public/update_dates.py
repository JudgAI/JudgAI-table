#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新html-order.html中的訂單日期範圍
Momo: 2025/09/02 到 2025/11/07
Clarks: 2025/11/08 到 2026/01/30
"""

from datetime import datetime, timedelta
import re

# 讀取HTML文件
with open('html - order.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Momo日期列表
momo_dates = [
    '2025/09/02', '2025/09/07', '2025/09/08', '2025/09/09', '2025/09/12', 
    '2025/09/18', '2025/09/21', '2025/09/23', '2025/09/24', '2025/09/25', 
    '2025/09/26', '2025/09/27', '2025/09/29', '2025/10/02', '2025/10/06', 
    '2025/10/10', '2025/10/11', '2025/10/12', '2025/10/20', '2025/10/21', 
    '2025/10/24', '2025/10/26', '2025/10/27', '2025/10/28', '2025/10/29', 
    '2025/10/30', '2025/11/02', '2025/11/07'
]

# Clarks日期列表
clarks_dates = [
    '2025/11/08', '2025/11/10', '2025/11/11', '2025/11/14', '2025/11/15', 
    '2025/11/26', '2025/11/27', '2025/11/28', '2025/11/30', '2025/12/01', 
    '2025/12/02', '2025/12/03', '2025/12/04', '2025/12/06', '2025/12/07', 
    '2025/12/17', '2025/12/18', '2025/12/24', '2025/12/26', '2025/12/27', 
    '2026/01/08', '2026/01/16', '2026/01/18', '2026/01/20', '2026/01/22', 
    '2026/01/26', '2026/01/29', '2026/01/30'
]

def add_days(date_str, days):
    """為日期增加天數"""
    date_obj = datetime.strptime(date_str, '%Y/%m/%d')
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime('%Y/%m/%d')

# 找到Momo表的tbody
momo_pattern = r'(id="multiverceTable".*?<tbody>)(.*?)(</tbody>\s*</div>\s*<div class="insight-box">)'
momo_match = re.search(momo_pattern, content, re.DOTALL)

if momo_match:
    # 替換Momo日期
    momo_tbody = momo_match.group(2)
    rows = re.findall(r'<tr>.*?</tr>', momo_tbody, re.DOTALL)
    
    print(f"找到 {len(rows)} 行 Momo 訂單")
    
    new_momo_tbody = ''
    for i, row in enumerate(rows[:28]):  # 只更新前28行
        if i < len(momo_dates):
            purchase_date = momo_dates[i]
            predicted_date = add_days(purchase_date, 1)
            actual_date = add_days(purchase_date, 2)
            
            # 更新日期
            row = re.sub(
                r'<td>\d{4}/\d{2}/\d{2}</td>',  # 購買日期 (第2列)
                f'<td>{purchase_date}</td>',
                row,
                count=1
            )
            
            # 替換所有日期
            date_cols = re.findall(r'<td>\d{4}/\d{2}/\d{2}</td>', row)
            for j, date_col in enumerate(date_cols):
                if j == 0:  # 已經處理購買日期
                    continue
                elif j == 1:  # 預計配送
                    row = row.replace(date_col, f'<td>{predicted_date}</td>', 1)
                elif j == 2:  # 實際配送
                    row = row.replace(date_col, f'<td>{actual_date}</td>', 1)
            
            new_momo_tbody += row
        else:
            break
    
    content = content.replace(momo_match.group(2), new_momo_tbody)
    print(f"✅ 已更新 Momo 表的 {min(len(rows), 28)} 行日期")

# 找到Clarks表的tbody
clarks_pattern = r'(id="carrefourTable".*?<tbody>)(.*?)(</tbody>\s*</div>\s*<div class="insight-box">)'
clarks_match = re.search(clarks_pattern, content, re.DOTALL)

if clarks_match:
    # 替換Clarks日期
    clarks_tbody = clarks_match.group(2)
    rows = re.findall(r'<tr>.*?</tr>', clarks_tbody, re.DOTALL)
    
    print(f"找到 {len(rows)} 行 Clarks 訂單")
    
    new_clarks_tbody = ''
    for i, row in enumerate(rows[:28]):  # 只更新前28行
        if i < len(clarks_dates):
            purchase_date = clarks_dates[i]
            predicted_date = add_days(purchase_date, 1)
            actual_date = add_days(purchase_date, 2)
            
            # 更新日期
            row = re.sub(
                r'<td>\d{4}/\d{2}/\d{2}</td>',  # 購買日期 (第2列)
                f'<td>{purchase_date}</td>',
                row,
                count=1
            )
            
            # 替換所有日期
            date_cols = re.findall(r'<td>\d{4}/\d{2}/\d{2}</td>', row)
            for j, date_col in enumerate(date_cols):
                if j == 0:  # 已經處理購買日期
                    continue
                elif j == 1:  # 預計配送
                    row = row.replace(date_col, f'<td>{predicted_date}</td>', 1)
                elif j == 2:  # 實際配送
                    row = row.replace(date_col, f'<td>{actual_date}</td>', 1)
            
            new_clarks_tbody += row
        else:
            break
    
    content = content.replace(clarks_match.group(2), new_clarks_tbody)
    print(f"✅ 已更新 Clarks 表的 {min(len(rows), 28)} 行日期")

# 更新數據週期信息
content = re.sub(
    r'📅 數據週期:.*?</span>',
    '📅 數據週期: 2025年9月~2026年1月</span>',
    content
)

# 寫入文件
with open('html - order.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 完成！文件已更新")
