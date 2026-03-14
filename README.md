# CoreInventory – Inventory Management System

CoreInventory is a simple web-based Inventory Management System designed to digitize and streamline stock operations within a business.  
It replaces manual registers and spreadsheets with a centralized system for managing product inventory.

---

## Problem

Many small businesses track inventory using Excel sheets or manual logs.  
This can lead to stock mismatches, lack of visibility, and inefficient management.

CoreInventory solves this by providing a simple interface to manage stock operations in real time.

---

## Features

- Add new products with name, SKU, category, and quantity
- View current inventory in a structured dashboard
- Receive incoming stock from vendors
- Deliver products to customers
- Automatic stock quantity updates
- Low stock alerts for products with limited quantity
- Delete products from inventory
- Stock movement history (inventory ledger)

---

## Inventory Workflow

The system supports the following operations:

### 1. Product Creation
Inventory managers can create products with basic details.

### 2. Receive Stock
When new stock arrives, the system increases product quantity.

### 3. Deliver Stock
When products are shipped to customers, stock quantity decreases.

### 4. Stock History Tracking
Every stock operation is logged in the movement history table.

---

## Tech Stack

### Frontend
- HTML  
- CSS  

### Backend
- Python  
- Flask  

### Database
- MySQL  

---

## Database Structure

### Products Table
Stores product information.

Fields:
- id
- name
- sku
- category
- quantity

### Movements Table
Stores stock operations.

Fields:
- id
- product_id
- type (receive / deliver)
- quantity
- date

---

## Future Improvements

- User authentication (login/signup)
- Role-based access (manager / warehouse staff)
- Product search and filtering
- Multi-warehouse inventory tracking
- Data analytics and inventory reports

---

## Demo Workflow

1. Add product  
2. Receive stock  
3. Deliver stock  
4. Low stock detection  
5. View stock movement history  

---

## Project Goal

The goal of CoreInventory is to provide a simple and efficient solution for tracking inventory operations and maintaining accurate stock records in real time.
