from flask import Flask, render_template, redirect, request


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
   if request.method  == "POST":
      brand_name = request.form.get("brand")
      price = request.form.get('price')
      
      print(brand_name)
   return render_template("home.html")

if __name__ == "__main__":
   app.run(debug=True)