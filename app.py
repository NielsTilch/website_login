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

    conn.close()

def print_accounts_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    conn.close()
    
    print("Accounts Table:")
    for account in accounts:
        print(f"ID: {account[0]}, Username: {account[1]}, Password: {account[2]}")
    print("End of Accounts Table\n")

init_sqlite_db()
print_accounts_table()

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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        print_accounts_table()  # Print the table after a new signup
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/home')
def home():
    if 'loggedin' in session:
        return f'Hello, {session["username"]}! You are logged in. <br><a href="/accounts">View all accounts</a>'
    return redirect(url_for('login'))

@app.route('/accounts')
def accounts():
    #if 'loggedin' in session:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts")
        accounts = cursor.fetchall()
        conn.close()
        return render_template('accounts.html', accounts=accounts)
    #return redirect(url_for('login'))

@app.route('/print_accounts')
def print_accounts():
    print_accounts_table()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
