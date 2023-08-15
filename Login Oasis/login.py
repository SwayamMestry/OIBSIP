from flask import Flask, render_template, request, redirect, session, flash
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.secret_key = '721228'
users = {}

def hash_password(password):
    return pbkdf2_sha256.hash(password)

def verify_password(password, hashed_password):
    return pbkdf2_sha256.verify(password, hashed_password)

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and verify_password(password, users[username]):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Login failed. Invalid credentials.', 'error')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists.', 'error')
        else:
            users[username] = hash_password(password)
            flash('Registration successful!', 'success')

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)