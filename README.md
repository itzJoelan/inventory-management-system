# Inventory Management System

A production-quality Inventory Management System built with Django, featuring a modern SaaS-like interface with clean architecture and professional UI.

## Technology Stack

### Backend
- Python 3.x
- Django (latest stable)
- SQLite3 Database
- Django ORM
- Django Authentication

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Vanilla JavaScript
- Bootstrap Icons
- Google Fonts (Poppins)

## Features

### Core Modules
1. **Dashboard** - KPIs, Charts, Inventory Summary, Recent Activities
2. **Products** - Full CRUD with SKU, Barcode, Images, Categories, Suppliers
3. **Categories** - Product categorization with images and descriptions
4. **Suppliers** - Supplier management with contact details
5. **Customers** - Customer profiles and purchase history
6. **Inventory** - Stock In/Out, Adjustments, Transfers, History
7. **Purchase Orders** - PO creation, receiving, tracking, printing
8. **Sales** - Sales invoices, history, printing
9. **Reports** - Inventory, Sales, Purchase, Stock Movement reports with PDF/Excel export
10. **Users** - User management, roles, permissions, profiles

### Additional Features
- Global search with autocomplete
- Low stock and out-of-stock alerts
- Professional sidebar navigation
- Responsive design (Desktop, Tablet, Mobile)
- Activity logging and audit trails
- Modern card-based layout
- Beautiful charts with Chart.js

## Theme

**Primary Color:** #3C453E
**Secondary Color:** #181D2E
**Accent:** White (#FFFFFF), Light Gray (#F5F5F5)

## Project Structure

```
inventory-management-system/
├── manage.py
├── requirements.txt
├── inventory_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── dashboard/
│   ├── products/
│   ├── categories/
│   ├── suppliers/
│   ├── customers/
│   ├── inventory/
│   ├── purchase_orders/
│   ├── sales/
│   ├── reports/
│   ├── users/
│   └── core/
├── templates/
│   ├── base/
│   ├── dashboard/
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── media/
└── services/
```

## Getting Started

### Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Collect static files: `python manage.py collectstatic`
8. Start development server: `python manage.py runserver`

Visit `http://localhost:8000`

## License

Proprietary - Inventory Management System
