import telebot
import json
import warnings
import urllib
import time
import os
import requests

bot = telebot.TeleBot("5040031474:AAEYMlFvTE54deHlDGvWRIEOUKoK8XeY23o")

@bot.message_handler(commands=['start'])
def hello(message):
        bot.send_message(message.chat.id,
                         "Добрый день!")

@bot.message_handler(commands=['help'])
def hello(message):
        bot.send_message(message.chat.id,
                         "Список всех команд")

@bot.message_handler(commands=['article'])
def hello(message):
        bot.send_message(message.chat.id,
                         "Артикул")

@bot.message_handler(commands=['newexcel'])
def hello(message):
        bot.send_message(message.chat.id,
                         "Присоединить новую ексель табличку")

@bot.message_handler(commands=['codeword'])
def hello(message):
        bot.send_message(message.chat.id,
                         "Ключ для выкупа")

@bot.message_handler(commands=['buy'])
def hello(message):
        bot.send_message(message.chat.id,
                         "Выкупаем")


bot.polling(none_stop=True)
