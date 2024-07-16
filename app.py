from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    cursor.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", ('testuser', hashlib.md5('password123'.encode()).hexdigest()))
    conn.commit()
    conn.close()

init_sqlite_db()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE username=? AND password=?", (username, hashed_password))
        account = cursor.fetchone()
        conn.close()
        
        if account:
            session['loggedin'] = True
            session['username'] = account[1]
            return redirect(url_for('home'))
        else:
            return 'Incorrect username/password!'
    
    return render_template('login.html')

@app.route('/home')
def home():
    if 'loggedin' in session:
        return f'Hello, {session["username"]}! You are logged in.'
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
