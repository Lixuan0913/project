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
        size = request.form.get('size')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM phones WHERE brand = ?, size = ? AND price = ?", (brand_name, size, price))
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