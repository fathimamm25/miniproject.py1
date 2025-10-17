import sqlite3

# ---------- Database Setup ----------
conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Menu(
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    item_id INTEGER,
    quantity INTEGER NOT NULL,
    total_price REAL,
    FOREIGN KEY (item_id) REFERENCES Menu(item_id)
)
""")
conn.commit()


# ---------- Functions ----------

def add_menu_item():
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    category = input("Enter category (Starter/Main/Dessert/Drink): ")
    cursor.execute("INSERT INTO Menu(item_name, price, category) VALUES (?, ?, ?)", (name, price, category))
    conn.commit()
    print("Item added successfully!\n")

def view_menu():
    cursor.execute("SELECT * FROM Menu")
    items = cursor.fetchall()
    print("\n--- Menu ---")
    for item in items:
        print(f"ID:{item[0]} | {item[1]} - ₹{item[2]} ({item[3]})")
    print()

def update_menu_item():
    item_id = int(input("Enter item ID to update: "))
    new_price = float(input("Enter new price: "))
    cursor.execute("UPDATE Menu SET price=? WHERE item_id=?", (new_price, item_id))
    conn.commit()
    print("Item updated!\n")

def delete_menu_item():
    item_id = int(input("Enter item ID to delete: "))
    cursor.execute("DELETE FROM Menu WHERE item_id=?", (item_id,))
    conn.commit()
    print("Item deleted!\n")

def place_order():
    customer = input("Enter customer name: ")
    item_id = int(input("Enter item ID: "))
    quantity = int(input("Enter quantity: "))

    cursor.execute("SELECT price FROM Menu WHERE item_id=?", (item_id,))
    item = cursor.fetchone()
    if item:
        total = item[0] * quantity
        cursor.execute("INSERT INTO Orders(customer_name, item_id, quantity, total_price) VALUES (?, ?, ?, ?)", 
                       (customer, item_id, quantity, total))
        conn.commit()
        print(f"Order placed! Total = ₹{total}\n")
    else:
        print("Invalid Item ID!\n")

def view_orders():
    cursor.execute("""SELECT Orders.order_id, Orders.customer_name, Menu.item_name, Orders.quantity, Orders.total_price
                      FROM Orders JOIN Menu ON Orders.item_id = Menu.item_id""")
    orders = cursor.fetchall()
    print("\n--- Orders ---")
    for order in orders:
        print(f"OrderID:{order[0]} | Customer:{order[1]} | Item:{order[2]} | Qty:{order[3]} | Total:₹{order[4]}")
    print()


# ---------- CLI Menu ----------
while True:
    print("\n--- Restaurant Menu System ---")
    print("1. Add Menu Item")
    print("2. View Menu")
    print("3. Update Menu Item")
    print("4. Delete Menu Item")
    print("5. Place Order")
    print("6. View Orders")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_menu_item()
    elif choice == "2":
        view_menu()
    elif choice == "3":
        update_menu_item()
    elif choice == "4":
        delete_menu_item()
    elif choice == "5":
        place_order()
    elif choice == "6":
        view_orders()
    elif choice == "7":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.\n")

conn.close()
