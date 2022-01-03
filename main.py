import telebot
import json
import warnings
import urllib
import time
import os

bot = telebot.TeleBot("5040031474:AAEYMlFvTE54deHlDGvWRIEOUKoK8XeY23o")

@bot.message_handler(commands=['start'])
def hello(message):
        bot.send_message(message.chat.id,
                         "Добрый день!")

bot.polling(none_stop=True)