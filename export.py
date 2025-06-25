import sqlite3
import csv

def export_to_csv():
    with sqlite3.connect("forum.db") as conn:
        posts = conn.execute("SELECT * FROM posts").fetchall()
        with open('forum_export.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Title', 'Content', 'Timestamp'])
            writer.writerows(posts)

export_to_csv()

