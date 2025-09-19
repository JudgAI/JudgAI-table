// 主題切換管理器
class ThemeManager {
    constructor() {
        this.currentTheme = this.getStoredTheme() || 'dark';
        this.init();
    }
    
    // 獲取存儲的主題
    getStoredTheme() {
        return localStorage.getItem('theme');
    }
    
    // 存儲主題設置
    setStoredTheme(theme) {
        localStorage.setItem('theme', theme);
    }
    
    // 初始化主題
    init() {
        this.applyTheme(this.currentTheme);
        this.createThemeToggle();
        this.bindEvents();
    }
    
    // 應用主題
    applyTheme(theme) {
        const body = document.body;
        const html = document.documentElement;
        
        if (theme === 'light') {
            body.classList.add('light-theme');
            body.classList.remove('dark-theme');
            html.classList.add('light-theme');
            html.classList.remove('dark-theme');
        } else {
            body.classList.add('dark-theme');
            body.classList.remove('light-theme');
            html.classList.add('dark-theme');
            html.classList.remove('light-theme');
        }
        
        this.currentTheme = theme;
        this.updateToggleButton();
    }
    
    // 切換主題
    toggleTheme() {
        const newTheme = this.currentTheme === 'dark' ? 'light' : 'dark';
        this.applyTheme(newTheme);
        this.setStoredTheme(newTheme);
    }
    
    // 創建主題切換按鈕
    createThemeToggle() {
        const toggleButton = document.createElement('button');
        toggleButton.id = 'theme-toggle';
        toggleButton.className = 'theme-toggle fixed top-20 right-4 z-50 bg-gray-800 hover:bg-gray-700 text-white p-3 rounded-full shadow-lg transition-all duration-300 hover:scale-110';
        toggleButton.setAttribute('aria-label', '切換主題');
        
        // 將按鈕添加到頁面
        document.body.appendChild(toggleButton);
        
        this.updateToggleButton();
    }
    
    // 更新切換按鈕
    updateToggleButton() {
        const button = document.getElementById('theme-toggle');
        if (!button) return;
        
        if (this.currentTheme === 'dark') {
            button.innerHTML = `
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"></path>
                </svg>
            `;
            button.title = '切換到淺色模式';
        } else {
            button.innerHTML = `
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
                </svg>
            `;
            button.title = '切換到深色模式';
        }
    }
    
    // 綁定事件
    bindEvents() {
        document.addEventListener('click', (e) => {
            if (e.target.closest('#theme-toggle')) {
                this.toggleTheme();
            }
        });
    }
}

// CSS 變量定義
const themeStyles = `
:root {
    /* 深色主題 (默認) */
    --bg-primary: #111827;
    --bg-secondary: #1f2937;
    --bg-tertiary: #374151;
    --text-primary: #f9fafb;
    --text-secondary: #d1d5db;
    --text-muted: #9ca3af;
    --border-color: #4b5563;
    --accent-primary: #06b6d4;
    --accent-secondary: #3b82f6;
}

.light-theme {
    /* 科技感白色主題 */
    --bg-primary: #ffffff;
    --bg-secondary: #f8fafc;
    --bg-tertiary: #f1f5f9;
    --text-primary: #0f172a;
    --text-secondary: #334155;
    --text-muted: #64748b;
    --border-color: #e2e8f0;
    --accent-primary: #0891b2;
    --accent-secondary: #2563eb;
    --card-bg: #ffffff;
    --card-border: #e2e8f0;
}

/* 基礎樣式覆蓋 - 科技感白色模式 */
.light-theme body {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
    color: var(--text-primary);
    min-height: 100vh;
}

/* 主要背景區塊 */
.light-theme .bg-gray-900,
.light-theme .hero-section {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%) !important;
}

.light-theme .bg-gray-800 {
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%) !important;
}

.light-theme .bg-gray-700 {
    background-color: var(--bg-tertiary) !important;
}

/* 文字顏色 */
.light-theme .text-gray-100,
.light-theme .text-gray-200,
.light-theme .text-white {
    color: var(--text-primary) !important;
}

.light-theme .text-gray-300,
.light-theme .text-gray-400 {
    color: var(--text-secondary) !important;
}

.light-theme .text-gray-500,
.light-theme .text-gray-600 {
    color: var(--text-muted) !important;
}

/* 邊框樣式 */
.light-theme .border-gray-700,
.light-theme .border-gray-800,
.light-theme .border-gray-600 {
    border-color: var(--border-color) !important;
}

/* 科技感卡片樣式 */
.light-theme .plan-card,
.light-theme .comparison-card,
.light-theme .audience-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
    border: 2px solid var(--border-color) !important;
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08), 0 4px 6px rgba(15, 23, 42, 0.05) !important;
    backdrop-filter: blur(10px) !important;
}

.light-theme .plan-card:hover,
.light-theme .comparison-card:hover {
    box-shadow: 0 20px 40px rgba(15, 23, 42, 0.12), 0 8px 16px rgba(15, 23, 42, 0.08) !important;
    transform: translateY(-2px) !important;
}

/* Header 科技感樣式 */
.light-theme .header-nav {
    background: rgba(255, 255, 255, 0.95) !important;
    border-bottom: 2px solid var(--border-color) !important;
    backdrop-filter: blur(20px) !important;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08) !important;
}

/* 7天免費試用區塊科技感樣式 */
.light-theme .relative.overflow-hidden.bg-gradient-to-br {
    background: linear-gradient(135deg, #f8fafc 0%, #ffffff 50%, #f1f5f9 100%) !important;
    border: 2px solid var(--accent-primary) !important;
    box-shadow: 0 20px 40px rgba(8, 145, 178, 0.15), 0 8px 16px rgba(8, 145, 178, 0.1) !important;
}

/* Hero Section 白色模式 */
.light-theme .hero-section {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%) !important;
}

/* 主標題區域 */
.light-theme .hero-section h1.gradient-text {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary), #8b5cf6) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}

/* 副標題文字 */
.light-theme .hero-section .text-gray-300 {
    color: var(--text-secondary) !important;
}

/* 科技圖標容器 */
.light-theme .bg-gradient-to-br.from-cyan-500,
.light-theme .bg-gradient-to-br.from-purple-500 {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary)) !important;
    box-shadow: 0 4px 12px rgba(8, 145, 178, 0.3) !important;
}

/* 數據亮點區塊 */
.light-theme .bg-gradient-to-r.from-gray-800\/50 {
    background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%) !important;
    border: 1px solid var(--border-color) !important;
    box-shadow: inset 0 2px 4px rgba(15, 23, 42, 0.05) !important;
}

/* 數據文字顏色 */
.light-theme .text-gray-400 {
    color: var(--text-muted) !important;
}

/* 分隔線 */
.light-theme .bg-gradient-to-b.from-transparent.via-gray-500 {
    background: linear-gradient(to bottom, transparent, var(--border-color), transparent) !important;
}

/* 星空背景在淺色模式下隱藏 */
.light-theme .stars,
.light-theme .absolute.inset-0.overflow-hidden {
    display: none !important;
}

/* 背景裝飾元素調整 */
.light-theme .absolute.inset-0.bg-gradient-to-r {
    background: linear-gradient(to right, transparent, rgba(8, 145, 178, 0.05), transparent) !important;
}

/* 頂部裝飾線 */
.light-theme .absolute.top-0.left-0.w-full.h-1 {
    background: linear-gradient(to right, var(--accent-primary), var(--accent-secondary), #8b5cf6) !important;
}

/* 確保所有區塊都有正確的白色背景 */
.light-theme section {
    background: inherit !important;
}

/* 專業版方案區塊 */
.light-theme #pricing-plans {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
}

/* 浮動粒子在淺色模式下調整 */
.light-theme .absolute.top-4.left-8,
.light-theme .absolute.top-12.right-12,
.light-theme .absolute.bottom-8.left-16,
.light-theme .absolute.bottom-16.right-8 {
    background-color: var(--accent-primary) !important;
    opacity: 0.3 !important;
}

/* 專業版方案標題 */
.light-theme #pricing-plans h2.gradient-text {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary), #8b5cf6) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}

/* main 區塊白色背景 */
.light-theme main {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
    min-height: 100vh;
}

/* 免費試用提示框 */
.light-theme .bg-gradient-to-r.from-cyan-500\/20 {
    background: linear-gradient(135deg, rgba(8, 145, 178, 0.1), rgba(37, 99, 235, 0.1)) !important;
    border-color: var(--accent-primary) !important;
}

.light-theme .text-cyan-300 {
    color: var(--accent-primary) !important;
}

/* 按鈕科技感樣式調整 */
.light-theme .cta-button {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary)) !important;
    box-shadow: 0 8px 20px rgba(8, 145, 178, 0.25) !important;
    border: 2px solid transparent !important;
    transition: all 0.3s ease !important;
}

.light-theme .cta-button:hover {
    box-shadow: 0 12px 30px rgba(8, 145, 178, 0.35) !important;
    transform: translateY(-2px) scale(1.02) !important;
}

/* 主題切換按鈕科技感樣式 */
.theme-toggle {
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

.light-theme .theme-toggle {
    background: linear-gradient(135deg, #ffffff, #f8fafc) !important;
    color: var(--text-primary) !important;
    border: 2px solid var(--border-color) !important;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.1) !important;
}

.light-theme .theme-toggle:hover {
    background: linear-gradient(135deg, #f8fafc, #f1f5f9) !important;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.15) !important;
    transform: scale(1.05) !important;
}

/* 梯度文字科技感調整 */
.light-theme .gradient-text {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary), #8b5cf6) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}

/* 表格科技感樣式 */
.light-theme .comparison-table {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
    border: 2px solid var(--border-color) !important;
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08) !important;
}

.light-theme .comparison-table th {
    background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%) !important;
    color: var(--text-primary) !important;
    border-bottom: 2px solid var(--accent-primary) !important;
}

.light-theme .comparison-table td {
    background-color: var(--bg-primary) !important;
    color: var(--text-secondary) !important;
    border-color: var(--border-color) !important;
}

/* 模態框科技感樣式 */
.light-theme .modal-overlay {
    background-color: rgba(15, 23, 42, 0.4) !important;
    backdrop-filter: blur(4px) !important;
}

.light-theme .modal-content {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
    color: var(--text-primary) !important;
    border: 2px solid var(--border-color) !important;
    box-shadow: 0 25px 50px rgba(15, 23, 42, 0.15) !important;
}

/* 動畫和過渡效果 */
* {
    transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}
`;

// 添加主題樣式到頁面
function injectThemeStyles() {
    const styleElement = document.createElement('style');
    styleElement.textContent = themeStyles;
    document.head.appendChild(styleElement);
}

// 初始化主題管理器
function initThemeManager() {
    injectThemeStyles();
    new ThemeManager();
}

// 自動初始化
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initThemeManager);
} else {
    initThemeManager();
}

// 導出主題管理器供其他腳本使用
window.ThemeManager = ThemeManager;