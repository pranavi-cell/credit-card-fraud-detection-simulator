import sqlite3

def create_database():

    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_number TEXT,
        amount REAL,
        location TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_transaction(card, amount, location, time):

    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions(card_number, amount, location, time)
    VALUES (?, ?, ?, ?)
    """,(card, amount, location, time))

    conn.commit()
    conn.close()