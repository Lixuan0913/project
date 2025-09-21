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
    phones = cursor.fetchall()
    conn.close()

    return render_template("home.html", phones=phones)

if __name__ == "__main__":
    app.run(debug=True)

