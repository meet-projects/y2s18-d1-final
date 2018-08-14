# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session
from databases import add_donate

# Add functions you need from databases.py to the next line!
# from databases import add_student, get_all_students

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/money')
def money():
    
    money=session.query(
       Donate).filter_by(
       needs=money).all()
    return render_template('money.html')
@app.route('/food')
def food():
    
    food=session.query(
       Donate).filter_by(
       needs=food).all()
    return render_template('food.html')
@app.route('/about_us')
def aboutus():
    return render_template('about_us.html')

@app.route('/essentials')
def essentials():
    
    essentials =session.query(
       Donate).filter_by(
       needs=essentials).all()  
    return render_template('essentials.html') 
@app.route('/contact_us')
def contact():
    return render_template('contact_us.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    print("hi")
    if request.method == 'GET':
           return render_template('add.html')
    else:

        print("hi2")
        name = request.form['name']
        address = request.form['address']
        story=request.form['backround']
        email=request.form['email']
        print("hi3")
        needer_type=request.form['needer_type']
        needs=request.form['donations']
        phone_num=request.form['phone_number']
        link=request.form['link']
        pic=request.form['pic']

        add_donate(name, story, email, needer_type, needs, phone_num, address, link, pic)
        print("hi 4")
        return render_template('check.html',
               n=name,
               s=story,
               e=email, nt=needer_type, ne=needs, p=phone_num, a=address, l=link, pic=pic)
 

if __name__ == "__main__":
    app.run(debug=True)
