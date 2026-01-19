# Clarks Inventory Dashboard - Development Guide

This is a React inventory management dashboard for Clarks footwear brand.

## Project Overview

- **Type:** React + Vite + TypeScript
- **Styling:** Tailwind CSS + shadcn/ui
- **Layout:** Two-column dashboard with sidebar navigation
- **Purpose:** Inventory management and forecasting for Clarks stores and warehouses

## Development Setup

### Quick Start
```bash
npm install
npm run dev
```

The application will be available at `http://localhost:5173`

### Build & Deploy
```bash
npm run build    # Production build
npm run preview  # Preview production build
npm run lint     # Run ESLint
```

## Project Structure

```
src/
├── components/
│   ├── Sidebar.tsx              # Left navigation sidebar
│   └── InventoryDataTable.tsx   # Main inventory table
├── data/
│   └── sampleData.ts            # Sample inventory data
├── App.tsx                      # Main application component
├── main.tsx                     # React entry point
└── index.css                    # Tailwind directives
```

## Key Components

### Sidebar
- Navigation between Store, Warehouse, and Shelf inventory views
- Active tab indication with warm amber highlighting
- Icon support via lucide-react

### InventoryDataTable
Displays 7-column inventory information:
1. Product (with image and SKU)
2. Current Stock (progress bar)
3. Forecast Demand (progress bar)
4. Suggested Order (quantity)
5. Status (badge: Normal/Restock/Overstock)
6. Supplier Info (company name)
7. Warehouse (location)

## Styling & Customization

- **CSS Framework:** Tailwind CSS
- **Color Scheme:** Warm amber primary, red for alerts
- **Responsive:** Mobile-friendly design with Tailwind utilities
- **Components:** Custom React components + lucide icons

## Adding Features

### New Inventory Items
Edit `src/data/sampleData.ts` to add products.

### New Navigation Views
Modify `src/components/Sidebar.tsx` navigation items.

### Custom Styling
Update Tailwind configuration in `tailwind.config.js` or use inline Tailwind classes.

## Dependencies

Core:
- react@19.2.0
- react-dom@19.2.0
- lucide-react (icons)

Styling:
- tailwindcss
- class-variance-authority
- clsx
- tailwind-merge

Build:
- typescript
- vite
- @vitejs/plugin-react

## Environment Notes

- **Node.js:** Version 16 or higher
- **Package Manager:** npm or yarn
- **Browser Support:** Latest versions of Chrome, Firefox, Safari, Edge
- **Development Server:** Vite (HMR enabled)

## Common Tasks

### Start Development Server
```bash
npm run dev
```

### Build for Production
```bash
npm run build
```

### Fix Lint Issues
```bash
npm run lint
```

### View Production Build
```bash
npm run preview
```

## Troubleshooting

**Issue:** Port 5173 already in use
- Solution: Kill the process or use a different port with `npm run dev -- --port 3000`

**Issue:** Tailwind styles not applying
- Solution: Ensure CSS imports are correct and tailwind.config.js is properly configured

**Issue:** Type errors
- Solution: Run `npm run build` to see full TypeScript errors, or check tsconfig.json

## Contact & Support

For questions about the dashboard design or implementation, refer to:
- React Documentation: https://react.dev
- Vite Guide: https://vite.dev
- Tailwind CSS: https://tailwindcss.com

---

**Last Updated:** January 2026
**Version:** 1.0.0
