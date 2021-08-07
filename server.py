from flask import Flask, render_template, request, redirect
from flask.globals import session

app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session['total'] = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple']) + int(request.form['blackberry'])
    print(f"Charging {request.form['first_name']} for {session['total']} fruits")
    return render_template("checkout.html", info=request.form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)