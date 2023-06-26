import sys as n
import random
import time
import webbrowser
import requests
import time as mm

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

api_id = '20809128'
api_hash = '69c8efc67e1e5b4e696b7f98ee4d7d51'
bot_token = '5846752965:AAHwMYEw2szkv21ziZ8CDOWVHNGNhHbsIi4'
bot_chat_id = '929366169'

bot = telebot.TeleBot(bot_token)

def create_private_channel(session_file):
    with TelegramClient(session_file, api_id, api_hash) as client:
        result = client(functions.channels.CreateChannelRequest(
            title='Private Channel',
            about='This is a private channel created by the bot.',
            megagroup=False
        ))
        if result and isinstance(result.chats[0], types.Channel):
            return result.chats[0].id

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "The bot has started.")

@bot.message_handler(commands=['قناة'])
def handle_create_channel(message):
    session_file = '+14809201923.session-journal'
    channel_id = create_private_channel(session_file)
    if channel_id:
        bot.send_message(bot_chat_id, f"A new private channel has been created. Channel ID: {channel_id}")
    else:
        bot.send_message(bot_chat_id, "Failed to create the private channel.")

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
