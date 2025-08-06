# Header 統一管理說明

## 概述
為了方便統一管理所有頁面的 header，我們提供了兩種解決方案：

## 方案一：使用 header-manager.js（推薦）

### 使用步驟：

1. **在 HTML 中添加腳本引用**
```html
<!-- 在 </body> 標籤前添加 -->
<script src="js/header-manager.js"></script>
```

2. **自動替換現有 header**
腳本會自動查找並替換頁面中的 nav 元素

3. **或者手動指定容器**
```html
<!-- 在需要插入 header 的位置添加 -->
<div id="header-container"></div>
```

### 特色功能：
- ✅ 自動識別當前頁面並高亮對應導航
- ✅ 圓形 Logo 設計
- ✅ 參考 index.html 的聯絡我們按鈕風格
- ✅ 響應式滾動效果
- ✅ 統一的過渡動畫

## 方案二：使用 components/header.html

### 使用步驟：

1. **複製 header 內容**
從 `components/header.html` 複製完整的 nav 結構

2. **貼到目標頁面**
替換現有的 header 部分

3. **手動調整活動狀態**
根據頁面需求調整 `text-cyan-400` 類別

## 檔案結構
```
JudgAI-table/
├── components/
│   └── header.html          # Header 組件模板
├── js/
│   └── header-manager.js    # JavaScript 自動管理方案
├── saymind.html            # 已更新 header
├── changelog.html          # 已更新 header
└── README-header.md        # 本說明文件
```

## 更新指南

### 要修改 header 內容時：

**方案一使用者：**
1. 編輯 `js/header-manager.js` 中的 `headerTemplate`
2. 所有頁面會自動同步更新

**方案二使用者：**
1. 編輯 `components/header.html`
2. 手動複製到各個頁面

## 已實現的改進：

✅ **統一的視覺風格**：與 changelog.html 保持一致
✅ **圓形 Logo**：更有質感的設計
✅ **聯絡我們按鈕**：參考 index.html 的風格和鏈接
✅ **響應式設計**：支援各種螢幕尺寸
✅ **統一管理**：避免重複修改多個檔案

## 技術特色：

- **Backdrop Filter**：毛玻璃效果
- **Gradient Buttons**：漸層按鈕設計
- **Smooth Transitions**：平滑過渡動畫
- **Responsive Layout**：響應式佈局
- **Auto Active State**：自動活動狀態偵測

推薦使用方案一（JavaScript 方案）以獲得最佳的維護性和一致性。
