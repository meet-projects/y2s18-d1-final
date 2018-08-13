from flask import Flask, render_template
app = Flask(__name__)

@app.route('/essentialslist')
def essen():
    essentials = []
    return render_template("essentialsls_loop.html",
    	essentials=essentials)

@app.route('/moneylist')
def mon():
    money = []
    return render_template("money_loop.html",
    	money=money)







if __name__ == '__main__':
   app.run(debug = True)