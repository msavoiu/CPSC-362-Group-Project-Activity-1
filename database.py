import sqlite3
from datetime import datetime
from collections import Counter

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# TABLES


cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT NOT NULL,
    size TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    description TEXT,
    image_url TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS cart (
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES inventory(product_id),
    PRIMARY KEY (customer_id, product_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ordered_items (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES inventory(product_id)
)
''')

conn.commit()


# ADDS PRODUCT TO INVENTORY
def add_product(color, size, quantity, description, image_url):
    cursor.execute('''
        INSERT INTO inventory (color, size, quantity, description, image_url)
        VALUES (?, ?, ?, ?, ?)
    ''', (color, size, quantity, description, image_url))
    conn.commit()
    print("Product added to inventory.")
    
# REMOVES PRODUCT FROM INVENTORY
def remove_product(product_id):
    cursor.execute("SELECT * FROM inventory WHERE product_id = ?", (product_id,))
    if not cursor.fetchone():
        print(f"No product found with ID {product_id}.")
        return

    cursor.execute("DELETE FROM cart WHERE product_id = ?", (product_id,))
    cursor.execute("DELETE FROM ordered_items WHERE product_id = ?", (product_id,))
    cursor.execute("DELETE FROM inventory WHERE product_id = ?", (product_id,))
    conn.commit()
    print(f"Product ID {product_id} and related data removed.")



# LISTS ALL PRODUCTS
def view_all_products():
    cursor.execute('SELECT product_id, color, size, quantity, description, image_url FROM inventory')
    products = cursor.fetchall()
    if not products:
        print("Inventory is empty.")
        return
    print("All Products in Inventory:")
    for p in products:
        print(f"ID {p[0]} | {p[1]} {p[2]} — {p[3]} in stock — {p[4]} | Image URL: {p[5]}")


# ADDS CUSTOMER
def add_customer(email, password):
    cursor.execute('''
        INSERT INTO customers (email, password)
        VALUES (?, ?)
    ''', (email, password))
    conn.commit()
    print("Customer added.")

# LISTS ALL CUSTOMERS
def view_all_customers():
    cursor.execute('SELECT customer_id, email, password FROM customers')
    customers = cursor.fetchall()
    if not customers:
        print("No customers found.")
        return

    print("👥 All Customers:")
    for customer in customers:
        print(f"ID {customer[0]} | Email: {customer[1]} | Password: {customer[2]}")

# REMOVES CUSTOMER
def remove_customer(customer_id):
    cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
    if not cursor.fetchone():
        print(f" No customer with ID {customer_id}")
        return

    cursor.execute("DELETE FROM cart WHERE customer_id = ?", (customer_id,))
    cursor.execute("DELETE FROM ordered_items WHERE customer_id = ?", (customer_id,))
    cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
    conn.commit()
    print(f"Customer ID {customer_id} and all associated data deleted.")

# ADD MORE PRODUCT STOCK
def restock_product(product_id, amount):
    cursor.execute("SELECT quantity FROM inventory WHERE product_id = ?", (product_id,))
    row = cursor.fetchone()
    if not row:
        print(f"Product ID {product_id} not found.")
        return
    cursor.execute('''
        UPDATE inventory SET quantity = quantity + ?
        WHERE product_id = ?
    ''', (amount, product_id))
    conn.commit()
    print(f"Restocked Product ID {product_id} by {amount}. New quantity: {row[0] + amount}")


# ADDS ITEMS TO CART
def add_to_cart(customer_id, product_id, quantity):
    cursor.execute("SELECT quantity FROM inventory WHERE product_id = ?", (product_id,))
    row = cursor.fetchone()
    if not row:
        print(f"Product ID {product_id} not found.")
        return
    if row[0] < quantity:
        print(f"Not enough stock. Available: {row[0]}, Requested: {quantity}")
        return

    cursor.execute('''
        INSERT INTO cart (customer_id, product_id, quantity)
        VALUES (?, ?, ?)
        ON CONFLICT(customer_id, product_id) DO UPDATE SET quantity = quantity + excluded.quantity
    ''', (customer_id, product_id, quantity))
    conn.commit()
    print(f"Added {quantity} of Product ID {product_id} to cart.")

# VIEWS ITEMS IN CART
def view_cart(customer_id):
    cursor.execute('''
        SELECT c.product_id, i.color, i.size, i.description, c.quantity
        FROM cart c
        JOIN inventory i ON c.product_id = i.product_id
        WHERE c.customer_id = ?
    ''', (customer_id,))
    items = cursor.fetchall()
    if not items:
        print("Cart is empty.")
        return
    print(f"🛒 Cart for customer ID {customer_id}:")
    for item in items:
        print(f"- {item[4]}x {item[1]} {item[2]} — {item[3]} (Product ID: {item[0]})")


# CLEARS CART
def clear_cart(customer_id):
    cursor.execute("DELETE FROM cart WHERE customer_id = ?", (customer_id,))
    conn.commit()
    print("Cart cleared.")

# ORDERES ITEMS IN CART AND CLEARS CART
def place_order_from_cart(customer_id):
    cursor.execute('SELECT product_id, quantity FROM cart WHERE customer_id = ?', (customer_id,))
    cart_items = cursor.fetchall()
    if not cart_items:
        print("Cart is empty.")
        return

    for pid, qty in cart_items:
        cursor.execute("SELECT quantity FROM inventory WHERE product_id = ?", (pid,))
        stock = cursor.fetchone()
        if stock[0] < qty:
            print(f"Not enough stock for Product ID {pid}. Available: {stock[0]}, Needed: {qty}")
            return

    order_date = datetime.now().strftime('%Y-%m-%d')

    for pid, qty in cart_items:
        cursor.execute('''
            INSERT INTO ordered_items (customer_id, order_date, product_id, quantity)
            VALUES (?, ?, ?, ?)
        ''', (customer_id, order_date, pid, qty))
        cursor.execute('''
            UPDATE inventory SET quantity = quantity - ?
            WHERE product_id = ?
        ''', (qty, pid))

    cursor.execute('DELETE FROM cart WHERE customer_id = ?', (customer_id,))
    conn.commit()
    print(f"Order placed for customer ID {customer_id}.")

# ORDER HISTORY
def view_order_history(customer_id):
    cursor.execute('''
        SELECT order_id, order_date, product_id, quantity
        FROM ordered_items
        WHERE customer_id = ?
        ORDER BY order_id
    ''', (customer_id,))
    orders = cursor.fetchall()
    if not orders:
        print("No order history found.")
        return

    print(f"Order history for customer ID {customer_id}:")
    for order in orders:
        cursor.execute("SELECT color, size, description FROM inventory WHERE product_id = ?", (order[2],))
        info = cursor.fetchone()
        print(f"- Order ID {order[0]} | {order[3]}x {info[0]} {info[1]} — {info[2]} | Date: {order[1]}")
        
# REMOVES ALL CUSTOMERS
def remove_all_customers():
  
    cursor.execute("DELETE FROM cart")
    cursor.execute("DELETE FROM ordered_items")
    cursor.execute("DELETE FROM customers")
    
 
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='customers'")
    
    conn.commit()
    print("All customers and related data have been deleted. Customer ID counter reset.")

def search_inventory_by_description(keyword):
    keyword = f"%{keyword}%"
    cursor.execute('''
        SELECT product_id, color, size, quantity, description, image_url
        FROM inventory
        WHERE description LIKE %?%
    ''', (keyword,))
    results = cursor.fetchall()

    if not results:
        print("No matching items found.")
        return

    print(f"🔍 Search results for description containing '{keyword.strip('%')}':")
    for item in results:
        print(f"ID {item[0]} | {item[1]} {item[2]} — {item[3]} in stock — {item[4]} | Image URL: {item[5]}")
        
        
def edit_product(product_id, color=None, size=None, quantity=None, description=None, image_url=None):
    cursor.execute("SELECT * FROM inventory WHERE product_id = ?", (product_id,))
    if not cursor.fetchone():
        print(f"No product found with ID {product_id}.")
        return

    updates = []
    values = []

    if color is not None:
        updates.append("color = ?")
        values.append(color)
    if size is not None:
        updates.append("size = ?")
        values.append(size)
    if quantity is not None:
        updates.append("quantity = ?")
        values.append(quantity)
    if description is not None:
        updates.append("description = ?")
        values.append(description)
    if image_url is not None:
        updates.append("image_url = ?")
        values.append(image_url)

    if not updates:
        print("No fields provided to update.")
        return

    update_clause = ", ".join(updates)
    values.append(product_id)

    cursor.execute(f'''
        UPDATE inventory
        SET {update_clause}
        WHERE product_id = ?
    ''', values)

    conn.commit()
    print(f" Product ID {product_id} has been updated.")
    
# REMOVES ITEM FROM CART
def remove_from_cart(customer_id, product_id, quantity):
    cursor.execute('''
        SELECT quantity FROM cart WHERE customer_id = ? AND product_id = ?
    ''', (customer_id, product_id))
    row = cursor.fetchone()

    if not row:
        print(f"No such item in the cart for customer ID {customer_id} and product ID {product_id}.")
        return

    current_quantity = row[0]

    if quantity >= current_quantity:
        cursor.execute('''
            DELETE FROM cart WHERE customer_id = ? AND product_id = ?
        ''', (customer_id, product_id))
        print(f"Removed entire Product ID {product_id} from customer ID {customer_id}'s cart.")
    else:
        cursor.execute('''
            UPDATE cart SET quantity = quantity - ?
            WHERE customer_id = ? AND product_id = ?
        ''', (quantity, customer_id, product_id))
        print(f"Removed {quantity} of Product ID {product_id} from customer ID {customer_id}'s cart.")

    conn.commit()

# SETUP
add_product("Black", "One Size", 100, "Vital Hoodie", "/hoodie.png")
add_product("Mauve", "One Size", 100, "Vital Tee", "/shirt.png")
view_all_products()

# FUNCTION CHEAT SHEET
# add_product(color, size, quantity, description, image_URL)
# view_all_products()
# restock_product(product_id, ammount)
# add_to_cart(customer_id, product_id, quantity)
# view_cart(customer_id)
# clear_cart(customer_id)
# place_order_from_cart(customer_id)
# view_order_history(customer_id)
#add_product("yellow", "small", "20", "Small Yellow Windbreaker", "small_yellow_windbreaker.png")
#view_all_products()
#view_all_customers()