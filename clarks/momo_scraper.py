# ========================================
# Momo購物網商品爬蟲腳本
# 角色設定：資料工程師 & 網路爬蟲專家
# 任務：爬取 momo 購物網商品名稱和價格
# ========================================



import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# ========== 第1步：設定與初始化 ==========

# 目標網址
TARGET_URL = "https://www.momoshop.com.tw/category/DgrpCategory.jsp?d_code=1501202433&p_orderType=4&showType=chessboardType"

# 設定 User-Agent（偽裝身份為真實瀏覽器）
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# 儲存結果的檔名
OUTPUT_FILE = "momo_products.csv"

# ========== 第2步：設定 Selenium Chrome 選項 ==========

def setup_chrome_driver():
    """
    設定 Chrome 瀏覽器驅動程式
    
    作用：
    - 設定無頭模式（不顯示瀏覽器視窗，加快速度）
    - 設定 User-Agent 標頭，讓網站認為是真實使用者
    - 禁用圖片加載（加快速度）
    - 設定超時時間
    """
    
    chrome_options = Options()
    
    # ⚠️ 取消註解下面這行可以隱藏瀏覽器視窗（背景執行）
    # chrome_options.add_argument("--headless")
    
    # 注：目前已取消隱藏，可以看到爬蟲過程
    
    # 設定 User-Agent
    chrome_options.add_argument(f"user-agent={USER_AGENT}")
    
    # 禁用圖片加載（加快爬蟲速度）
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    
    # 避免被偵測為自動化工具
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # 設定視窗大小
    chrome_options.add_argument("--window-size=1920,1080")
    
    try:
        # 建立 Chrome 驅動程式（自動下載對應版本的 ChromeDriver）
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("✓ Chrome 驅動程式已成功啟動")
        return driver
    except Exception as e:
        print(f"✗ Chrome 驅動程式啟動失敗: {e}")
        print("  提示：確認網路連線正常，webdriver-manager 會自動下載 ChromeDriver")
        return None


# ========== 第3步：爬蟲主函數 ==========

def scrape_momo_products():
    """
    主要爬蟲函數
    
    流程：
    1. 啟動 Chrome 驅動程式
    2. 打開目標網址
    3. 等待頁面動態加載完成
    4. 提取商品資訊
    5. 儲存為 CSV 檔案
    """
    
    driver = setup_chrome_driver()
    
    if not driver:
        print("爬蟲啟動失敗，程式結束")
        return False
    
    products_data = []  # 儲存商品資訊的列表
    
    try:
        # ========== 步驟1：打開目標網址 ==========
        print(f"\n📍 正在打開網址: {TARGET_URL}")
        driver.get(TARGET_URL)
        
        # 等待3秒讓頁面基本加載
        time.sleep(3)
        
        # ========== 步驟2：等待動態內容加載 ==========
        print("⏳ 等待頁面內容加載... (等待8秒)")
        
        # 使用固定等待時間而不是條件等待，確保 JS 執行完畢
        time.sleep(8)
        
        print("✓ 頁面應已加載完成")
        
        # 額外等待2秒確保所有動態內容完全加載
        time.sleep(2)
        
        # ========== 額外步驟：滾動頁面以觸發動態加載 ==========
        print("📜 正在滾動頁面以加載更多商品...")
        for i in range(3):
            driver.execute_script("window.scrollBy(0, 500);")  # 向下滾動500像素
            time.sleep(1)
        
        # 滾動回頂部
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        
        # ========== 步驟3：提取商品資訊 ==========
        print("🔍 開始提取商品資訊...")
        
        # ========== 調試：先檢查頁面上的所有元素 ==========
        print("\n【頁面診斷】")
        
        # 檢查所有可能的商品容器
        containers = [
            ("prdListArea", driver.find_elements(By.CLASS_NAME, "prdListArea")),
            ("prdName", driver.find_elements(By.CLASS_NAME, "prdName")),
            ("current-price", driver.find_elements(By.CLASS_NAME, "current-price")),
            ("goodsItem", driver.find_elements(By.CLASS_NAME, "goodsItem")),
            ("product", driver.find_elements(By.CLASS_NAME, "product")),
        ]
        
        print(f"頁面上的商品容器檢查結果：")
        for container_name, elements in containers:
            print(f"  - {container_name}: 找到 {len(elements)} 個")
        
        # ========== 關鍵改進：用 prdName 直接找所有商品 ==========
        print("\n✓ 使用新策略：直接查找所有商品名稱")
        product_names = driver.find_elements(By.CLASS_NAME, "prdName")
        product_prices = driver.find_elements(By.CLASS_NAME, "current-price")
        
        print(f"  - 找到 {len(product_names)} 個商品名稱")
        print(f"  - 找到 {len(product_prices)} 個價格")
        
        if len(product_names) == 0:
            print("\n⚠️ 仍然找不到商品！")
            print("📄 頁面 HTML 片段（前2000字）:")
            page_html = driver.page_source[:2000]
            print(page_html)
            return False
        
        # ========== 配對商品名稱和價格 ==========
        product_items = []
        for i in range(min(len(product_names), len(product_prices))):
            product_items.append({
                'name': product_names[i],
                'price': product_prices[i] if i < len(product_prices) else None
            })
        
        print(f"✓ 配對出 {len(product_items)} 個商品")
        
        # 逐個提取商品資訊
        for index, item in enumerate(product_items, 1):
            try:
                # 提取商品名稱
                product_name = "未知商品"
                try:
                    product_name = item['name'].text.strip()
                except:
                    product_name = "未知商品"
                
                # 提取商品價格
                price_text = "價格未顯示"
                try:
                    price_text = item['price'].text.strip() if item['price'] else "價格未顯示"
                except:
                    price_text = "價格未顯示"
                
                # 清理價格資料（移除特殊符號和空白）
                price_text = price_text.replace("NT$", "").replace(",", "").replace("元", "").strip()
                
                # ========== 調試輸出 ==========
                print(f"\n  [{index}] 名稱: {product_name}")
                print(f"      價格: {price_text}")
                
                # 儲存商品資訊
                products_data.append({
                    "商品名稱": product_name,
                    "價格": price_text,
                    "成本": int(float(price_text.split(',')[0]) * 0.45) if price_text.replace(',', '').isdigit() else "N/A",
                    "配送廠商": "富昇物流",
                    "SKU碼": "CLK-" + str(index).zfill(4),
                    "來源": "Momo",
                    "配送方式": "宅配"
                })
                
            except Exception as e:
                print(f"  ⚠️ 第 {index} 個商品提取失敗: {e}")
                continue
        
        # ========== 步驟4：儲存為 CSV 檔案 ==========
        if products_data:
            print(f"\n💾 正在儲存 {len(products_data)} 個商品資訊...")
            
            try:
                with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8-sig') as csvfile:
                    # 定義欄位名稱
                    fieldnames = ["商品名稱", "價格", "成本", "配送廠商", "SKU碼", "來源", "配送方式"]
                    writer.writerows(products_data)
                
                print(f"✓ CSV 檔案已儲存: {OUTPUT_FILE}")
                print(f"  檔案位置: {os.path.abspath(OUTPUT_FILE)}")
                
            except Exception as e:
                print(f"✗ 儲存 CSV 檔案失敗: {e}")
                return False
        else:
            print("✗ 未能提取任何商品資訊")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ 爬蟲執行過程發生錯誤: {e}")
        # 發生錯誤仍然保留瀏覽器不關
        print("\n⚠️ 發生錯誤！瀏覽器保持開啟供檢查")
        return False
    
    # ========== 爬蟲完成，永遠不關閉瀏覽器 ==========
    print("\n✅ 爬蟲完成！")
    print("⏸️ 瀏覽器保持開啟")
    print("💡 您可以在瀏覽器中檢查爬取結果，按 Ctrl+C 結束程式")


# ========== 第5步：錯誤處理與主程式入口 ==========

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Momo購物網商品爬蟲程式")
    print("=" * 60)
    print("\n【程式說明】")
    print("此程式會自動抓取 momo 購物網的商品資訊")
    print("並將結果儲存為 CSV 檔案")
    print("\n【重要提示】")
    print("⚠️  首次執行前，請確保已安裝必要的套件：")
    print("   pip install selenium")
    print("   並下載對應版本的 ChromeDriver")
    print("\n【如果抓不到資料的解決步驟】")
    print("1. 打開 momo 網站，用 F12 開啟開發者工具")
    print("2. 在商品卡片上按右鍵 → 選『Inspect』")
    print("3. 找到商品名稱和價格的 class 或 id 名稱")
    print("4. 將本程式碼中的 class 名稱改成新的名稱")
    print("5. 重新執行程式")
    print("=" * 60)
    
    # 執行爬蟲
    success = scrape_momo_products()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ 爬蟲程式執行完成！")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ 爬蟲程式執行失敗")
        print("=" * 60)
    
    # ========== 永遠不結束程式 ==========
    print("\n" + "=" * 60)
    print("⏸️ 程式持續運行中...")
    print("🔔 瀏覽器保持開啟")
    print("💡 按 Ctrl+C 來終止程式")
    print("=" * 60)
    
    try:
        # 讓程式永遠處於運行狀態
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 程式已被中斷，再見！")


# ========== 【修改指南】如果爬蟲抓不到資料 ==========
"""
常見的修改位置：

1️⃣  商品名稱 class 名稱（約第130行）
    目前設定：item.find_element(By.CLASS_NAME, "name")
    
    修改方式：
    a) 打開 momo 網站
    b) F12 開啟開發者工具
    c) 右鍵點商品 → Inspect
    d) 找到商品名稱所在的 HTML 標籤
    e) 複製 class 名稱，替換上面的 "name"

2️⃣  商品價格 class 名稱（約第140行）
    目前設定：item.find_element(By.CLASS_NAME, "price")
    
    修改方式：同上

3️⃣  等待頁面元素加載（約第90行）
    目前設定：wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "goodsItem")
            ))
    
    修改方式：同上，找到商品容器的正確 class 名稱

4️⃣  等待時間調整
    如果網路較慢，可以增加 time.sleep() 的秒數
    line 76: time.sleep(3)  → 可改為 time.sleep(5)
    line 85: time.sleep(2)  → 可改為 time.sleep(3)

5️⃣  輸出檔名修改
    OUTPUT_FILE = "momo_products.csv"  → 可改為任意名稱

💡 小技巧：
   - 如果被網站擋住，可以在 User-Agent 中試試其他瀏覽器字串
   - 可以加入 time.sleep() 在迴圈中延遲請求，避免過於頻繁
   - 如果仍無法抓取，可能是網站有反爬蟲機制，需要更進階的解決方案
"""
