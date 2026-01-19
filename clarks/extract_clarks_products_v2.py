#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re

# 读取HTML文件
file_path = r"c:\Users\User\Documents\judi ai\JudgAI-table\clarks\爬蟲csv\☀️26春夏新品 _ ☀️26春夏新品商品推薦 _ Clarks.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# 提取商品数据
products = []

# 查找所有商品卡片元素
# 根据HTML结构，每个商品卡片都在一个特定的div结构中
product_links = soup.find_all('a', class_=re.compile('product-card__vertical'))

print(f"找到 {len(product_links)} 个商品卡片\n")
print("=" * 80)
print("Clarks 26春夏新品 - 商品提取列表")
print("=" * 80)
print("商品名稱 | 價格 | SKU")
print("-" * 80)

found_products = []

for idx, link in enumerate(product_links, 1):
    try:
        # 获取商品名称
        name_elem = link.find(string=re.compile(r'Clarks'))
        name = name_elem.strip() if name_elem else "未知"
        
        # 获取价格（最后显示的价格）
        # 查找data-qe-id="body-price-text"属性的div
        price_elem = link.find('div', attrs={'data-qe-id': 'body-price-text'})
        price = price_elem.get_text(strip=True) if price_elem else "未知"
        
        # 获取alt文本中的SKU/产品代码
        img_elem = link.find('img', class_=re.compile('product-card__vertical__media'))
        sku = ""
        if img_elem and img_elem.get('alt'):
            alt_text = img_elem['alt']
            # 从alt文本中提取SKU（通常是最后的产品代码，如CLM87320C）
            match = re.search(r'(CL[A-Z]\d+C)', alt_text)
            if match:
                sku = match.group(1)
        
        if name and name != "未知":
            product_data = f"{name} | {price} | {sku}"
            print(product_data)
            found_products.append({
                'name': name,
                'price': price,
                'sku': sku
            })
    except Exception as e:
        print(f"错误: 处理第{idx}个商品时出错: {str(e)}")

print("-" * 80)
print(f"\n总共找到 {len(found_products)} 个商品")

# 验证数据
print("\n" + "=" * 80)
print("数据验证")
print("=" * 80)

# 检查重复
unique_names = set(p['name'] for p in found_products)
unique_skus = set(p['sku'] for p in found_products if p['sku'])

print(f"✓ 总商品数: {len(found_products)}")
print(f"✓ 唯一商品名称数: {len(unique_names)}")
print(f"✓ 唯一SKU数: {len(unique_skus)}")
print(f"✓ 有有效SKU的商品数: {len([p for p in found_products if p['sku']])}")

# 检查价格格式
prices_with_nt = [p for p in found_products if 'NT$' in p['price']]
print(f"✓ 格式正确的价格（NT$）: {len(prices_with_nt)}/{len(found_products)}")

# 检查是否有空值
empty_names = [p for p in found_products if not p['name'] or p['name'] == '未知']
empty_prices = [p for p in found_products if not p['price'] or p['price'] == '未知']
empty_skus = [p for p in found_products if not p['sku']]

print(f"✓ 无效商品名称: {len(empty_names)}")
print(f"✓ 无效价格: {len(empty_prices)}")
print(f"✓ 缺失SKU: {len(empty_skus)}")

# 显示详细信息
print("\n" + "=" * 80)
print("商品详细列表 (JSON格式)")
print("=" * 80)

import json
print(json.dumps(found_products, ensure_ascii=False, indent=2))

# 导出为CSV
print("\n" + "=" * 80)
print("导出为CSV格式")
print("=" * 80)

csv_content = "商品名稱,價格,SKU\n"
for p in found_products:
    # 防止CSV中的逗号破坏格式
    name_escaped = f'"{p["name"]}"' if ',' in p["name"] else p["name"]
    csv_content += f'{name_escaped},{p["price"]},{p["sku"]}\n'

output_file = r"c:\Users\User\Documents\judi ai\JudgAI-table\clarks_products_extracted.csv"
with open(output_file, 'w', encoding='utf-8-sig') as f:
    f.write(csv_content)

print(f"✓ CSV文件已保存至: {output_file}")
print(f"✓ 共 {len(found_products)} 行商品数据（含表头）")

