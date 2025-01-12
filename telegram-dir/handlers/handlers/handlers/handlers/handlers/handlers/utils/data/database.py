import sqlite3

DATABASE_NAME = "alerts.db"

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            price REAL NOT NULL,
            condition TEXT NOT NULL,
            user_id INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_alert(symbol, price, condition,user_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO alerts (symbol, price, condition, user_id)
        VALUES (?, ?, ?, ?)
    """, (symbol, price, condition,user_id))
    conn.commit()
    conn.close()
def remove_alert(alert_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alerts WHERE id = ?", (alert_id,))
    conn.commit()
    conn.close()


def get_alerts():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts")
    alerts = cursor.fetchall()
    conn.close()
    return alerts


create_table()