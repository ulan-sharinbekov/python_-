from telebot import *
import requests


TOKEN = "1883154030:AAGF21aoXyK3TYzLvlrRrOqxKUG6rObEG2U"

bot = TeleBot(TOKEN)

KEY = '186a2ae6b4e4a7465105495e3430df15'
URL = 'https://api.openweathermap.org/data/2.5/weather'
# params = {
#     'q': city,
#     'appid': KEY,
#     'units': 'metric',
# }

@bot.message_handler(commands=['start'])
def greeting(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(content_types=['text'])
def handler(message):
    city = message.text.capitalize()
    params = {
        'q': city,
        'appid': KEY,
        'units': 'metric'
    }
    data = requests.get(URL,params)
    data = data.json()
    print(data)
    temp = data['main']['temp']
    bot.send_message(message.chat.id, temp)

bot.polling()