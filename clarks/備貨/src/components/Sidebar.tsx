import React from 'react';
import { Store, Package, Layers } from 'lucide-react';

interface SidebarProps {
  activeTab: 'store' | 'warehouse' | 'shelf';
  onTabChange: (tab: 'store' | 'warehouse' | 'shelf') => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ activeTab, onTabChange }) => {
  const navItems = [
    { id: 'store', label: '門市總覽', icon: Store, description: 'Store' },
    { id: 'warehouse', label: '倉庫', icon: Package, description: 'Warehouse' },
    { id: 'shelf', label: '架上', icon: Layers, description: 'Shelf' },
  ] as const;

  return (
    <aside className="w-64 bg-white border-r border-gray-200 p-6 h-screen flex flex-col">
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">庫存盤點</h1>
        <p className="text-sm text-gray-500 mt-1">Inventory Dashboard</p>
      </div>

      <nav className="space-y-2 flex-1">
        {navItems.map(({ id, label, icon: Icon, description }) => (
          <button
            key={id}
            onClick={() => onTabChange(id)}
            className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
              activeTab === id
                ? 'bg-amber-100 text-amber-900'
                : 'text-gray-700 hover:bg-gray-100'
            }`}
          >
            <Icon className="w-5 h-5" />
            <div className="text-left">
              <div className="font-medium">{label}</div>
              <div className="text-xs opacity-75">{description}</div>
            </div>
          </button>
        ))}
      </nav>

      <div className="pt-4 border-t border-gray-200">
        <p className="text-xs text-gray-400">Clarks Footwear</p>
      </div>
    </aside>
  );
};
