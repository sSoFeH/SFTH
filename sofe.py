import random
import time
import webbrowser
import requests
import time as mm
from telethon.sync import TelegramClient, events

api_id = '20809128'
api_hash = '69c8efc67e1e5b4e696b7f98ee4d7d51'
session_file = '+14809201923.session-journal.session'
client = TelegramClient(session_file, api_id, api_hash)

token = '5846752965:AAHwMYEw2szkv21ziZ8CDOWVHNGNhHbsIi4'
ID = '929366169'
X = 1
_ = '_'
b = 'bot'
ABC = 'ASDFGHJKLQWERTYUIOPZXCVBNM'
klshy = 'ASDFGHJKLZXCVBNMQWERTYUIOP1234567890'
Extrra = 1
is_running = False

@client.on(events.NewMessage(pattern='قناة'))
async def create_private_channel(event):
    try:
        entity = await client.get_entity(event.chat_id)
        if entity.is_channel:
            channel = await client.create_channel(entity.username, 'Private channel description', megagroup=False)
            await event.reply(f"Private channel created! ID: {channel.id}")
        else:
            await event.reply("Please send the command in a channel.")
    except Exception as e:
        await event.reply(f"Failed to create private channel: {e}")

def start_execution():
    global X
    while is_running:
        F = ''.join(random.sample(ABC, Extrra))
        G = ''.join(random.sample(klshy, Extrra))
        SoFe = (F + F + G + F + G + F)
        extra = (F + G + F + F + G)
        Extra = (F + G + G + F + G + F)
        eXtra = (F + F + F + G + F)
        LL = (F + G + F + G + G)
        LL = (F + F + G + F + F + G)
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

@client.on(events.NewMessage(pattern='^/start'))
async def handle_start(event):
    global is_running
    if not is_running:
        is_running = True
        await event.reply("The code has started.")
        start_execution()
    else:
        await event.reply("The code is already running.")

@client.on(events.NewMessage(pattern='^/stop'))
async def handle_stop(event):
    global is_running
    if is_running:
        is_running = False
        await event.reply("The code has stopped.")
    else:
        await event.reply("The code is not running.")

@client.on(events.NewMessage(pattern='صيد'))
async def handle_hunt(event):
    keyboard = types.InlineKeyboardMarkup()
    start_button = types.InlineKeyboardButton("Start HUNTING!!", callback_data="start")
    stop_button = types.InlineKeyboardButton("Stop HUNTING", callback_data="stop")
    keyboard.row(start_button, stop_button)
    await event.reply("❤️‍🔥 - - - - Choose bot mode - - - - ❤️‍🔥", reply_markup=keyboard)

@client.on(events.CallbackQuery(pattern='start'))
async def handle_start_callback(event):
    await event.respond("Starting the code.")
    await handle_start(event)

@client.on(events.CallbackQuery(pattern='stop'))
async def handle_stop_callback(event):
    await event.respond("Stopping the code.")
    await handle_stop(event)

def main():
    client.start()
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
