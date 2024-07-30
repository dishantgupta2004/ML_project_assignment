from flask import Flask, render_template, redirect, url_for, request, flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config.from_object('config.Config')


mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = {
            'username': form.username.data,
            'email': form.email.data,
            'password': hashed_password
        }
        mongo.db.users.insert_one(user)
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.users.find_one({'email': form.email.data})
        if user and bcrypt.check_password_hash(user['password'], form.password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/home')
def home():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)
