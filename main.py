from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('phones.db')  # Connect to the database file
    conn.row_factory = sqlite3.Row  # This allows you to access columns by name
    return conn

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get the user-selected brand and price from the form
        brand_name = request.form.get("brand")
        price = request.form.get('price')
        
        # Connect to the SQLite database
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Query the database based on brand and price
        cursor.execute("SELECT * FROM phones WHERE brand = ? AND price = ?", (brand_name, price))
        phones = cursor.fetchall()  # Get all the matching rows
        
        # Close the connection to the database
        conn.close()
        
        # Return the results to the template
        return render_template("home.html", phones=phones)

    # If it's a GET request, display all phones
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phones")  # Get all phones
    phones = cursor.fetchall()  # Fetch all the rows
    conn.close()

    return render_template("home.html", phones=phones)

if __name__ == "__main__":
    app.run(debug=True)