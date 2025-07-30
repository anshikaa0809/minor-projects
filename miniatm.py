#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
conn=sqlite3.connect("stu.db")
cur=conn.cursor()


# In[2]:


cur.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')
conn.commit()
print("Table created successfully.")


# In[3]:


def insert_student(name, age, grade):
    cur.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print("Student inserted successfully.")
insert_student('anshika', 20, 'A')
insert_student('palak', 22, 'B')
insert_student('athira', 24, 'c')


# In[4]:


def fetch_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
fetch_students()


# In[5]:


def update_student(student_id, new_name, new_age, new_grade):
    cur.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (new_name, new_age, new_grade, student_id))
    conn.commit()
    print("Student updated successfully.")
update_student(1, 'shiv', 21, 'A')
update_student(2, 'tanmay', 23, 'B')


# In[6]:


def fetch_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
fetch_students()


# In[7]:


def delete_student(student_id):
    cur.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("deleted successfully.")
delete_student(5)


# In[8]:


conn.close()
print("Database connection closed.")


# In[9]:


import sqlite3
conn = sqlite3.connect("atm.db")
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    pin TEXT,
    balance REAL
)
''')
conn.commit()


# In[10]:


def create_account(name, pin, balance):
    cur.execute("INSERT INTO accounts (name, pin, balance) VALUES (?, ?, ?)", (name, pin, balance))
    conn.commit()
    print(" Account created successfully!")
create_account('anshika',1234,50000)
create_account('palak', 24321,40000)
create_account('athira',3456,5000)


# In[11]:


def login(acc_no, pin):
    cur.execute("SELECT * FROM accounts WHERE acc_no=? AND pin=?", (acc_no, pin))
    user = cur.fetchone()
    if user:
        print(f" Welcome {user[1]}!")
        return user
    else:
        print(" Invalid account number or PIN.")
        return None
login(1,1634)


# In[12]:


def check_balance(acc_no):
    cur.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
    balance = cur.fetchone()[0]
    print(f"Current Balance: ₹{balance}")
check_balance(1)


# In[13]:


def deposit(acc_no, amount):
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE acc_no=?", (amount, acc_no))
    conn.commit()
    print(f" ₹{amount} deposited successfully.")
deposit(3,60000)


# In[14]:


def withdraw(acc_no, amount):
    cur.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
    current_balance = cur.fetchone()[0]

    if amount > current_balance:
        print(" Insufficient balance!")
    else:
        cur.execute("UPDATE accounts SET balance = balance - ? WHERE acc_no=?", (amount, acc_no))
        conn.commit()
        print(f" ₹{amount} withdrawn successfully.")
withdraw(1,2000)


# In[15]:


def atm_menu():
    print("===== Welcome to Python ATM =====")
    acc_no = int(input("Enter Account Number: "))
    pin = input("Enter PIN: ")

    user = login(acc_no, pin)
    if not user:
        return

    while True:
        print("\n--- Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            check_balance(acc_no)
        elif choice == '2':
            amt = float(input("Enter amount to deposit: ₹"))
            deposit(acc_no, amt)
        elif choice == '3':
            amt = float(input("Enter amount to withdraw: ₹"))
            withdraw(acc_no, amt)
        elif choice == '4':
            print(" Thank you for using the ATM. Bye!")
            break
        else:
            print("Invalid choice.")
atm_menu()


# In[16]:


atm_menu()
conn.close()

