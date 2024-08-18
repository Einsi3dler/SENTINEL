#!/usr/bin/python3
# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from functools import wraps
import MySQLdb.cursors
import re
from werkzeug.security import check_password_hash
import sys
import os

current_script_directory = os.path.dirname(__file__)

# Calculate the path to the project root directory by navigating up three levels
project_root_path = os.path.abspath(os.path.join(current_script_directory, '../../'))

# Add the project root directory to the beginning of sys.path
sys.path.insert(0, project_root_path)


from console import SentinelCommand


app = Flask(__name__)


app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sentinel_dev'
app.config['MYSQL_PASSWORD'] = 'sentinel_dev_pwd'
app.config['MYSQL_DB'] = 'sentinel_prod_db'

mysql = MySQL(app)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/dashboard')
@login_required
def dashboard():
     return render_template('index.html')

@app.route('/')
def home():
	return render_template('landing.html')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'user-email' in request.form and 'password' in request.form:
        email = request.form['user-email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT id, email, password FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account and check_password_hash(account['password'], password):
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['email']
            print("Login successful, redirecting...")
            return redirect(url_for('dashboard'))  # Redirect to a dashboard or similar page
        else:
            msg = 'Incorrect email or password!'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('landing'))


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
            argument = f'User first_name={first_name} last_name="{last_name}" email="{email}" phone_number="{phone_number}" password="{password}"'
            command_instance = SentinelCommand()
            command_instance.do_create(argument)
            ##cursor.execute('INSERT INTO users (first_name, last_name, email, phone_number, password) VALUES (%s, %s, %s, %s, %s)', (first_name, last_name, email, phone_number, password_hash))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            return render_template('login.html', msg=msg)
    return render_template('signUp.html', msg=msg)



if __name__ == '__main__':
	app.run()