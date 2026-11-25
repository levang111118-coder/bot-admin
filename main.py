from config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    fact = response.json()["text"]
    bot.reply_to(message, fact)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()