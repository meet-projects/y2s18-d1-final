# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_student, get_all_students

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/money')
def money():
    return render_template('money.html')
    
    # Running the Flask app
@app.route('/essentials')
def essentials():
	return render_template("essentials.html")
@app.route('/food')
def food():
    return render_template('food.html')
@app.route('/about_us')
def aboutus():
    return render_template('about_us.html')
@app.route('/contact_us')
def contact():
    return render_template('contact_us.html')
if __name__ == "__main__":
    app.run(debug=True)
