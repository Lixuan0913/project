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
    storage = request.form.get('storage', "")

    query = "SELECT * FROM phones WHERE 1=1"
    params = []

    if brand_name:
        query += " AND brand = ?"
        params.append(brand_name)
    else:
        query += "" 

    if price:
        query += " AND price <= ?"
        params.append(price)
    else:
        query += "" 

    if storage:
        query += " AND storage LIKE ?"
        params.append(f"%{storage}%")
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
            "model_name": row[2],
            "price": row[3],
            "image_filename": row[4],
            "storage": row[5],
            "description": row[6]
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
    
    phone = {
        "id": phone_data[0],
        "brand": phone_data[1],
        "model_name": phone_data[2],
        "price": phone_data[3],
        "image_filename": phone_data[4],
        "storage":phone_data[5],
        "description": phone_data[6]
    }
    
    
    return render_template("phone_descriptions.html", phone=phone)

if __name__ == "__main__":
    app.run(debug=True)

