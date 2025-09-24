from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Important for sessions

def get_db_connection():
    conn = sqlite3.connect('phones.db')  
    conn.row_factory = sqlite3.Row  
    return conn

@app.route("/", methods=["GET", "POST"])
def home():
    # Handle filter form
    brand_name = request.form.get("brand", "")
    price = request.form.get('price', "")
    storage = request.form.get('storage', "")
    
    # Handle quiz form
    if request.method == "POST" and "quiz_question" in request.form:
        quiz_question = request.form.get("quiz_question")
        quiz_answer = request.form.get("quiz_answer")
        
        # Initialize quiz session if not exists
        if 'quiz_answers' not in session:
            session['quiz_answers'] = {}
        
        # Store the answer
        session['quiz_answers'][quiz_question] = quiz_answer
        session.modified = True  # Important: Mark session as modified
        
        # If this was the last question, process the results
        if quiz_question == "5":
            return redirect(url_for('quiz_results'))
        else:
            # Redirect to avoid form resubmission issues
            return redirect(url_for('home'))
    
    # Build query for phone filtering (only if not a quiz submission)
    query = "SELECT * FROM phones WHERE 1=1"
    params = []

    if brand_name and "quiz_question" not in request.form:
        query += " AND brand = ?"
        params.append(brand_name)

    if price and "quiz_question" not in request.form:
        query += " AND price <= ?"
        params.append(price)

    if storage and "quiz_question" not in request.form:
        query += " AND storage LIKE ?"
        params.append(f"%{storage}%")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    # For the phone cards
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

    # Determine current quiz question - FIXED LOGIC
    current_question = 1
    if 'quiz_answers' in session:
        answered_questions = len(session['quiz_answers'])
        current_question = answered_questions + 1
        if current_question > 5:
            current_question = 1  # Reset or show completion

    return render_template("home.html", phones=phones, current_question=current_question)

@app.route("/quiz-results")
def quiz_results():
    if 'quiz_answers' not in session or not session['quiz_answers']:
        return redirect(url_for('home'))
    
    # Process quiz answers to determine preferences
    answers = session['quiz_answers']
    
    # Build query based on quiz answers
    query = "SELECT * FROM phones WHERE 1=1"
    params = []
    
    # Question 1: Budget preference
    if answers.get('1') == 'budget':
        query += " AND price <= 1000"
    elif answers.get('1') == 'midrange':
        query += " AND price > 1000 AND price <= 2000"
    elif answers.get('1') == 'premium':
        query += " AND price > 2000"
    
    # Question 2: Brand preference
    brand_map = {
        'apple': 'iPhone',
        'samsung': 'Samsung',
        'honor': 'Honor',
        'vivo': 'Vivo',
        'realme': 'Realme'
    }
    if answers.get('2') in brand_map:
        query += " AND brand = ?"
        params.append(brand_map[answers.get('2')])
    
    # Question 3: Storage preference
    if answers.get('3') == 'low':
        query += " AND storage LIKE ?"
        params.append('%128GB%')
    elif answers.get('3') == 'medium':
        query += " AND (storage LIKE ? OR storage LIKE ?)"
        params.append('%256GB%')
        params.append('%128GB%')
    elif answers.get('3') == 'high':
        query += " AND storage LIKE ?"
        params.append('%512GB%')
    
    # Question 4: Usage preference
    if answers.get('4') == 'basic':
        query += " AND price <= 1500"  # Basic usage = budget phones
    elif answers.get('4') == 'gaming':
        query += " AND description LIKE ?"
        params.append('%GPU%')  # Look for phones with GPU mentioned
    
    # Question 5: Priority
    if answers.get('5') == 'performance':
        query += " ORDER BY price DESC"  # Higher price often correlates with better performance
    elif answers.get('5') == 'value':
        query += " ORDER BY price ASC"  # Lower price for better value
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    recommended_phones = []
    for row in rows:
        recommended_phones.append({
            "id": row[0],
            "brand": row[1],
            "model_name": row[2],
            "price": row[3],
            "image_filename": row[4],
            "storage": row[5],
            "description": row[6]
        })
    
    # Clear quiz answers after showing results
    session.pop('quiz_answers', None)
    
    return render_template("quiz_results.html", phones=recommended_phones, answers=answers)

@app.route("/reset-quiz")
def reset_quiz():
    session.pop('quiz_answers', None)
    return redirect(url_for('home'))

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
        "storage": phone_data[5],
        "description": phone_data[6]
    }
    
    return render_template("phone_descriptions.html", phone=phone)

if __name__ == "__main__":
    app.run(debug=True)