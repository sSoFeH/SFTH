import random
import sys
import string
import time
import requests
import json
import threading
import asyncio
import re
from telethon.sync import TelegramClient
from telethon import functions, types

accounts = [
    {
        "name": "SoFe2",
        "api_id": 20809128,
        "api_hash": "69c8efc67e1e5b4e696b7f98ee4d7d51",
        "session_file": "SoFe",
        "channel_username": "@SFDONE2"
    },
    {
        "name": "SoFe5",
        "api_id": 18488234,
        "api_hash": "f5ffd16eaf366c3ce4f11d0d376915d7",
        "session_file": "SoFe5",
        "channel_username": "@SFDONE5"
    },
    {
        "name": "SoFe6",
        "api_id": 29380802,
        "api_hash": "b2003f36f0ec042dabd28a482ba40550",
        "session_file": "SoFe6",
        "channel_username": "@SFDONE6"
    },
    {
        "name": "SoFe7",
        "api_id": 6991944,
        "api_hash": "f2a57040043608b53890598eec021cdc",
        "session_file": "SoFe7",
        "channel_username": "@SFDONE7"
    },
    {
        "name": "SoFe8",
        "api_id": 22645434,
        "api_hash": "3d5ba78bf3e7d29dcb923d1d8368b4f9",
        "session_file": "SoFe8",
        "channel_username": "@SFDONE8"
    },
    {
        "name": "SoFe9",
        "api_id": 28538270,
        "api_hash": "a11a4f75370b98f3555c5f70de0f7c21",
        "session_file": "SoFe9",
        "channel_username": "@SFDONE9"
    },
    {
        "name": "SoFe10",
        "api_id": 22418318,
        "api_hash": "b6757fd9c11bf751579298ce2236e1bd",
        "session_file": "SoFe10",
        "channel_username": "@SFDONE10"
    },
    {
        "name": "SoFe11",
        "api_id": 17633498,
        "api_hash": "9f29b73397e59c064b6064f16f189a9b",
        "session_file": "SoFe11",
        "channel_username": "@SFDONE11"
    },
    {
        "name": "SoFe12",
        "api_id": 21006277,
        "api_hash": "69e5f5764d981707160ceca976db13af",
        "session_file": "SoFe12",
        "channel_username": "@SFDONE12"
    },
    {
        "name": "SoFe13",
        "api_id": 25715430,
        "api_hash": "416afb2125072837f9861a2ffd93cfe7",
        "session_file": "SoFe13",
        "channel_username": "@SFDONE13"
    },
    # Add more accounts as needed
]
clients = [TelegramClient(account["session_file"], account["api_id"], account["api_hash"]) for account in accounts]
print("it works (-:")
sys.stdout.flush()
current_account_index = 0  # Set the default account index
client = clients[current_account_index]

TOKEN = '6378255143:AAEp0H9cyM7xGWWVM8LXjOKX3ojZ68-w95k'
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

patterns = {
    "خماسي": ["a1aa1", "aa1a1", "aaa11", "a11aa", "a1a1a"],
    "سداسي": ["a1aa1a", "aa1a1a", "aa1aa1", "a1aaa1", "aaaa11", "aaa1a1", "a111aa", "aa111a", "aa11aa", "a1a1aa"],
    "عشوائي": ["a1a1aaa111aa1", "a111aaaa111a1"],
}
timer_interval = 5  # Default timer interval in seconds


def generate_username(pattern: str) -> str:
    random_letter = random.choice(string.ascii_lowercase)
    random_char = random.choice(string.ascii_lowercase + string.digits)
    username = ""
    for char in pattern:
        if char == "a":
            username += random_letter
        elif char == "1":
            username += random_char
    return username


def get_updates(offset=None, timeout=30):
    params = {'timeout': timeout, 'offset': offset}
    raw_resp = requests.get(BASE_URL + 'getUpdates', params)
    try:
        resp = json.loads(raw_resp.text)
    except json.JSONDecodeError as e:
        print(f"Failed to parse response: {raw_resp.text}")
        raise e
    return resp


def send_message(chat_id, text, reply_markup=None):
    params = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    if reply_markup:
        params["reply_markup"] = json.dumps(reply_markup)
    raw_resp = requests.post(BASE_URL + 'sendMessage', params)
    try:
        resp = json.loads(raw_resp.text)
    except json.JSONDecodeError as e:
        print(f"Failed to parse response: {raw_resp.text}")
        raise e
    return resp


async def set_chat_username(channel_id, username):
    try:
        if channel_id:
            channel_entity = await client.get_entity(channel_id)
            if isinstance(channel_entity, types.Channel):
                await client(functions.channels.UpdateUsernameRequest(
                    channel=channel_entity,
                    username=username
                ))
                return True
            else:
                print(f"Error updating username: Invalid channel entity for ID {channel_id}")
                return False
        else:
            print("Error updating username: Channel ID is not set.")
            return False
    except Exception as e:
        print(f"Error updating username: {e}")
        return False


async def is_username_available(username):
    try:
        result = await client(functions.contacts.SearchRequest(q=username, limit=1))
        return not bool(result.users)
    except Exception as e:
        print(f"Error checking username availability: {e}")
        return False


async def check_usernames(patterns_list, chat_id, chat_data):
    while not chat_data[chat_id]["stop"]:
        username = generate_username(random.choice(patterns_list))
        print(f"Checking username: @{username}")
        if await is_username_available(username):
            if await set_chat_username(accounts[current_account_index]["channel_username"], username):
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                message_text = f"❤️‍🔥New Username HUNTED \n BY -- SoFe @x_xxi --  \n Username ==> @{username} Date and time: {current_time}❤️‍🔥 \n old username {accounts[current_account_index]['channel_username']}"
                await client.send_message(username, message_text)
                send_message(chat_id, f"*تم ايجاد يوزر , يوزر القناة اصبح @{username} في حسابك الذي اسمه {accounts[current_account_index]['name']}*")
                await asyncio.sleep(2)  # Wait 2 seconds before generating the next username
            else:
                print("Failed to set the new username.")
        await asyncio.sleep(2)  # Wait 2 seconds before checking the next username





admins = [6286991122, 929366169]  # List of allowed admin IDs

def handle_updates(updates):
    global timer_interval  # Add a global variable for the timer interval
    for update in updates["result"]:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"].lower()
        user_id = update["message"]["from"]["id"]  # Get the ID of the user sending the message
        if user_id not in admins:  # Check if the user is not an admin
            send_message(chat_id, "انت لست ادمن لايمكنك استخدام هذا البوت  , تواصل مع المطور اذا كنت تريد استعمال البوت \n المطور ==> SoFe -- @x_xxi")
            continue
        if text.startswith("/start"):
            send_message(chat_id, "*اهلا مطوري , اختار النوع ليبدا في صيد اليوزرات على حسب طلبك*")
            reply_markup = {
                "keyboard": [
                    [{"text": "خماسي"}],
                    [{"text": "سداسي"}],
                    [{"text": "عشوائي"}],
                ],
                "one_time_keyboard": True,
                "resize_keyboard": True,
            }
            send_message(chat_id, "*اختر نوع اليوزر الذي تريد صيده*", reply_markup=reply_markup)
        elif text == "ايقاف الصيد":
            chat_data[chat_id]["stop"] = True  # Set stop flag to True
            send_message(chat_id, "*تم ايقاف الصيد*")
        elif text == "زمن اليوزرز":
            send_message(chat_id, f"*زمن تغيررالحسابات الحالي هو {timer_interval} ثانية*")
        elif text.isdigit():
            timer_interval = int(text)
            send_message(chat_id, f"*تم تعديل زمن تغيير الحسابات الى {timer_interval} ثانية*")
        elif text in patterns.keys():
            if chat_id not in chat_data:
                chat_data[chat_id] = {"stop": False}
            threading.Thread(target=client.loop.run_until_complete, args=(check_usernames(patterns[text], chat_id, chat_data),)).start()
        elif text == "/stop":
            if chat_id in chat_data:
                chat_data[chat_id]["stop"] = True
        elif text.startswith("/settime"):
            match = re.match(r"/settime\s+(\d+)", text)
            if match:
                new_interval = int(match.group(1))
                timer_interval = new_interval
                send_message(chat_id, f"*تم تعديل زمن تغيير الحسابات إلى {new_interval} ثانية*")
            else:
                send_message(chat_id, "الرجاء كتابة الأمر بالشكل الصحيح. استخدم /settime <عدد الثواني> \n ثم قم باختيار النمط من خلال إرسال /start")

def switch_account():
    global current_account_index, client
    if current_account_index < len(clients) - 1:
        current_account_index += 1
    else:
        current_account_index = 0
    client = clients[current_account_index]
    print(f"Switched to account: {accounts[current_account_index]['name']}")  # Print the account name when switching
    send_message(admins[0], f"Switched to account: {accounts[current_account_index]['name']}")  # Notify admin when switching account
    threading.Timer(timer_interval, switch_account).start()
if __name__ == "__main__":
    chat_data = {}
    for client in clients:
        client.start()

    switch_account()  # Start switching accounts
    last_update_id = None
    while True:
        try:
            updates = get_updates(last_update_id)
            if len(updates["result"]) > 0:
                last_update_id = updates["result"][-1]["update_id"] + 1
                handle_updates(updates)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

    for client in clients:
        client.disconnect()
