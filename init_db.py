import sqlite3

conn = sqlite3.connect('phones.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS phones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        price INTEGER NOT NULL,
        image_filename TEXT NOT NULL
    )
""")

cursor.execute("INSERT INTO phones (brand, price, image_filename) VALUES (?, ?, ?)", ("iPhone", 3000, "iphone.jpg"))
cursor.execute("INSERT INTO phones (brand, price, image_filename) VALUES (?, ?, ?)", ("Samsung", 2000, "samsung.jpg"))
cursor.execute("INSERT INTO phones (brand, price, image_filename) VALUES (?, ?, ?)", ("Honor", 1000, "honor.jpg"))

conn.commit()
conn.close()

print("Database initialized and sample data added.")