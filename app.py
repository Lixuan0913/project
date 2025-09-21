from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('phones.db')  
    conn.row_factory = sqlite3.Row  
    return conn

@app.route("/", methods=["GET", "POST"])
def home():
    brand_name = request.form.get("brand", "")
    price = request.form.get('price', "")
    screen_size = request.form.get('screen_size', "")
    sim = request.form.get('sim', "")

    query = "SELECT * FROM phones WHERE 1=1"
    params = []

    if brand_name:
        query += " AND brand = ?"
        params.append(brand_name)
    else:
        query += "" 

    if price:
        query += " AND price = ?"
        params.append(price)
    else:
        query += "" 

    if screen_size:
        query += " AND screen_size = ?"
        params.append(screen_size)
    else:
        query += "" 

    if sim:
        query += " AND sim = ?"
        params.append(sim)
    else:
        query += ""  

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    #for the phone cards
    phones = []
    for row in rows:
        phones.append({
            "id": row[0],
            "brand": row[1],
            "price": row[2],
            "image_filename": row[3],
            "screen_size": row[4],
            "sim": row[5] 
        })

    return render_template("home.html", phones=phones)

@app.route("/phone/<int:phone_id>")
def phone_descriptions(phone_id):
    conn = sqlite3.connect('phones.db')  
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM phones WHERE id = ?", (phone_id,))
    phone_data = cursor.fetchone()
    conn.close()
    
    if not phone_data:
        return "Sorry, the phone you're looking for doesn't exist or may have been removed."
    
    return render_template("phone_descriptions.html", phone=phone_data)

if __name__ == "__main__":
    app.run(debug=True)

