// Header 配置管理
const HeaderConfig = {
    // 基本品牌信息
    brand: {
        logo: "奇點.png",
        name: "JudgAI",
        alt: "JudgAI Logo"
    },
    
    // 導航項目配置
    navigation: [
        {
            title: "首頁",
            href: "index.html",
            isActive: function(currentPage) {
                return currentPage === 'index' || currentPage === '';
            }
        },
        {
            title: "方案定價",
            href: "pricing.html",
            isActive: function(currentPage) {
                return currentPage === 'pricingv2' || currentPage === 'pricing';
            }
        },
        {
            title: "AI行銷與業務專欄",
            href: "column_article.html",
            isActive: function(currentPage) {
                return currentPage === 'column_article';
            }
        },
        {
            title: "AI保單銷售手冊",
            href: "insur_policy_demo.html",
            isActive: function(currentPage) {
                return currentPage === 'insur_policy_demo';
            }
        },
        {
            title: "直播分享",
            href: "index.html#live-sharing",
            isActive: function(currentPage) {
                return false; // 這是錨點連結，通常不會高亮
            }
        }
    ],
    
    // CTA 按鈕配置
    ctaButtons: {
        primary: {
            title: "聯絡我們",
            href: "https://line.me/ti/p/ECTAxiLRSh",
            target: "_blank"
        },
        secondary: {
            title: "免費試用",
            href: "https://aistudy.pse.is/insurance-bot",
            target: "_blank"
        }
    },
    
    // 生成 header HTML
    generateHeader: function(currentPage = '') {
        const desktopNav = this.navigation.map(item => {
            const isActive = item.isActive(currentPage);
            const activeClass = isActive ? 'text-cyan-400' : 'text-gray-200 hover:text-blue-400';
            
            return `
                <a href="${item.href}" class="nav-link ${activeClass} font-medium py-2 px-3">
                    ${item.title}
                </a>
            `;
        }).join('');
        
        const mobileNav = this.navigation.map(item => {
            const isActive = item.isActive(currentPage);
            const activeClass = isActive ? 'text-cyan-400' : 'text-gray-200 hover:text-blue-400';
            
            return `
                <a href="${item.href}" class="nav-link ${activeClass} font-medium py-2">
                    ${item.title}
                </a>
            `;
        }).join('');
        
        return `
            <header class="header-nav fixed top-0 left-0 right-0 z-50">
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex justify-between items-center py-4">
                        <!-- Logo 和品牌名稱 -->
                        <div class="flex items-center space-x-3">
                            <img src="${this.brand.logo}" alt="${this.brand.alt}" class="h-10 w-10 rounded-full">
                            <span class="font-orbitron text-xl font-bold gradient-text">${this.brand.name}</span>
                        </div>
                        
                        <!-- 桌面版導航 -->
                        <nav class="hidden md:flex space-x-8">
                            ${desktopNav}
                        </nav>
                        
                        <!-- CTA 按鈕 -->
                        <div class="hidden md:flex items-center space-x-4">
                            <a href="${this.ctaButtons.primary.href}" target="${this.ctaButtons.primary.target}" class="cta-button text-white font-medium py-2 px-6 rounded-lg text-sm">
                                ${this.ctaButtons.primary.title}
                            </a>
                        </div>
                        
                        <!-- 手機版菜單按鈕 -->
                        <button id="mobile-menu-button" class="md:hidden text-gray-200 hover:text-blue-400 focus:outline-none">
                            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                            </svg>
                        </button>
                    </div>
                    
                    <!-- 手機版導航菜單 -->
                    <div id="mobile-menu" class="md:hidden hidden mobile-menu rounded-lg mt-2 py-4">
                        <div class="flex flex-col space-y-3 px-4">
                            ${mobileNav}
                            <div class="pt-3 border-t border-gray-700">
                                <a href="${this.ctaButtons.secondary.href}" target="${this.ctaButtons.secondary.target}" class="cta-button block text-center text-white font-medium py-2 px-6 rounded-lg text-sm">
                                    ${this.ctaButtons.secondary.title}
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
        `;
    },
    
    // 初始化 header
    init: function(currentPage = '') {
        // 獲取當前頁面名稱
        if (!currentPage) {
            const path = window.location.pathname;
            const filename = path.split('/').pop();
            currentPage = filename.replace('.html', '');
        }
        
        // 查找 header 容器並插入 HTML
        const headerContainer = document.getElementById('header-container');
        if (headerContainer) {
            headerContainer.innerHTML = this.generateHeader(currentPage);
        }
        
        // 綁定手機版菜單事件
        this.bindMobileMenuEvents();
    },
    
    // 綁定手機版菜單事件
    bindMobileMenuEvents: function() {
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');
        
        if (mobileMenuButton && mobileMenu) {
            mobileMenuButton.addEventListener('click', function() {
                mobileMenu.classList.toggle('hidden');
            });
            
            // 點擊外部關閉菜單
            document.addEventListener('click', function(event) {
                if (!mobileMenuButton.contains(event.target) && !mobileMenu.contains(event.target)) {
                    mobileMenu.classList.add('hidden');
                }
            });
        }
    }
};

// 自動初始化（如果 DOM 已加載）
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        HeaderConfig.init();
    });
} else {
    HeaderConfig.init();
}

// 導出配置對象供其他腳本使用
window.HeaderConfig = HeaderConfig;