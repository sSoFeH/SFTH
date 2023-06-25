import sys as n
import random
import time
import webbrowser
import requests
import time as mm
import telebot
import telethon
from fake_useragent import UserAgent
from telethon.sync import functions

from jmbot import jmbot
from telebot import types

token = '5846752965:AAHwMYEw2szkv21ziZ8CDOWVHNGNhHbsIi4'
ID = '929366169'
X = 1
_ = '_'
b = 'bot'
ABC = 'ASDFGHJKLQWERTYUIOPZXCVBNM'
klshy = 'ASDFGHJKLZXCVBNMQWERTYUIOP1234567890'
Extrra = 1
is_running = False

bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: message.text == 'صيد')
async def hunterusername(event):
    choice = str(event.pattern_match.group(1))
    await event.edit(f"**- تم تفعيل الصيد بنجاح الان**")
    try:
        ch = await jmbot(
            functions.channels.CreateChannelRequest(
                title="HUNTTING BY SOFE",
                about="This Channel To Huntting Usernames By ==> @SoFeThon -- @x_xxi ❤️‍🔥"
            )
        )

def start_execution():
    global X
    while is_running:
        F = ''.join(random.sample(ABC, Extrra))
        G = ''.join(random.sample(klshy, Extrra))
        SoFe = (F + F + G + F + G + F)
        extra = (F + G + F + F + G)
        Extra = (F + G + G + F + G + F )
        eXtra = (F + F + F + G + F)
        LL = (F + G + F + G + G)
        LL = (F + F + G + F + F + G )
        LL = (F + G + G + F + F + F)
        ZZ = (F + F + F + G + G + F)
        MM = (F + G + F + G + G + G)
        EXTRA = SoFe, extra, Extra, eXtra, LL, ZZ, MM
        user = str("".join(random.choice(EXTRA)))
        url = f"https://t.me/{user}"
        req = requests.get(url)
        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            print(f"'\033[1;32m  [   {X}   ] متـاح : {user} ")
            try:
                req = requests.post(
                    f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Welcome.\n========\nحـصلتلك يـوزر راقـي ✅ \n- - - - - - - - - - - - - - - -\n@{user} \nاداة : @x_xxi ''')
            except NameError:
                pass
        else:
            print(f"\033[2;39m [  {X}  ] مـحجـوز >>  {user} ")
        X += 1

@bot.message_handler(commands=['start'])
def handle_start(message):
    global is_running
    if not is_running:
        is_running = True
        bot.send_message(message.chat.id, "The code has started.")
        start_execution()
    else:
        bot.send_message(message.chat.id, "The code is already running.")

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    global is_running
    if is_running:
        is_running = False
        bot.send_message(message.chat.id, "The code has stopped.")
    else:
        bot.send_message(message.chat.id, "The code is not running.")

@bot.message_handler(func=lambda message: message.text == 'صيد')
def handle_hunt(message):
    keyboard = types.InlineKeyboardMarkup()
    start_button = types.InlineKeyboardButton("Start HUNTTING!!", callback_data="start")
    stop_button = types.InlineKeyboardButton("Stop HUNTTING", callback_data="stop")
    keyboard.row(start_button, stop_button)
    bot.send_message(message.chat.id, "❤️‍🔥 - - - - اختار وضع ابوت - - - - ❤️‍🔥", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "start":
        bot.send_message(call.message.chat.id, "Starting the code.")
        handle_start(call.message)
    elif call.data == "stop":
        bot.send_message(call.message.chat.id, "Stopping the code.")
        handle_stop(call.message)

bot.polling()