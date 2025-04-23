from flask import Flask, request, jsonify, session
import sqlite3
import hashlib
from datetime import datetime
from collections import Counter

app = Flask(__name__)
app.secret_key = '362'  #key

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def close_db(conn):
    if conn:
        conn.close()

#Databse functions
def add_product(color, size, quantity, description):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO inventory (color, size, quantity, description)
        VALUES (?, ?, ?, ?)
    ''', (color, size, quantity, description))
    conn.commit()
    close_db(conn)
    return True

def view_all_products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT product_id, color, size, quantity, description FROM inventory')
    products = cursor.fetchall()
    close_db(conn)
    return [dict(row) for row in products]

def add_customer(email, password):
    conn = get_db()
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        cursor.execute('''
            INSERT INTO customers (email, password)
            VALUES (?, ?)
        ''', (email, hashed_password))
        conn.commit()
        close_db(conn)
        return True
    except sqlite3.IntegrityError:
        close_db(conn)
        return False

def get_customer_by_email(email):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id, email, password FROM customers WHERE email = ?", (email,))
    user = cursor.fetchone()
    close_db(conn)
    return user

def get_customer_by_id(customer_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id, email FROM customers WHERE customer_id = ?", (customer_id,))
    user = cursor.fetchone()
    close_db(conn)
    return user

def view_order_history(customer_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT order_id, order_date, product_id, quantity
        FROM ordered_items
        WHERE customer_id = ?
        ORDER BY order_id
    ''', (customer_id,))
    orders = cursor.fetchall()
    results = []
    for order in orders:
        cursor.execute("SELECT color, size, description FROM inventory WHERE product_id = ?", (order['product_id'],))
        info = cursor.fetchone()
        results.append({
            'order_id': order['order_id'],
            'order_date': order['order_date'],
            'product_id': order['product_id'],
            'quantity': order['quantity'],
            'color': info['color'] if info else None,
            'size': info['size'] if info else None,
            'description': info['description'] if info else None
        })
    close_db(conn)
    return results

def add_to_cart(customer_id, product_id, quantity):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT quantity FROM inventory WHERE product_id = ?", (product_id,))
    row = cursor.fetchone()
    if not row:
        close_db(conn)
        return False, f"Product ID {product_id} not found."
    if row['quantity'] < quantity:
        close_db(conn)
        return False, f"Not enough stock. Available: {row['quantity']}, Requested: {quantity}"

    cursor.execute('''
        INSERT INTO cart (customer_id, product_id, quantity)
        VALUES (?, ?, ?)
        ON CONFLICT(customer_id, product_id) DO UPDATE SET quantity = quantity + excluded.quantity
    ''', (customer_id, product_id, quantity))
    conn.commit()
    close_db(conn)
    return True, f"Added {quantity} of Product ID {product_id} to cart."

def view_cart(customer_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT c.product_id, i.color, i.size, i.description, c.quantity
        FROM cart c
        JOIN inventory i ON c.product_id = i.product_id
        WHERE c.customer_id = ?
    ''', (customer_id,))
    items = cursor.fetchall()
    close_db(conn)
    return [dict(row) for row in items]

def place_order_from_cart(customer_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT product_id, quantity FROM cart WHERE customer_id = ?', (customer_id,))
    cart_items = cursor.fetchall()
    if not cart_items:
        close_db(conn)
        return False, "Cart is empty."

    order_date = datetime.now().strftime('%Y-%m-%d')
    success = True
    errors = []

    for item in cart_items:
        product_id = item['product_id']
        quantity = item['quantity']

        cursor.execute("SELECT quantity FROM inventory WHERE product_id = ?", (product_id,))
        stock = cursor.fetchone()
        if not stock or stock['quantity'] < quantity:
            success = False
            errors.append(f"Not enough stock for Product ID {product_id}. Available: {stock['quantity'] if stock else 0}, Needed: {quantity}")
            continue

        cursor.execute('''
            INSERT INTO ordered_items (customer_id, order_date, product_id, quantity)
            VALUES (?, ?, ?, ?)
        ''', (customer_id, order_date, product_id, quantity))
        cursor.execute('''
            UPDATE inventory SET quantity = quantity - ?
            WHERE product_id = ?
        ''', (quantity, product_id))

    if success:
        cursor.execute('DELETE FROM cart WHERE customer_id = ?', (customer_id,))
        conn.commit()
        close_db(conn)
        return True, f"Order placed for customer ID {customer_id}."
    else:
        conn.rollback()
        close_db(conn)
        return False, "\n".join(errors)

# --- API Routes ---
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No JSON data provided'}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user = get_customer_by_email(email)

    if user:
        hashed_provided_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_provided_password == user['password']:
            session['user_id'] = user['customer_id']
            return jsonify({'message': 'Login successful', 'user_id': user['customer_id']}), 200
        else:
            return jsonify({'message': 'Invalid credentials!'}), 401
    else:
        return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No JSON data provided'}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required!'}), 400

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if add_customer(email, hashed_password):
        user = get_customer_by_email(email)
        session['user_id'] = user['customer_id']
        return jsonify({'message': 'Registration successful', 'user_id': user['customer_id']}), 201
    else:
        return jsonify({'message': 'Email already exists!'}), 409 # Conflict

@app.route('/api/profile', methods=['GET'])
def profile():
    if 'user_id' in session:
        user_id = session['user_id']
        user = get_customer_by_id(user_id)
        if user:
            order_history = view_order_history(user_id)
            return jsonify({'user': {'email': user['email'], 'customer_id': user['customer_id']}, 'order_history': order_history}), 200
        else:
            return jsonify({'message': 'User not found!'}), 404
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@app.route('/api/catalog', methods=['GET'])
def catalog():
    products = view_all_products()
    return jsonify({'products': products}), 200

@app.route('/api/cart', methods=['GET'])
def get_cart():
    if 'user_id' in session:
        cart_items = view_cart(session['user_id'])
        return jsonify({'cart': cart_items}), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@app.route('/api/cart/add', methods=['POST'])
def add_item_to_cart():
    if 'user_id' in session:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No JSON data provided'}), 400
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        if not product_id:
            return jsonify({'message': 'Product ID is required'}), 400

        success, message = add_to_cart(session['user_id'], product_id, quantity)
        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'message': message}), 400
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@app.route('/api/checkout', methods=['POST'])
def checkout():
    if 'user_id' in session:
        success, message = place_order_from_cart(session['user_id'])
        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'message': message}), 400
    else:
        return jsonify({'message': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run(debug=True)
