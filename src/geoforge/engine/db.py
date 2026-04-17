import sqlite3
from datetime import datetime

conn = sqlite3.connect("geoforge.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    analysis TEXT
)
""")


def save_result(data):
    cursor.execute(
        "INSERT INTO results (timestamp, analysis) VALUES (?, ?)",
        (str(datetime.now()), str(data))
    )
    conn.commit()


def fetch_results():
    cursor.execute("SELECT * FROM results")
    return cursor.fetchall()