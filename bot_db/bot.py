from telebot import *
from db import Product


TOKEN = "1883154030:AAGF21aoXyK3TYzLvlrRrOqxKUG6rObEG2U"

bot = TeleBot(TOKEN)
products = Product("product.sql")
# products.create_table()

name = ""
amount = ""
price = ""
category = ""

@bot.message_handler(commands=['start'])
def greeting(message):
    bot.send_message(message.chat.id, "Напиште что хотите сделать")

@bot.message_handler(commands=['create'])
def create_product(message):
    bot.send_message(message.chat.id, "Введите название товара:")
    bot.register_next_step_handler(message, ask_amount)

@bot.message_handler(commands=['show'])
def show_products(message):
    data = products.select_products()
    for product in data:
        temp = "ID: " + product[0] + "\n" + "Name: " + product[1] + "\n" + "Amount: " + str(product[2]) + "\n" + "Price: " + str(product[3]) + "\n" + "Category: " + product[4]
        bot.send_message(message.chat.id, temp)



def ask_amount(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, "Введите колво товара:")
    bot.register_next_step_handler(message, ask_price)

def ask_price(message):
    global amount
    amount = int(message.text)
    bot.send_message(message.chat.id, "Введите цену товара:")
    bot.register_next_step_handler(message, ask_category)


def ask_category(message):
    global price
    price = int(message.text)
    bot.send_message(message.chat.id, "Введите категорию товара:")
    bot.register_next_step_handler(message, insert_product)

def insert_product(message):
    global category
    category = message.text
    insert_final()


def insert_final():
    global name, price, amount, category
    ID = len(products.select_products()) + 1
    products.insert_product(ID, name, amount, price, category)
    data = products.select_products()
    print(data)
    name = ""
    amount = ""
    price = ""
    category = ""


bot.polling()