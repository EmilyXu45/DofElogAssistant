import sqlite3

DB_NAME = "dofe_logs.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        week INTEGER,
        activity TEXT,
        skills TEXT,
        challenges TEXT,
        reflection TEXT,
        date TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_log(week, activity, skills, challenges, reflection):
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
    INSERT INTO logs (week, activity, skills, challenges, reflection, date)
    VALUES (?, ?, ?, ?, ?, DATE('now'))
    """, (week, activity, skills, challenges, reflection))
    conn.commit()
    conn.close()

def get_logs():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY week")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_log(log_id):
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM logs WHERE id = ?",
        (log_id,)
    )

    conn.commit()
    conn.close()
