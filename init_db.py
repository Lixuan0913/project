import sqlite3

conn = sqlite3.connect('phones.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS phones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model_name TEXT NOT NULL,
        price INTEGER NOT NULL,
        image_filename TEXT NOT NULL,
        description TEXT NOT NULL
    )
""")

cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, description) VALUES (?, ?, ?, ?, ?)", ("iPhone",'iPhone 15', 2699, "i15.png", "Colour: Black, Silver, Blue, Capacity: 128GB,256GB, 512GB, Size:147.6 mm x 71.6 mm x 7.80 mm,173g, 6.1‑inch (diagonal) all‑screen OLED display, CPU: Octa-Core CPU, Adreno 619 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, description) VALUES (?, ?, ?, ?, ?)", ("iPhone",'iPhone 14', 2299, "i14.png", "Colour: Starlight, Purple,Blue, Midnight, Yellow, Capacity: 128GB, 256GB, 512GB ,Size:146.7 mm x 71.5 mm x 7.80 mm, 172g, 6.1‑inch (diagonal) all‑screen OLED display,CPU: 6‑core CPU with 2 performance and 4 efficiency cores, 5-core GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, description) VALUES (?, ?, ?, ?, ?)", ("iPhone",'iPhone 13', 1999, "i13.png", "Colour: Starlight, Midnight,Blue, Pink, Green, Capacity: 128GB, 256GB, 512GB ,Size:146.7 mm x 71.5 mm x 7.65 mm,173g, 6.1‑inch (diagonal) all‑screen OLED display,CPU: 6‑core CPU with 2 performance and 4 efficiency cores, 4-core GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, description) VALUES (?, ?, ?, ?, ?)", ("Samsung",'Samsung Galaxy A35', 1399, "s35.png", "Colour: Iceblue, Lilac, Navy,Lemon, Capacity: 128GB, 256GB, Size:161.7 x 78 x 8.2 mm, 209 g, 6.6 inches Super AMOLED display,CPU: Octa-Core CPU, Mali-G68 MP5 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, description) VALUES (?, ?, ?, ?, ?)", ("Samsung",'Samsung Galaxy A15', 749, "s15.png", "Colour: Blue, Black, Yellow, Capacity: 128GB, 256GB, Size:160.1 x 76.8 x 8.4 mm,  200 g, 6.5 inches Super AMOLED display,CPU: Octa-Core CPU, Mali-G57 MC2 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, description) VALUES (?, ?, ?, ?, ?)", ("Samsung",'Samsung Galaxy S23 FE', 2999, "ss23.png", "Colour:Mint, Cream, Purple, Graphite, Capacity: 128GB, 256GB, Size:158 x 76.5 x 8.2 mm,209 g, 6.4 inches Dynamic AMOLED 2X  display,CPU: Octa-Core CPU, Xclipse 920 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, description) VALUES (?, ?, ?, ?, ?)", ("Honor",'Honor X9 5G', 1299, "hx9.png","Colour: Black, Silver, Blue,Capacity: 128GB,Size:166.1 x 75.8 x 8.1 mm, 6.81 inches IPS LCD Display,CPU: Octa-Core CPU, Adreno 619 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, description) VALUES (?, ?, ?, ?, ?)", ("Honor",'Honor Play7T Pro ', 999, "h7T.png","Colour: Black, Dark Green, Silver,Capacity: 128GB,Size:162.9 x 74.5 x 7.4 mm, 175 g, 6.7 inches IPS LCD Display,CPU: Octa-Core CPU, Mali-G57 MC2 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, description) VALUES (?, ?, ?, ?, ?)", ("Honor",'HONOR 400 Pro', 2699, "h400.png","Colour: Desert Gold, Tidal Blue, Midnight Black,Capacity: 512GB,Size:160.8  x  76.1  x  8.1 mm, 205 g, 6.7 inches AMOLED display,CPU: Octa-Core CPU, Adreno 750 GPU"))

try:
    cursor.execute("ALTER TABLE phones ADD COLUMN screen_size TEXT NOT NULL DEFAULT 'unknown'")
except sqlite3.OperationalError:
    print("Column 'screen_size' already exists")

try:
    cursor.execute("ALTER TABLE phones ADD COLUMN sim TEXT NOT NULL DEFAULT 'unknown'")
except sqlite3.OperationalError:
    print("Column 'sim' already exists")

conn.commit()
conn.close()

print("Database initialized and sample data added.")