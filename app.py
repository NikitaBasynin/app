from flask import Flask, request, render_template_string, redirect
import sqlite3
import os

app = Flask(__name__)

# Хардкод пароля (уязвимость)
ADMIN_PASSWORD = "admin123"
AWS_SECRET_ACCESS_KEY = "AKIA1234567890FAKEKEY"


# Создание БД при первом запуске
def init_db():
    if not os.path.exists('users.db'):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
            )
        ''')
        conn.commit()
        conn.close()

init_db()

@app.route('/')
def home():
    return render_template_string('''
        <h2>Login</h2>
        <form method="POST" action="/login">
            Username: <input name="username"><br>
            Password: <input name="password"><br>
            <input type="submit" value="Login">
        </form>
        <br>
        <a href="/register">Register new user</a>
    ''')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Уязвимость: отсутствие валидации, возможна SQL-инъекция
        query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template_string('''
        <h2>Register</h2>
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password"><br>
            <input type="submit" value="Register">
        </form>
        <br>
        <a href="/">Back to login</a>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # SQL-инъекция (уязвимость)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    result = cursor.execute(query).fetchone()
    conn.close()

    if result:
        return f"Welcome, {username}!"
    else:
        return "Invalid credentials"

@app.route('/message')
def message():
    msg = request.args.get("msg", "")
    return f"<p>You said: {msg}</p>"  # XSS уязвимость

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
