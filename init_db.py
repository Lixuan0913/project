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
        storage TEXT NOT NULL,
        description TEXT NOT NULL
    )
""")

cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("iPhone",'iPhone 15', 2699, "i15.png","128GB, 256GB, 512GB", "Colour: Black, Silver, Blue,Size:147.6 mm x 71.6 mm x 7.80 mm,173g, 6.1‑inch (diagonal) all‑screen OLED display, CPU: Octa-Core CPU, Adreno 619 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("iPhone",'iPhone 14', 2299, "i14.png",'128GB, 256GB, 512GB', "Colour: Starlight, Purple,Blue, Midnight, Yellow,Size:146.7 mm x 71.5 mm x 7.80 mm, 172g, 6.1‑inch (diagonal) all‑screen OLED display,CPU: 6‑core CPU with 2 performance and 4 efficiency cores, 5-core GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("iPhone",'iPhone 13', 1999, "i13.png", "128GB, 256GB, 512GB" ,"Colour: Starlight, Midnight,Blue, Pink, Green, Size:146.7 mm x 71.5 mm x 7.65 mm,173g, 6.1‑inch (diagonal) all‑screen OLED display,CPU: 6‑core CPU with 2 performance and 4 efficiency cores, 4-core GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Samsung",'Samsung Galaxy A35', 1399, "s35.png", "128GB, 256GB" ,"Colour: Iceblue, Lilac, Navy,Lemon, Size:161.7 x 78 x 8.2 mm, 209 g, 6.6 inches Super AMOLED display,CPU: Octa-Core CPU, Mali-G68 MP5 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Samsung",'Samsung Galaxy A15', 749, "s15.png", "128GB, 256GB", "Colour: Blue, Black, Yellow, Size:160.1 x 76.8 x 8.4 mm,  200 g, 6.5 inches Super AMOLED display,CPU: Octa-Core CPU, Mali-G57 MC2 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Samsung",'Samsung Galaxy S23 FE', 2999, "ss23.png", "128GB, 256GB", "Colour:Mint, Cream, Purple, Graphite, Size:158 x 76.5 x 8.2 mm,209 g, 6.4 inches Dynamic AMOLED 2X  display,CPU: Octa-Core CPU, Xclipse 920 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Honor",'Honor X9 5G', 1299, "hx9.png", "128GB", "Colour: Black, Silver, Blue, Size:166.1 x 75.8 x 8.1 mm, 6.81 inches IPS LCD Display,CPU: Octa-Core CPU, Adreno 619 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Honor",'Honor Play7T Pro ', 999, "h7T.png", "128GB" , "Colour: Black, Dark Green, Silver, Size:162.9 x 74.5 x 7.4 mm, 175 g, 6.7 inches IPS LCD Display,CPU: Octa-Core CPU, Mali-G57 MC2 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Honor",'HONOR 400 Pro', 2699, "h400.png", "512GB", "Colour: Desert Gold, Tidal Blue, Midnight Black, Size:160.8  x  76.1  x  8.1 mm, 205 g, 6.7 inches AMOLED display,CPU: Octa-Core CPU, Adreno 750 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Vivo",'Vivo iQOO Z7x', 999, "vz7x.png", "128GB, 256GB" ,"Colour: Black, Blue, Size:164.6 x 75.8 x 9.1 mm, 205 g, 6.64 inches IPS LCD display, Octa-Core CPU, Adreno 619 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Vivo",'vivo V27', 1799, "vv27.png", "256GB", "Colour: Noble Black, Emerald Green, Flowing Gold, Magic Blue ,Size:164.1 x 74.8 x 7.4 mm, 180 g, 6.78 inches AMOLED display,CPU: Octa-Core CPU, Mali-G610 MC4 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Vivo",'vivo X70', 2499, "vx70.png", "128GB, 256GB", "Cosmic Black,Aurora Dawn,White ,Size:160.1 x 75.4 x 7.6 mm, 182 g, 6.56 inches AMOLED display,CPU: Octa-Core CPU, Mali-G77 MC9 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Realme",'Realme 10', 999, "r10.png", "256GB", "Colour: Black,White ,Size:159.9 x 73.3 x 8 mm, 178 g, 6.4 inches Super AMOLED display, CPU: Octa-Core CPU, Mali-G57 MC2 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Realme",'Realme 11 Pro+', 1999, "r11pro.png", "512GB", "Colour: Oasis Green, Sunrise Beige, Astral Black ,Size:161.7 x 73.9 x 8.2 mm,  183 g, 6.7 inches AMOLED display, CPU: Octa-Core CPU, Mali-G68 MC4 GPU"))
cursor.execute("INSERT INTO phones (brand,model_name, price, image_filename, storage, description) VALUES (?, ?, ?, ?, ?, ?)", ("Realme",'Realme GT 2 Pro', 2999, "r2pro.png", "256GB", "Colour: Paper White, Paper Green, Steel Black ,Size:163.2 x 74.7 x 8.2 mm, 199 g, 6.7 inches LTPO2 AMOLED display, CPU: Octa-Core CPU, Adreno 730 GPU"))

conn.commit()
conn.close()

print("Database initialized and sample data added.")