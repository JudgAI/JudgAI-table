#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json
import re

# 读取HTML文件
file_path = r"c:\Users\User\Documents\judi ai\JudgAI-table\clarks\爬蟲csv\☀️26春夏新品 _ ☀️26春夏新品商品推薦 _ Clarks.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# 查找所有可能的商品容器
# 通常商品卡片会使用特定的class名称
products = []

# 方案1：查找所有可能的商品卡片div
# 寻找包含商品信息的元素
print("=" * 80)
print("正在分析HTML结构...")
print("=" * 80)

# 查找是否有预加载的数据或JSON数据
scripts = soup.find_all('script', type='text/javascript')
print(f"找到 {len(scripts)} 个JavaScript脚本标签")

# 查找PRELOADED_STATE或其他数据源
for i, script in enumerate(scripts):
    if script.string and '__PRELOADED_STATE__' in str(script.string)[:500]:
        print(f"脚本 {i}: 找到 __PRELOADED_STATE__ 标记")
        try:
            # 尝试提取JSON数据
            content = str(script.string)
            # 查找JSON内容
            start_idx = content.find('{')
            end_idx = content.rfind('}')
            if start_idx != -1 and end_idx != -1:
                json_str = content[start_idx:end_idx+1]
                # 尝试解析JSON
                data = json.loads(json_str)
                print("✓ 成功解析PRELOADED_STATE数据")
                
                # 遍历数据寻找商品信息
                def find_products_in_data(obj, depth=0):
                    products_found = []
                    if depth > 10:
                        return products_found
                    
                    if isinstance(obj, dict):
                        for key, value in obj.items():
                            if 'product' in key.lower() or 'item' in key.lower() or 'sale' in key.lower():
                                products_found.extend(find_products_in_data(value, depth+1))
                            else:
                                products_found.extend(find_products_in_data(value, depth+1))
                    elif isinstance(obj, list):
                        for item in obj:
                            products_found.extend(find_products_in_data(item, depth+1))
                    
                    return products_found
                
                found = find_products_in_data(data)
                if found:
                    print(f"在嵌套数据中找到 {len(found)} 个潜在商品")
                    
        except Exception as e:
            print(f"✗ 无法解析脚本 {i}: {str(e)[:100]}")

print("\n" + "=" * 80)
print("查找DOM中的商品元素...")
print("=" * 80)

# 查找所有可能的商品卡片容器
# 通常会有特定的class或结构
possible_containers = soup.find_all(['div', 'article', 'li', 'section'])
print(f"找到 {len(possible_containers)} 个容器元素")

# 查找包含价格和商品名称的元素
price_patterns = [
    soup.find_all(string=re.compile(r'NT\$\s*\d+|NT\$\d+|\$\s*\d+|¥\d+|\d+\s*元')),
    soup.find_all('span', class_=re.compile(r'price|cost|amount')),
    soup.find_all('div', class_=re.compile(r'price|cost|amount'))
]

print("\n找到的价格相关元素:")
all_price_elements = []
for pattern_results in price_patterns:
    if pattern_results:
        all_price_elements.extend(pattern_results)
        print(f"  - 找到 {len(pattern_results)} 个价格相关元素")

# 查找商品名称元素
name_elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'a'])
print(f"找到 {len(name_elements)} 个标题/链接元素")

# 查找所有可能包含商品ID/SKU的元素
sku_patterns = [
    soup.find_all(string=re.compile(r'[A-Z]{2,}\d{4,}|SKU|sku|货号')),
    soup.find_all(['span', 'div', 'p'], class_=re.compile(r'sku|id|code|product-code'))
]

print("\n找到的SKU/代码相关元素:")
for pattern_results in sku_patterns:
    if pattern_results:
        print(f"  - 找到 {len(pattern_results)} 个SKU相关元素")

# 尝试查找商品卡片结构
print("\n" + "=" * 80)
print("分析商品卡片结构...")
print("=" * 80)

# 查找最可能是商品卡片的div
potential_product_cards = []

# 方案1：查找包含图片、名称、价格的容器
images = soup.find_all('img')
print(f"找到 {len(images)} 个图片元素")

# 获取最大的图片容器
for img in images[:10]:
    parent = img.parent
    if parent:
        # 查找该图片的容器链
        container = parent
        for _ in range(5):
            if container.parent:
                container = container.parent
                # 检查是否包含多个子元素（可能是商品卡片）
                if len(container.find_all(['img', 'span', 'div'])) > 3:
                    text_content = container.get_text(strip=True)
                    if len(text_content) > 10:
                        break

# 查找所有 <a> 标签，这些通常链接到商品详情页面
product_links = soup.find_all('a', href=re.compile(r'product|item|detail|goods', re.I))
print(f"找到 {len(product_links)} 个可能的商品链接")

print("\n" + "=" * 80)
print("尝试通过JSON数据提取...")
print("=" * 80)

# 查找所有JSON数据
json_scripts = soup.find_all('script', type='application/json')
print(f"找到 {len(json_scripts)} 个JSON脚本")

for script in json_scripts:
    try:
        data = json.loads(script.string)
        print(f"✓ 成功解析JSON: {str(data)[:100]}...")
    except:
        pass

# 再次尝试在nineyi变量中查找数据
for script in scripts:
    if script.string and 'nineyi' in str(script.string)[:500]:
        content = str(script.string)
        if '__PRELOADED_STATE__' in content:
            try:
                # 提取JSON部分
                match = re.search(r'nineyi\.__PRELOADED_STATE__\s*=\s*({.*?});', content, re.DOTALL)
                if match:
                    json_str = match.group(1)
                    data = json.loads(json_str)
                    
                    # 在PRELOADED_STATE中查找商品数据
                    def extract_products(data, products=[]):
                        if isinstance(data, dict):
                            for key, value in data.items():
                                if key in ['products', 'items', 'productList', 'goodsList']:
                                    if isinstance(value, list):
                                        for item in value:
                                            if isinstance(item, dict):
                                                products.append(item)
                                extract_products(value, products)
                        elif isinstance(data, list):
                            for item in data:
                                extract_products(item, products)
                        return products
                    
                    extracted = extract_products(data, [])
                    print(f"从__PRELOADED_STATE__中提取了 {len(extracted)} 个商品")
                    
                    if extracted:
                        print("\n提取的商品数据示例:")
                        for i, prod in enumerate(extracted[:3]):
                            print(f"\n商品 {i+1}:")
                            print(json.dumps(prod, indent=2, ensure_ascii=False)[:300])
                    
            except Exception as e:
                print(f"✗ 解析失败: {str(e)}")

print("\n" + "=" * 80)
print("总结")
print("=" * 80)
print("这是一个动态加载的页面，商品数据可能存储在JavaScript变量中。")
print("需要用Selenium或其他浏览器自动化工具来获取渲染后的内容。")
print("或者需要检查网络请求来找到API端点。")
