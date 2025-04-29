import unittest
import json
import os
import sqlite3
import hashlib
from app import app, DATABASE, get_db, close_db

class TestECommerceAPI(unittest.TestCase):
    
    def setUp(self):
        # Configure the Flask app for testing
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        
        # Create and populate a test database
        self.setup_test_database()

    def tearDown(self):
        # Clean up after each test
        os.remove('test_database.db')

    def setup_test_database(self):
        # Override the DATABASE global for testing
        global DATABASE
        app.config['DATABASE'] = 'test_database.db'
        DATABASE = 'test_database.db'
        
        # Create test database and tables
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Create inventory table
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
        
        # Create customers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                password TEXT
            )
        ''')
        
        # Create cart table
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
        
        # Create ordered_items table
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
        
        # Insert test data
        # Add test products
        cursor.execute('''
            INSERT INTO inventory (color, size, quantity, description, image_url)
            VALUES (?, ?, ?, ?, ?)
        ''', ('Red', 'Large', 10, 'Test T-shirt', 'https://example.com/image1.jpg'))
        
        cursor.execute('''
            INSERT INTO inventory (color, size, quantity, description, image_url)
            VALUES (?, ?, ?, ?, ?)
        ''', ('Blue', 'Medium', 5, 'Test Jeans', 'https://example.com/image2.jpg'))
        
        # Add test customer
        hashed_password = hashlib.sha256('testpassword'.encode()).hexdigest()
        cursor.execute('''
            INSERT INTO customers (email, password)
            VALUES (?, ?)
        ''', ('test@example.com', hashed_password))
        
        conn.commit()
        conn.close()
    
    # Authentication Tests
    def test_login_success(self):
        response = self.app.post('/api/login', json={
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Login successful')
        self.assertIn('user_id', data)
    
    def test_login_invalid_credentials(self):
        response = self.app.post('/api/login', json={
            'email': 'test@example.com',
            'password': 'wrongpassword'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Invalid credentials!')
    
    def test_login_missing_data(self):
        response = self.app.post('/api/login', json={
            'email': 'test@example.com'
            # Missing password
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Email and password are required')
    
    def test_register_success(self):
        response = self.app.post('/api/register', json={
            'email': 'new@example.com',
            'password': 'newpassword'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Registration successful')
        self.assertIn('user_id', data)
    
    def test_register_existing_email(self):
        response = self.app.post('/api/register', json={
            'email': 'test@example.com',  # Already exists in test data
            'password': 'newpassword'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(data['message'], 'Email already exists!')
    
    # Catalog Tests
    def test_get_catalog(self):
        response = self.app.get('/api/catalog')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('products', data)
        self.assertEqual(len(data['products']), 2)  # We added 2 test products
    
    # Search Tests
    def test_search_inventory_success(self):
        response = self.app.post('/api/search', json={
            'keyword': 'Hoodie'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', data)
        self.assertEqual(len(data['results']), 1)  # Should find the t-shirt
        self.assertEqual(data['results'][0]['description'], 'Vital Hoodie')
    
    def test_search_inventory_no_results(self):
        response = self.app.post('/api/search', json={
            'keyword': 'nonexistent'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'No matching items found')
    
    # Cart Tests (with authenticated session)
    def test_add_to_cart(self):
        # Login first
        with self.app as client:
            # Login to set the session
            client.post('/api/login', json={
                'email': 'test@example.com',
                'password': 'testpassword'
            })
            
            # Add item to cart
            response = client.post('/api/cart/add', json={
                'product_id': 1,
                'quantity': 2
            })
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Added 2 of Product ID 1 to cart', data['message'])
            
            # Check cart contents
            response = client.get('/api/cart')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('cart', data)
            self.assertEqual(len(data['cart']), 1)
            self.assertEqual(data['cart'][0]['quantity'], 2)
    
    def test_remove_from_cart(self):
        # Login and add item to cart first
        with self.app as client:
            client.post('/api/login', json={
                'email': 'test@example.com',
                'password': 'testpassword'
            })
            client.post('/api/cart/add', json={
                'product_id': 1,
                'quantity': 3
            })
            
            # Remove 1 item from cart
            response = client.post('/api/cart/remove', json={
                'product_id': 1,
                'quantity': 1
            })
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Removed 1 of Product ID 1 from cart', data['message'])
            
            # Check cart contents
            response = client.get('/api/cart')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['cart'][0]['quantity'], 2)
    
    def test_remove_all_from_cart(self):
        with self.app as client:
            client.post('/api/login', json={
                'email': 'test@example.com',
                'password': 'testpassword'
            })
            client.post('/api/cart/add', json={
                'product_id': 1,
                'quantity': 2
            })
            
            # Remove all items
            response = client.post('/api/cart/remove', json={
                'product_id': 1,
                'quantity': 5  # More than in cart
            })
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Removed entire Product ID 1 from cart', data['message'])
            
            # Check cart is empty
            response = client.get('/api/cart')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['cart']), 0)
    
    # Checkout Tests
    def test_checkout_success(self):
        with self.app as client:
            client.post('/api/login', json={
                'email': 'test@example.com',
                'password': 'testpassword'
            })
            client.post('/api/cart/add', json={
                'product_id': 1,
                'quantity': 2
            })
            
            # Checkout
            response = client.post('/api/checkout')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Order placed for customer ID', data['message'])
            
            # Check cart is empty
            response = client.get('/api/cart')
            data = json.loads(response.data)
            self.assertEqual(len(data['cart']), 0)
            
            # Check order in profile
            response = client.get('/api/profile')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('order_history', data)
            self.assertEqual(len(data['order_history']), 1)
            self.assertEqual(data['order_history'][0]['product_id'], 1)
            self.assertEqual(data['order_history'][0]['quantity'], 2)
    
    def test_checkout_insufficient_stock(self):
        with self.app as client:
            client.post('/api/login', json={
                'email': 'test@example.com',
                'password': 'testpassword'
            })
            client.post('/api/cart/add', json={
                'product_id': 1,
                'quantity': 20  # More than available (10)
            })
            
            # Checkout should fail
            response = client.post('/api/checkout')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 400)
            self.assertIn('Not enough stock', data['message'])
    
    # Profile Tests
    def test_profile_authenticated(self):
        with self.app as client:
            client.post('/api/login', json={
                'email': 'test@example.com',
                'password': 'testpassword'
            })
            
            response = client.get('/api/profile')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn('user', data)
            self.assertEqual(data['user']['email'], 'test@example.com')
    
    def test_profile_unauthenticated(self):
        response = self.app.get('/api/profile')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Unauthorized')
    
    # Customer Listing Test
    def test_get_all_customers(self):
        response = self.app.get('/api/customers')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('customers', data)
        self.assertGreaterEqual(len(data['customers']), 1)  # At least our test customer

if __name__ == '__main__':
    unittest.main()