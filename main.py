import sqlite3

import telebot
from telebot import types
import random

from settings import TOKEN # Удалить после добавления токена

conn = sqlite3.connect('mydata.db')
cursor1 = conn.cursor()
cursor2 = conn.cursor()

# TOKEN = 'Добавить ваш токен сюда'

URL = 'https://api.telegram.org/bot'

bot = telebot.TeleBot(TOKEN)

class BotService:

    @staticmethod
    def start_message(chat_id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Анекдот")
        btn2 = types.KeyboardButton("Мемчик")
        markup.add(btn1, btn2)
        bot.send_message(chat_id, "Привет! Я Joke Bot! Пришлю тебе анекдот или смешной мем. Жми на кнопку!",
                         reply_markup=markup)


cursor1.execute("SELECT image FROM memos")
cursor2.execute("SELECT jokes FROM texts")
images = cursor1.fetchall()
texts = cursor2.fetchall()


class BotMessageSender:

    @classmethod
    def bot_message(cls, message):

        if message.text == 'Анекдот':
            text = random.choice(texts)
            bot.reply_to(message, text)

        elif message.text == 'Мемчик':
            image = random.choice(images)
            cls.send_photo(message, path=image[0])

        else:
            bot.send_message(message.chat.id, "Нифига не понятно, но очень интересно")

    @staticmethod
    def send_photo(message, path: str):
        with open(path, 'rb') as photo:
            bot.send_photo(message.from_user.id, photo)


@bot.message_handler(commands=['start'])
def command_hello(message):
    BotService.start_message(chat_id=message.chat.id)


@bot.message_handler(content_types='text')
def button_message(message):
    BotMessageSender.bot_message(message=message)


bot.infinity_polling()
