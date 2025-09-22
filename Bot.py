import os
import telebot
from flask import Flask, request

bot = telebot.TeleBot(os.environ['8419639724:AAHaSv73O-VAancVmgfDP4r3ErUrlpMIxKc'])
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает на Render! 🚀")

@app.route("/")
def home():
    return "Бот жив! ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    return 'Error', 403

if __name__ == '__main__':
    print("Запуск бота...")
    bot.remove_webhook()
    # Этот URL поменяем после создания на Render
    bot.set_webhook(url="https://your-bot-name.onrender.com/webhook")
    app.run(host='0.0.0.0', port=5000)
