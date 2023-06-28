import random
import time
import requests
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import UpdateUsernameRequest
import telebot
from telebot import types

token = '6094718644:AAF90K7zXROxPicP0donrSQt918AYQiRae8'
channel_username_or_id = 'DONNEChat'
ID = '929366169'
channel_ms = 'SoFeThon'  # Replace with your channel username or ID

api_id = '20809128'  # Replace with your API ID
api_hash = '69c8efc67e1e5b4e696b7f98ee4d7d51'  # Replace with your API Hash

client = TelegramClient('+14809201923.session-journal', api_id, api_hash)
bot = telebot.TeleBot(token)

ABC = 'ASDFGHJKLQWERTYUIOPZXCVBNM'
klshy = 'ASDFGHJKLZXCVBNMQWERTYUIOP1234567890'
Extrra = 1
is_running = False
X = 1

async def change_channel_username(user):
    await client.start()
    channel = await client.get_entity(channel_username_or_id)
    try:
        await client(UpdateUsernameRequest(channel=channel, username=user))
        await client.disconnect()
        return True
    except Exception as e:
        print(f"Error changing username: {e}")
        await client.disconnect()
        return False

async def start_execution():
    global X
    while is_running:
        F = ''.join(random.sample(ABC, Extrra))
        G = ''.join(random.sample(klshy, Extrra))
        SoFe = (F + G + F + F + G)
        extra = (F + G + F + F + G)
        Extra = (F + G + G + F + G + F)
        eXtra = (F+F+G+F+G+F)
        LL = (F+G+F+G+F)
        ZZ = (F+G+G+F+F)
        MM = (F+F+F+G+G)
        EXTRA = SoFe, extra, Extra, eXtra, LL, ZZ, MM
        user = str("".join(random.choice(EXTRA)))
        url = f"https://t.me/{user}"
        req = requests.get(url)
        if req.text.find('If you have <strong>Telegram</strong>, you can contact') >= 0:
            print(f"'\033[1;32m [ {X} ] متـاح : {user} ")
            changed = await change_channel_username(user)
            if changed:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
                bot.send_message({user}, f"New Username HUNTTED BY SoFe @x_xxi ==> \n Username : @{user} Date and time: {timestamp}")
                X += 1
            else:
                print(f"Failed to change channel username to {user}")
        else:
            print(f"\033[2;39m [ {X} ] مـحجـوز >> {user} ")
            X += 1
            await asyncio.sleep(2)

@bot.message_handler(commands=['start'])
def handle_start(message):
    global is_running
    if not is_running:
        is_running = True
        bot.send_message(message.chat.id, "The code has started.")
        asyncio.run(start_execution())
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
    bot.send_message(message.chat.id, "❤️‍🔥 - - - - اختار وضع ابوت - - - - ❤️‍🔥",reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "start":
        bot.send_message(call.message.chat.id, "Starting the hunt...")
        handle_start(call.message)
    elif call.data == "stop":
        bot.send_message(call.message.chat.id, "Stopping the hunt...")
        handle_stop(call.message)

def main():
    print("Bot is running...")
    bot.polling()

if __name__ == '__main__':
    main()
