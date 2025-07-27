import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    order_id TEXT NOT NULL,
    order_date DATE NOT NULL,
    order_subtotal FLOAT NOT NULL
  )
''')

users = [
  ('Alice', 'Smith', 'Alice Smith', 'alice@example.com', 'ORD001', '2024-06-01', 100.50),
  ('Bob', 'Johnson', 'Bob Johnson', 'bob@example.com', 'ORD002', '2024-06-02', 200.75),
  ('Charlie', 'Williams', 'Charlie Williams', 'charlie@example.com', 'ORD003', '2024-06-03', 150.00),
  ('David', 'Brown', 'David Brown', 'david@example.com', 'ORD004', '2024-06-04', 175.25),
  ('Eve', 'Jones', 'Eve Jones', 'eve@example.com', 'ORD005', '2024-06-05', 220.10),
  ('Frank', 'Garcia', 'Frank Garcia', 'frank@example.com', 'ORD006', '2024-06-06', 90.00),
  ('Grace', 'Miller', 'Grace Miller', 'grace@example.com', 'ORD007', '2024-06-07', 300.00),
  ('Heidi', 'Davis', 'Heidi Davis', 'heidi@example.com', 'ORD008', '2024-06-08', 50.75),
  ('Ivan', 'Martinez', 'Ivan Martinez', 'ivan@example.com', 'ORD009', '2024-06-09', 400.00),
  ('Judy', 'Lopez', 'Judy Lopez', 'judy@example.com', 'ORD010', '2024-06-10', 120.50),
  ('Mallory', 'Gonzalez', 'Mallory Gonzalez', 'mallory@example.com', 'ORD011', '2024-06-11', 250.00),
  ('Niaj', 'Wilson', 'Niaj Wilson', 'niaj@example.com', 'ORD012', '2024-06-12', 180.80),
  ('Alice', 'Smith', 'Alice Smith', 'alice@example.com', 'ORD013', '2024-06-15', 210.00),
  ('Bob', 'Johnson', 'Bob Johnson', 'bob@example.com', 'ORD014', '2024-06-16', 180.00),
  ('Charlie', 'Williams', 'Charlie Williams', 'charlie@example.com', 'ORD015', '2024-06-17', 175.50),
  ('Eve', 'Jones', 'Eve Jones', 'eve@example.com', 'ORD016', '2024-06-18', 99.99),
  ('Frank', 'Garcia', 'Frank Garcia', 'frank@example.com', 'ORD017', '2024-06-19', 110.00),
  ('Grace', 'Miller', 'Grace Miller', 'grace@example.com', 'ORD018', '2024-06-20', 320.00)
]

for i in range(len(users)):
    sql = f"INSERT INTO users \
      (first_name, last_name, name, email, order_id, order_date, order_subtotal) \
      VALUES ('{users[i][0]}', '{users[i][1]}', '{users[i][2]}', '{users[i][3]}', '{users[i][4]}', '{users[i][5]}', {users[i][6]})"
    cursor.execute(sql)

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

def get_users(rows):
  while True:
    for i in range(len(rows+1)):
      print(i)


conn.close()
