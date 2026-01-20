import re

with open('html - order.html', 'r', encoding='utf-8') as f:
    content = f.read()

def add_data_date_to_table(content, table_id):
    pattern = f'(<table id="{table_id}"[^>]*>.*?<tbody[^>]*>)(.*?)(</tbody>)'
    
    def process_tbody(match):
        prefix = match.group(1)
        tbody_content = match.group(2)
        suffix = match.group(3)
        
        row_pattern = r'(<tr)(.*?)(>.*?<td>.*?</td>.*?<td>)(\d{4}/\d{2}/\d{2})(</td>)'
        
        def add_date_attr(row_match):
            tr_start = row_match.group(1)
            tr_attrs = row_match.group(2)
            before_date = row_match.group(3)
            date_text = row_match.group(4)
            after_date = row_match.group(5)
            
            date_normalized = date_text.replace('/', '-')
            
            if 'data-date' not in tr_attrs:
                tr_attrs += f' data-date="{date_normalized}"'
            
            return f'{tr_start}{tr_attrs}>{before_date}{date_text}{after_date}'
        
        new_tbody = re.sub(row_pattern, add_date_attr, tbody_content)
        return prefix + new_tbody + suffix
    
    new_content = re.sub(pattern, process_tbody, content, flags=re.DOTALL)
    return new_content

print("处理 allOrdersTable...")
content = add_data_date_to_table(content, 'allOrdersTable')
print("✓ allOrdersTable 完成")

print("处理 multiverceTable...")
content = add_data_date_to_table(content, 'multiverceTable')
print("✓ multiverceTable 完成")

print("处理 carrefourTable...")
content = add_data_date_to_table(content, 'carrefourTable')
print("✓ carrefourTable 完成")

count = content.count('data-date=')
print(f"\n✓ 总共添加了 {count} 个 data-date 属性")

with open('html - order.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ 文件已保存")
