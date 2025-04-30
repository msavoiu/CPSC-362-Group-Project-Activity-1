import unittest
import json
import os
import sqlite3
import hashlib
from app import app, DATABASE, get_db, close_db

class TestVitalApp(unittest.TestCase):
    # Tests API for authentication, product catalog, adding to cart, and user profile.
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.setup_test_database()

    def tearDown(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cart')
        conn.commit()
        conn.close()
        os.remove('test_database.db')

    def clear_cart(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cart')
        conn.commit()
        conn.close()
    
    # Creates a test database
    def setup_test_database(self):
        global DATABASE
        app.config['DATABASE'] = 'test_database.db'
        DATABASE = 'test_database.db'
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                color TEXT,
                size TEXT,
                quantity INTEGER,
                description TEXT,
                image_url TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                password TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cart (
                customer_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                PRIMARY KEY (customer_id, product_id),
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (product_id) REFERENCES inventory(product_id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ordered_items (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                order_date TEXT,
                product_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (product_id) REFERENCES inventory(product_id)
            )
        ''')
        
        hashed_password = hashlib.sha256('password1'.encode()).hexdigest()
        cursor.execute('''
            INSERT INTO customers (email, password)
            VALUES (?, ?)
        ''', ('user1@gmail.com', hashed_password))
        
        conn.commit()
        conn.close()
    
    # Tests a successful login with user email and password
    def test_login_success(self):
        response = self.app.post('/api/login', json={
            'email': 'user1@gmail.com',
            'password': 'password1'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Login successful')
        self.assertIn('user_id', data)
    
    # Tests login with invalid user email or password
    def test_login_invalid_credentials(self):
        response = self.app.post('/api/login', json={
            'email': 'user1@gmail.com',
            'password': 'wrongpassword'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Invalid credentials!')
    
    # Tests login with a missing password
    def test_login_missing_data(self):
        response = self.app.post('/api/login', json={
            'email': 'user1@gmail.com'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Email and password are required')
    
    # Tests registering a profile with an already existing email
    def test_register_existing_email(self):
        response = self.app.post('/api/register', json={
            'email': 'user1@gmail.com',
            'password': 'password1'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(data['message'], 'Email already exists!')
    
    # Tests the product catalog
    def test_get_catalog(self):
        response = self.app.get('/api/catalog')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('products', data)
        self.assertEqual(len(data['products']), 2)
    
    # Tests a successful search for a product in the inventory
    def test_search_inventory_success(self):
        response = self.app.post('/api/search', json={
            'keyword': 'Hoodie'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', data)
        self.assertEqual(len(data['results']), 1)
        self.assertEqual(data['results'][0]['description'], 'Vital Hoodie')
    
    # Tests a search with a keyword that doesn't match a product in the inventory
    def test_search_inventory_no_results(self):
        response = self.app.post('/api/search', json={
            'keyword': 'nonexistent'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'No matching items found')
    
    # Adds items to cart and clears cart before each test run
    def test_add_to_cart(self):
        self.clear_cart()
        
        with self.app as client:
            client.post('/api/login', json={
                'email': 'user1@gmail.com',
                'password': 'password1'
            })
            response = client.post('/api/cart/add', json={
                'product_id': 1,
                'quantity': 2
            })
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Added 2 of Product ID 1 to cart', data['message'])
            response = client.get('/api/cart')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('cart', data)
            self.assertEqual(len(data['cart']), 1)
            self.assertEqual(data['cart'][0]['quantity'], data['cart'][0]['quantity'])
    
    # Tests if the user email and password is authenticated properly
    def test_profile_authenticated(self):
        with self.app as client:
            client.post('/api/login', json={
                'email': 'user1@gmail.com',
                'password': 'password1'
            })
            response = client.get('/api/profile')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('user', data)
            self.assertEqual(data['user']['email'], 'user1@gmail.com')
    
    # Tests if user email and password is unauthorized
    def test_profile_unauthenticated(self):
        response = self.app.get('/api/profile')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Unauthorized')
    
    # Get's all the current customers
    def test_get_all_customers(self):
        response = self.app.get('/api/customers')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('customers', data)
        self.assertGreaterEqual(len(data['customers']), 1)

if __name__ == '__main__':
    unittest.main()
