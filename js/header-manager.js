/**
 * 統一 Header 管理系統
 * 使用此腳本可以在所有頁面中統一管理 header
 */

// Header HTML 模板
const headerTemplate = `
<nav class="bg-gray-900/80 backdrop-filter backdrop-blur-lg border-b border-gray-700/50 sticky top-0 z-40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-4">
            <div class="flex items-center">
                <!-- 圓形 Logo -->
                <div class="relative mr-3">
                    <div class="w-10 h-10 rounded-full overflow-hidden border-2 border-cyan-400/30 bg-gradient-to-br from-cyan-400/20 to-blue-600/20 backdrop-blur-sm">
                        <img src="SayMind_LOGO.png" alt="SayMind Logo" class="w-full h-full object-cover rounded-full">
                    </div>
                    <!-- 外層光暈效果 -->
                    <div class="absolute inset-0 rounded-full bg-gradient-to-r from-cyan-400 to-blue-500 opacity-20 blur-sm"></div>
                </div>
                <span class="font-orbitron text-xl font-bold text-white">SayMind</span>
            </div>
            <div class="flex items-center space-x-8">
                <!-- 導航連結 - 根據當前頁面自動調整 -->
                <a href="saymind.html" class="nav-link text-gray-300 hover:text-cyan-400 font-medium transition-all duration-300" data-nav="home">首頁</a>
                <a href="changelog.html" class="nav-link text-gray-300 hover:text-cyan-400 font-medium transition-all duration-300" data-nav="changelog">更新日誌</a>
                
                <!-- 聯絡我們按鈕 - 參考 index.html 風格 -->
                <a href="https://line.me/ti/p/ECTAxiLRSh" target="_blank" 
                   class="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white font-medium py-2 px-6 rounded-lg text-sm transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-cyan-500/25">
                    聯絡我們
                </a>
                
                <!-- 立即使用按鈕 -->
                <a href="https://dev-box3.taiwanmds.com/speech2text_free_registry/" target="_blank" 
                   class="border border-cyan-400 text-cyan-400 hover:bg-cyan-400 hover:text-gray-900 font-medium py-2 px-6 rounded-lg text-sm transition-all duration-300">
                    立即使用
                </a>
            </div>
        </div>
    </div>
</nav>
`;

// 初始化 Header
function initializeHeader() {
    // 查找 header 容器
    const headerContainer = document.getElementById('header-container') || 
                           document.querySelector('[data-header-container]') ||
                           document.querySelector('nav');
    
    if (headerContainer) {
        headerContainer.outerHTML = headerTemplate;
        
        // 設置當前頁面的活動狀態
        setActiveNavigation();
        
        // 添加滾動效果
        addScrollEffects();
    }
}

// 設置當前頁面的導航活動狀態
function setActiveNavigation() {
    const currentPage = getCurrentPageName();
    const navLinks = document.querySelectorAll('[data-nav]');
    
    navLinks.forEach(link => {
        const navType = link.getAttribute('data-nav');
        if (shouldBeActive(navType, currentPage)) {
            link.classList.remove('text-gray-300');
            link.classList.add('text-cyan-400');
        }
    });
}

// 獲取當前頁面名稱
function getCurrentPageName() {
    const path = window.location.pathname;
    const filename = path.split('/').pop().toLowerCase();
    
    if (filename.includes('changelog')) return 'changelog';
    if (filename.includes('saymind') || filename === '' || filename === '/') return 'home';
    return 'other';
}

// 判斷導航項是否應該處於活動狀態
function shouldBeActive(navType, currentPage) {
    const activeMap = {
        'home': currentPage === 'home',
        'changelog': currentPage === 'changelog'
    };
    
    return activeMap[navType] || false;
}

// 添加滾動效果
function addScrollEffects() {
    let lastScrollY = window.scrollY;
    const nav = document.querySelector('nav');
    
    if (!nav) return;
    
    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > lastScrollY && currentScrollY > 100) {
            // 向下滾動時隱藏
            nav.style.transform = 'translateY(-100%)';
        } else {
            // 向上滾動時顯示
            nav.style.transform = 'translateY(0)';
        }
        
        // 根據滾動位置調整透明度
        const opacity = Math.min(0.95, 0.7 + (currentScrollY / 200) * 0.25);
        nav.style.backgroundColor = `rgba(17, 24, 39, ${opacity})`;
        
        lastScrollY = currentScrollY;
    });
}

// 當 DOM 加載完成時初始化
document.addEventListener('DOMContentLoaded', initializeHeader);

// 導出給其他腳本使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { initializeHeader, headerTemplate };
}
