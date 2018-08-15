# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request

from flask_mail import Mail, Message

from databases import add_donate, get_all_donates_by_type, search_donate


# Add functions you need from databases.py to the next line!
# from databases import add_student, get_all_students

# Starting the flask app
app = Flask(__name__)
mail=Mail(app)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME":'websitedonate1@gmail.com',
    "MAIL_PASSWORD": 'xzaq1234'
}

app.config.update(mail_settings)

mail=Mail(app)
# App routing code here
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/money')
def money():
    money=get_all_donates_by_type("money")
    return render_template('money.html' , money=money)

@app.route('/food')
def food():
    food=get_all_donates_by_type("food")
    return render_template('food.html' , food=food)

@app.route('/about_us')
def aboutus():
    return render_template('about_us.html')

@app.route('/essentials')
def essentials():
    essentials=get_all_donates_by_type("essentials")
    return render_template('essentials.html' , essentials=essentials)

@app.route('/search', methods=['POST'])
def search():
	results=search_donate(request.form["Search_text"])
	print(results)
	return render_template("search.html",results=results)

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
        needs=request.form.getlist('donations')
        print("Needs: ",needs)
        phone_num=request.form['phone_number']
        link=request.form['link']
        pic=request.form['pic']
        msg = Message("Hello" + name,
                  sender="websitedonate1@gmail.com",
                  recipients=[email])
        msg.body = "name: "+str(name) + "\n adress: "+ str(address) + "\nstory: "+str(story)+ "\nneeder type: "+str(needer_type) +"\n needs: " + str(needs) + "\nphone: "+str(phone_num) + "\nlink: "+str(link)+"\npic: "+str(pic)+"\n thank you for joining us! good luck!" 
        mail.send(msg)
        add_donate(name, story, email, needer_type, "|".join(needs), phone_num, address, link, pic)
        print("hi 4")
        return render_template('check.html',
               n=name,
               s=story,
               e=email, nt=needer_type, ne=needs, p=phone_num, a=address, l=link, pic=pic)
 

if __name__ == "__main__":
    app.run(debug=True)
