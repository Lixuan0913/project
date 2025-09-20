import sqlite3

# Create a connection to the SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('phones.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the phones table (if it doesn't exist)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS phones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        price INTEGER NOT NULL,
        image_filename TEXT NOT NULL
    )
""")

# Insert some sample data into the table (you can add as many rows as you like)
cursor.execute("INSERT INTO phones (brand, price, image_filename) VALUES (?, ?, ?)", ("iPhone", 3000, "iphone.jpg"))
cursor.execute("INSERT INTO phones (brand, price, image_filename) VALUES (?, ?, ?)", ("Samsung", 2000, "samsung.jpg"))
cursor.execute("INSERT INTO phones (brand, price, image_filename) VALUES (?, ?, ?)", ("Honor", 1000, "honor.jpg"))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database initialized and sample data added.")