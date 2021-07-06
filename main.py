import telebot
import requests

API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hello. \
""")

@bot.message_handler(commands=['setpinoff'])
def setpinpff_(message):
    print("works")
    r = requests.get("http://IP//LED=ON")
    print(r)


@bot.message_handler(commands=['setpin'])
def setpin_(message):
    print("works")
    r = requests.get("http://IP//LED=OFF")
    print(r)

bot.polling()
