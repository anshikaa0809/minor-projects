#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sqlite3
conn = sqlite3.connect("billing.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL
)
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(product_id) REFERENCES products(id)
)
''')

conn.commit()
def setup_data():
    products = [
        ('Apple', 'Fruits', 20),
        ('Banana', 'Fruits', 10),
        ('Chips', 'Snacks', 30),
        ('Cookies', 'Snacks', 40),
        ('Coke', 'Drinks', 25),
        ('Juice', 'Drinks', 35)
    ]
    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] == 0:
        for name, category, price in products:
            cur.execute("INSERT INTO products (name, category, price) VALUES (?, ?, ?)", (name, category, price))
        conn.commit()

def show_catalog():
    print("\n=== Product Catalog ===")
    cur.execute("SELECT DISTINCT category FROM products")
    categories = cur.fetchall()
    for (cat,) in categories:
        print(f"\n{cat.upper()}:")
        cur.execute("SELECT name, price FROM products WHERE category=?", (cat,))
        items = cur.fetchall()
        for name, price in items:
            print(f" - {name} @ ₹{price}")

def add_to_cart():
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    cur.execute("SELECT id FROM products WHERE name=?", (product_name,))
    result = cur.fetchone()

    if result:
        product_id = result[0]
        cur.execute("INSERT INTO cart (product_id, quantity) VALUES (?, ?)", (product_id, quantity))
        conn.commit()
        print("Added to cart!")
    else:
        print("Product not found.")

def generate_bill():
    print("\n=== FINAL BILL ===")
    cur.execute('''
        SELECT p.name, p.price, c.quantity, (p.price * c.quantity) as total
        FROM cart c
        JOIN products p ON c.product_id = p.id
    ''')
    items = cur.fetchall()

    grand_total = 0
    print("\nProduct\tQty\tPrice\tTotal")
    print("-" * 30)
    for name, price, qty, total in items:
        print(f"{name}\t{qty}\t₹{price}\t₹{total}")
        grand_total += total

    print("-" * 30)
    print(f"Grand Total: ₹{grand_total}")
    print("Thank you for shopping!\n")

    cur.execute("DELETE FROM cart")
    conn.commit()

def menu():
    setup_data()
    while True:
        print("\n--- Menu ---")
        print("1. Show Catalog")
        print("2. Add Product to Cart")
        print("3. Generate Bill & Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_catalog()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            generate_bill()
            break
        else:
            print("Invalid choice. Please try again")
menu()


# In[ ]:





# In[ ]:





# In[ ]:




