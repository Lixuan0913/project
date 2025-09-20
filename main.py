from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('phones.db')
    conn.row_factory = sqlite3.Row  
    return conn

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        brand_name = request.form.get("brand")
        price = request.form.get('price')
        screen_size = request.form.get('screen_size')
        sim = request.form.get('sim')

        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM phones WHERE brand = ?, screen_size = ?, sim = ? AND price = ?", (brand_name, screen_size, sim, price))
        phones = cursor.fetchall() 
        
        conn.close()

        return render_template("home.html", phones=phones)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phones") 
    phones = cursor.fetchall()  
    conn.close()

    return render_template("home.html", phones=phones)

if __name__ == "__main__":
    app.run(debug=True)