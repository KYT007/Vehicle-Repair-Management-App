from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createticket')
def createticket():
    return render_template('createticket.html')

@app.route('/viewticket')
def viewticket():
    return render_template('viewticket.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

# So far we've gotten our routes and html templates mostly set up. Soon we'll finish that and get to adding 
#database functionality, forms functionality, and Bootstrap5 styling. 
