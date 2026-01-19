import React from 'react';

interface Product {
  id: string;
  name: string;
  sku: string;
  image?: string;
  currentStock: number;
  forecastDemand: number;
  suggestedOrder: number;
  status: 'normal' | 'restock' | 'overstock';
  supplierName: string;
  warehouseLocation: string;
}

interface DataTableProps {
  data: Product[];
}

const StatusBadge: React.FC<{ status: string }> = ({ status }) => {
  const statusConfig = {
    normal: { bg: 'bg-green-100', text: 'text-green-800', label: '正常' },
    restock: { bg: 'bg-red-100', text: 'text-red-800', label: '補貨' },
    overstock: { bg: 'bg-yellow-100', text: 'text-yellow-800', label: '超庫' },
  };
  
  const config = statusConfig[status as keyof typeof statusConfig] || statusConfig.normal;
  
  return (
    <span className={`inline-block px-3 py-1 rounded-full text-sm font-semibold ${config.bg} ${config.text}`}>
      {config.label}
    </span>
  );
};

const ProgressBar: React.FC<{ current: number; forecast: number; color: string }> = ({ current, forecast, color }) => {
  const percentage = Math.min((current / forecast) * 100, 100);
  
  return (
    <div className="w-full">
      <div className="flex justify-between mb-1">
        <span className="text-sm font-medium text-gray-700">{current} 件</span>
      </div>
      <div className="w-full bg-gray-200 rounded-full h-2">
        <div
          className={`h-2 rounded-full transition-all ${color}`}
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  );
};

export const InventoryDataTable: React.FC<DataTableProps> = ({ data }) => {
  return (
    <div className="w-full overflow-x-auto bg-white rounded-lg border border-gray-200">
      <table className="w-full">
        <thead className="bg-gray-50 border-b border-gray-200">
          <tr>
            <th className="px-6 py-4 text-left text-sm font-semibold text-gray-900 w-80">
              商品 (Product)
            </th>
            <th className="px-6 py-4 text-left text-sm font-semibold text-gray-900 w-40">
              本週商品庫存盤點 (Current Stock)
            </th>
            <th className="px-6 py-4 text-left text-sm font-semibold text-gray-900 w-40">
              下週預估商品需求量 (Forecast Demand)
            </th>
            <th className="px-6 py-4 text-left text-sm font-semibold text-gray-900 w-32">
              建議下單量 (Suggested Order)
            </th>
            <th className="px-6 py-4 text-left text-sm font-semibold text-gray-900 w-24">
              狀態 (Status)
            </th>
            <th className="px-6 py-4 text-left text-sm font-semibold text-gray-900">
              廠商資訊 (Supplier Info)
            </th>
            <th className="px-6 py-4 text-left text-sm font-semibold text-gray-900 w-40">
              倉庫 (Warehouse)
            </th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-200">
          {data.map((product) => (
            <tr key={product.id} className="hover:bg-gray-50 transition-colors">
              <td className="px-6 py-4">
                <div className="flex items-center gap-3">
                  <div className="w-12 h-12 bg-gray-200 rounded-lg flex items-center justify-center flex-shrink-0">
                    {product.image ? (
                      <img src={product.image} alt={product.name} className="w-full h-full object-cover rounded-lg" />
                    ) : (
                      <span className="text-gray-400 text-xs">Image</span>
                    )}
                  </div>
                  <div>
                    <p className="font-medium text-gray-900 text-sm">{product.name}</p>
                    <p className="text-xs text-gray-500">SKU: {product.sku}</p>
                  </div>
                </div>
              </td>
              <td className="px-6 py-4">
                <ProgressBar current={product.currentStock} forecast={product.forecastDemand} color="bg-blue-500" />
              </td>
              <td className="px-6 py-4">
                <ProgressBar current={product.forecastDemand} forecast={Math.max(product.currentStock, product.forecastDemand)} color="bg-gray-400" />
                <p className="text-sm font-medium text-gray-900 mt-2">{product.forecastDemand} 件</p>
              </td>
              <td className="px-6 py-4">
                <p className="text-lg font-bold text-orange-600">{product.suggestedOrder}</p>
              </td>
              <td className="px-6 py-4">
                <StatusBadge status={product.status} />
              </td>
              <td className="px-6 py-4">
                <p className="text-sm text-gray-700">{product.supplierName}</p>
              </td>
              <td className="px-6 py-4">
                <p className="text-sm text-gray-700">{product.warehouseLocation}</p>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
