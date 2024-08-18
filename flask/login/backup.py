#!/usr/bin/python3
# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from werkzeug.security import generate_password_hash

app = Flask(__name__)


app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sentinel_dev'
app.config['MYSQL_PASSWORD'] = 'sentinel_dev_pwd'
app.config['MYSQL_DB'] = 'sentinel_prod_db'

mysql = MySQL(app)

@app.route('/')
def home():
	return render_template('landing.html')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'user-email' in request.form and 'password' in request.form:
        email = request.form['user-email']  # Changed from 'username' to 'user-email'
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['email']
            msg = f"Logged in successfully! {session['id']}"
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        email = request.form.get('user-email')
        phone_number = request.form.get('phone-number')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        terms = request.form.get('terms-and-condition', False)

        # Database cursor setup here, ensure you have mysql setup
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()

        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif password != confirm_password:
            msg = 'Passwords do not match!'
        elif not terms:
            msg = 'Please accept the terms and conditions to proceed!'
        elif not (first_name and last_name and email and phone_number and password):
            msg = 'Please fill out the form completely!'
        else:
            # Encrypt the password before storing it
            password_hash = generate_password_hash(password)
            cursor.execute('INSERT INTO users (first_name, last_name, email, phone_number, password) VALUES (%s, %s, %s, %s, %s)', 
                           (first_name, last_name, email, phone_number, password_hash))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    return render_template('signUp.html', msg=msg)



if __name__ == '__main__':
	app.run()