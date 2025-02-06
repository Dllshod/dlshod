import os
import sqlite3


def init_db():
    if not os.path.exists("db"):
        os.makedirs("db")

    conn = sqlite3.connect("db/users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        user_id INTEGER, 
                        name TEXT, 
                        phone TEXT)''')
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()