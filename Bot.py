import telebot
import sqlite3
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


conn = sqlite3.connect("db/users.db", check_same_thread=False)
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    user_id INTEGER, 
                    name TEXT)''')
conn.commit()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Напишите свое имя для регистрации.")

@bot.message_handler(content_types=['text'])
def register_user(message):
    user_id = message.chat.id
    name = message.text.strip()

    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users (user_id, name) VALUES (?, ?)", (user_id, name))
        conn.commit()
        bot.send_message(message.chat.id, f"✅ Вы успешно зарегистрированы как {name}!")
    else:
        bot.send_message(message.chat.id, "⚠️ Вы уже зарегистрированы!")

@bot.message_handler(commands=['users'])
def list_users(message):
    admin_id = 123456789
    if message.chat.id == admin_id:
        cursor.execute("SELECT name, user_id FROM users")
        users = cursor.fetchall()
        if users:
            user_list = "\n".join([f"👤 {user[0]} (ID: {user[1]})" for user in users])
            bot.send_message(message.chat.id, f"📋 Список пользователей:\n{user_list}")
        else:
            bot.send_message(message.chat.id, "⚠️ В базе нет зарегистрированных пользователей.")
    else:
        bot.send_message(message.chat.id, "⛔ У вас нет доступа!")

bot.polling(none_stop=True)