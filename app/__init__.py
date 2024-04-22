from flask import Flask, redirect, render_template, url_for
from config import Config
from formclass import LoginForm
from flask import flash


app = Flask(__name__)
app.config.from_object(Config)
#We've created a seperate "config.py" file for our config,
#and we simply import it here and use the from_object() method
#to use it here. This is to help keep the main app file less cluttered.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createticket')
def createticket():
    return render_template('createticket.html')

@app.route('/viewticket')
def viewticket():
    return render_template('viewticket.html')

@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
    

if __name__ == '__main__':
    app.run(debug=True)

# So far we've gotten our routes and html templates mostly set up. Soon we'll finish that and get to adding 
#database functionality, forms functionality, and Bootstrap5 styling. 
