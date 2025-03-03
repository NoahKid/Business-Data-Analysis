import sqlite3


conn = sqlite3.connect("business.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        product TEXT,
        category TEXT,
        revenue REAL,
        quantity INTEGER
    )
''')


sample_data = [
    ("2024-01-10", "Product A", "Electronics", 500.0, 5),
    ("2024-01-11", "Product B", "Clothing", 200.0, 10),
    ("2024-01-12", "Product C", "Electronics", 700.0, 7),
]

cursor.executemany("INSERT INTO sales_data (date, product, category, revenue, quantity) VALUES (?, ?, ?, ?, ?)", sample_data)
conn.commit()
conn.close()

print("Database setup complete!")
