# Restaurant Management System

A simple Python CLI (Command Line Interface) project to manage a restaurant menu and customer orders.  
You can add, view, update, and delete menu items, place orders, and view all orders.

---

## Requirements

- Python 3.x installed on your system
- SQLite (comes built-in with Python)
- Optional: any terminal/console to run Python scripts

---

## How It Works

1. *Menu Management*: Add, view, update, and delete items in the restaurant menu.  
2. *Order Management*: Place customer orders by selecting item ID and quantity, and view all orders with totals.  
3. *Database*: Uses SQLite database restaurant.db to store menu and order data.

---

## Database Schema

### Menu Table
| Column     | Type    | Description               |
|-----------|---------|---------------------------|
| item_id   | INTEGER | Primary key               |
| item_name | TEXT    | Name of the menu item     |
| price     | REAL    | Price of the item         |
| category  | TEXT    | Food category (Starter/Main/Dessert/Drink) |

### Orders Table
| Column        | Type    | Description                      |
|---------------|---------|----------------------------------|
| order_id      | INTEGER | Primary key                      |
| customer_name | TEXT    | Name of the customer             |
| item_id       | INTEGER | Foreign key referencing Menu     |
| quantity      | INTEGER | Quantity ordered                 |
