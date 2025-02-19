import telebot
from telebot import types
from token_1 import my_token
token = my_token
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Введи выражение для вычисления, например: 2 + 2")
@bot.message_handler(func=lambda message: True)

def calc(message):
    try:
        bot.send_message(message.chat.id, f'Результат: {eval(message.text)}')
    except:
        bot.send_message(message.chat.id, f'били?')

bot.infinity_polling()
