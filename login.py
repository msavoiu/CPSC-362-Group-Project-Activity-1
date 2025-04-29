import sqlite3
from datetime import datetime
from collections import Counter
from database import *
import hashlib

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# SESSION ID OF CUSTOMER ID
session_customer_id = None


# CUSTOMER LOG IN
# Logs customer in and sets the session_customer_id to the customers ID to keep track of cart and order history
def Customer_login(email, password):
    global session_customer_id

    # HASHES PASSWORD
    password = password.strip()
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()

    cursor.execute('''
        SELECT customer_id, email FROM customers
        WHERE email = ? AND password = ?
    ''', (email, hex_dig))
    row = cursor.fetchone()
    
    if row:
        print("Login successful under email - " + str(row[1]))
        session_customer_id = row[0]  
    else:
        print("Invalid email or password.")
        return None
    
# CUSTOMER REGISTER / LOG IN
# Creates a new customer and logs them in, sets the session_customer_id to the customers ID to keep track of cart and order history
def Customer_register(email, password):
    global session_customer_id

    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()


    add_customer(email, hex_dig)
    
    cursor.execute('''
        SELECT customer_id, email FROM customers
        WHERE email = ? AND password = ?
    ''', (email, hex_dig))
    row = cursor.fetchone()
    
    if row:
        print("Login successful under email - " + str(row[1]))
        session_customer_id = row[0]  
    else:
        print("Error creating account")
        return None
    
    
    
# TESTING SECTION
#view_all_customers()
#Customer_register("two", "one")
#Customer_login("landon@gmail.com", "landonpassword")