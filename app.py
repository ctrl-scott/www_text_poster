from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize DB
def init_db():
    with sqlite3.connect("forum.db") as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
init_db()

@app.route('/')
def index():
    with sqlite3.connect("forum.db") as conn:
        posts = conn.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sqlite3.connect("forum.db") as conn:
            conn.execute("INSERT INTO posts (title, content, timestamp) VALUES (?, ?, ?)", (title, content, timestamp))
        return redirect('/')
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

