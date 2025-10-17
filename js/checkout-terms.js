// Centralized purchase URL mapping and terms-modal handlers
(function(){
    // Purchase URL mapping shared across pages. Keep keys consistent with onclick plan names.
    window.purchaseUrls = Object.assign(window.purchaseUrls || {}, {
        '專業版月繳限時優惠': 'https://cart.cashier.ecpay.com.tw/qp/y2E0',
        '專業版月繳': 'https://cart.cashier.ecpay.com.tw/qp/y2k3',
        '專業版半年繳': 'https://cart.cashier.ecpay.com.tw/qp/y2jC',
        '專業版年繳': 'https://cart.cashier.ecpay.com.tw/qp/y2h3',
        '一套專業版': 'https://cart.cashier.ecpay.com.tw/qp/y2bA',
        '加值分鐘數 優惠A': 'https://cart.cashier.ecpay.com.tw/qp/y2d7',
        '加值分鐘數 優惠B': 'https://cart.cashier.ecpay.com.tw/qp/y2e2',
        '加值分鐘數 原價': 'https://cart.cashier.ecpay.com.tw/qp/y2g7'
    });

    // track selected plan
    window.__selectedPurchasePlan = null;

    function findTermsModalElement(){
        // Pricing page uses 'refundTermsModal', other pages use 'termsModal'
        return document.getElementById('refundTermsModal') || document.getElementById('termsModal');
    }

    function findDiscountModalElement(){
        return document.getElementById('discountTermsModal');
    }

    function showDiscountTermsModal(planKey){
        window.__selectedPurchasePlan = planKey || null;
        const modal = findDiscountModalElement();
        if (!modal) return console.warn('No discount modal found to show');
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }

    function closeDiscountTermsModal(){
        const modal = findDiscountModalElement();
        if (!modal) return;
        modal.classList.add('hidden');
        document.body.style.overflow = 'auto';
    }

    function showTermsModal(planKey){
        window.__selectedPurchasePlan = planKey || null;
        const modal = findTermsModalElement();
        if (!modal) return console.warn('No terms modal found to show');
        // update header if present
        const header = modal.querySelector('.modal-content h2');
        if (header && planKey) header.textContent = `服務條款 — ${planKey}`;
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }

    function closeTermsModal(){
        const modal = findTermsModalElement();
        if (!modal) return;
        modal.classList.add('hidden');
        const header = modal.querySelector('.modal-content h2');
        if (header) header.textContent = '服務條款';
        document.body.style.overflow = 'auto';
    }

    function acceptRefundTerms(){
        const key = window.__selectedPurchasePlan;
        if (!key) return closeTermsModal();
        const url = window.purchaseUrls && window.purchaseUrls[key];
        if (!url) {
            console.warn('No purchase URL mapped for plan:', key);
            return closeTermsModal();
        }
        const w = window.open(url, '_blank');
        if (w) try { w.opener = null; } catch(e){}
        // close both possible modals if open
        closeTermsModal();
        closeDiscountTermsModal();
    }

    // expose globally for inline onclick handlers
    window.showTermsModal = showTermsModal;
    window.closeTermsModal = closeTermsModal;
    window.acceptRefundTerms = acceptRefundTerms;
    window.showDiscountTermsModal = showDiscountTermsModal;
    window.closeDiscountTermsModal = closeDiscountTermsModal;

})();
