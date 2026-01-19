import { useState } from 'react';
import { Sidebar } from './components/Sidebar';
import { InventoryDataTable } from './components/InventoryDataTable';
import { sampleInventoryData } from './data/sampleData';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState<'store' | 'warehouse' | 'shelf'>('store');

  const getTabTitle = () => {
    switch (activeTab) {
      case 'store':
        return '門市總覽 (Store Overview)';
      case 'warehouse':
        return '倉庫庫存 (Warehouse Inventory)';
      case 'shelf':
        return '架上庫存 (Shelf Inventory)';
    }
  };

  return (
    <div className="flex h-screen bg-gray-50">
      <Sidebar activeTab={activeTab} onTabChange={setActiveTab} />
      
      <main className="flex-1 overflow-auto">
        <div className="p-8">
          <div className="mb-8">
            <h2 className="text-3xl font-bold text-gray-900">{getTabTitle()}</h2>
            <p className="text-gray-600 mt-2">管理各區域庫存、掌握下週需求，並快速達成即時連連 (Manage regional inventory and forecast demand)</p>
          </div>

          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <InventoryDataTable data={sampleInventoryData} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
