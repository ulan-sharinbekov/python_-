from telebot import *
import time, random
from gtts import *
TOKEN = "1883154030:AAGF21aoXyK3TYzLvlrRrOqxKUG6rObEG2U"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def greeting(message):
    # REPLY KEYBOARD
    # keyboard = types.ReplyKeyboardMarkup()
    # btn1 = types.KeyboardButton(text='/time')
    # btn2 = types.KeyboardButton(text='/image')
    # keyboard.add(btn1)
    # keyboard.add(btn2)
    # bot.send_message(message.chat.id, "выберите команду:", reply_markup=keyboard)
    # print(message)

    #INLINE KEYBOARD
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='time', callback_data="btn1")
    btn2 = types.InlineKeyboardButton(text='image', callback_data="btn2")
    keyboard.add(btn1)
    keyboard.add(btn2)
    bot.send_message(message.chat.id, "выберите команду:", reply_markup=keyboard)


    # bot.send_message(message.chat.id, '/start - starting message' + '\n' + '/time - get current time')


@bot.callback_query_handler(func = lambda call:True)
def inline_keyboard_click(call):
    if call.data == "btn1":
        bot.send_message(call.message.chat.id, time.asctime())
    elif call.data == "btn2":
        f = open("a1ab2599007589a93047258cc4f9c42d.jpg", 'rb')
        bot.send_message(call.message.chat.id, f)



@bot.message_handler(commands=['time'])
def getTime(message):
    bot.send_message(message.chat.id, str(time.asctime()))

@bot.message_handler(commands=['image'])
def get_image(message):
    f = open("a1ab2599007589a93047258cc4f9c42d.jpg", 'rb')
    bot.send_photo(message.chat.id, f)


@bot.message_handler(content_types=['text'])
def handling(message):
    if message.text == 'random':
        bot.send_message(message.chat.id, random.randint(0, 100))

    else:
        text = message.text
        speech = gTTS(text=text, lang="en", slow="False", tld="co.in")
        speech.save("audio.mp3")
        f = open("audio.mp3", "rb")

        bot.send_audio(message.chat.id, f)
    print(time.asctime())

bot.polling()