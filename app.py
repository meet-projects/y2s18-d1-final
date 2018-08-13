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
    return render_template('money.html')
    money=session.query(
       Donate).filter_by(
       needs=money).all()

@app.route('/food')
def food():
    return render_template('food.html')
    food=session.query(
       Donate).filter_by(
       needs=food).all()

@app.route('/about_us')
def aboutus():
    return render_template('about_us.html')

@app.route('/essentials')
def essentials():
    return render_template('essentials.html') 
    essentials =session.query(
       Donate).filter_by(
       needs=essentials).all()  

@app.route('/contact_us')
def contact():
    return render_template('contact_us.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    print("hi")
    if request.method == 'GET':
           return render_template('add.html')
    else:
<<<<<<< HEAD

       name = request.form['firstname']
       address = request.form['address']
       story=request.form['backround']
       email=request.form['email']
       needer_type=request.form['needer_type']
       needs=request.form['donations']
       phone_num=request.form['phone_number']
       link=request.form['link']


       save_to_database(name, animal) 
=======
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
 

>>>>>>> 3a75e80c0df2587185afefbd4b52d3e4f0094b18
if __name__ == "__main__":
    app.run(debug=True)
