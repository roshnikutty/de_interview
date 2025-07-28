import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL
  )
''')

cursor.execute('''
  CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    order_id TEXT NOT NULL,
    order_date DATE NOT NULL,
    order_subtotal FLOAT NOT NULL
  )
''')

users = [
  ('Alice', 'Smith', 'Alice Smith', 'alice@company.com'),
  ('Bob', 'Johnson', 'Bob Johnson', 'bob@company.com'),
  ('Charlie', 'Williams', 'Charlie Williams', 'charlie@company.com'),
  ('David', 'Brown', 'David Brown', 'david@company.com'),
  ('Eve', 'Jones', 'Eve Jones', 'eve@company.com'),
  ('Frank', 'Garcia', 'Frank Garcia', 'frank@company.com'),
  ('Grace', 'Miller', 'Grace Miller', 'grace@company.com'),
  ('Heidi', 'Davis', 'Heidi Davis', 'heidi@company.com'),
  ('Ivan', 'Martinez', 'Ivan Martinez', 'ivan@company.com'),
  ('Judy', 'Lopez', 'Judy Lopez', 'judy@company.com'),
  ('Mallory', 'Gonzalez', 'Mallory Gonzalez', 'mallory@company.com'),
  ('Niaj', 'Wilson', 'Niaj Wilson', 'niaj@company.com'),
  ('Alice', 'Smith', 'Alice Smith', 'alice@company.com'),
  ('Bob', 'Johnson', 'Bob Johnson', 'bob@company.com'),
  ('Charlie', 'Williams', 'Charlie Williams', 'charlie@company.com'),
  ('Eve', 'Jones', 'Eve Jones', 'eve@company.com'),
  ('Frank', 'Garcia', 'Frank Garcia', 'frank@company.com'),
  ('Grace', 'Miller', 'Grace Miller', 'grace@company.com')
]

orders = [
  ('alice@company.com', 'ORD001', '2024-06-01', 100.50),
  ('bob@company.com', 'ORD002', '2024-06-02', 200.75),
  ('charlie@company.com', 'ORD003', '2024-06-03', 150.00),
  ('david@company.com', 'ORD004', '2024-06-04', 175.25),
  ('eve@company.com', 'ORD005', '2024-06-05', 220.10),
  ('frank@company.com', 'ORD006', '2024-06-06', 90.00),
  ('grace@company.com', 'ORD007', '2024-06-07', 300.00),
  ('heidi@company.com', 'ORD008', '2024-06-08', 50.75),
  ('ivan@company.com', 'ORD009', '2024-06-09', 400.00),
  ('judy@company.com', 'ORD010', '2024-06-10', 120.50),
  ('mallory@company.com', 'ORD011', '2024-06-11', 250.00),
  ('niaj@company.com', 'ORD012', '2024-06-12', 180.80),
  ('alice@company.com', 'ORD013', '2024-06-15', 210.00),
  ('bob@company.com', 'ORD014', '2024-06-16', 180.00),
  ('charlie@company.com', 'ORD015', '2024-06-17', 175.50),
  ('eve@company.com', 'ORD016', '2024-06-18', 99.99),
  ('frank@company.com', 'ORD017', '2024-06-19', 110.00),
  ('grace@company.com', 'ORD018', '2024-06-20', 320.00)
]

for i in range(len(users)):
    sql = f"INSERT INTO users \
      (first_name, last_name, name, email) \
      VALUES ('{users[i][0]}', '{users[i][1]}', '{users[i][2]}', '{users[i][3]}')"
    cursor.execute(sql)

conn.commit()

for i in range(len(orders)):
    sql = f"INSERT INTO orders \
      (email, order_id, order_date, order_subtotal) \
      VALUES ('{orders[i][0]}', '{orders[i][1]}', '{orders[i][2]}', '{orders[i][3]}')"
    cursor.execute(sql)

conn.commit()

conn.close()


def get_users(rows):
  while True:
    for i in range(len(rows+1)):
      print(i)
