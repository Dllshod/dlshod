import sqlite3

class Database:
    def __init__(self, db_path="users.db"):
        """Подключение к базе и создание таблицы, если ее нет"""
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Создание таблицы пользователей"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT,
                latitude REAL,
                longitude REAL
            )
        """)
        self.conn.commit()

    def add_user(self, user_id, name):
        """Добавляет нового пользователя"""
        self.cursor.execute("INSERT INTO users (user_id, name) VALUES (?, ?)", (user_id, name))
        self.conn.commit()

    def update_phone(self, user_id, phone):
        """Обновляет номер телефона"""
        self.cursor.execute("UPDATE users SET phone=? WHERE user_id=?", (phone, user_id))
        self.conn.commit()

    def update_location(self, user_id, latitude, longitude):
        """Обновляет геолокацию"""
        self.cursor.execute("UPDATE users SET latitude=?, longitude=? WHERE user_id=?", (latitude, longitude, user_id))
        self.conn.commit()

    def get_user(self, user_id):
        """Получает данные пользователя"""
        self.cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        return self.cursor.fetchone()

    def close(self):
        """Закрывает соединение с базой"""
        self.conn.close()