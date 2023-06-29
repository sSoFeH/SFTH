import random
import string
import time
import requests
import json
import threading
from telethon.sync import TelegramClient
from telethon import functions, types

accounts = [
    {
        "name": "صوفي4",
        "api_id": 29380802,
        "api_hash": "b2003f36f0ec042dabd28a482ba40550",
        "session_file": "+48459262237",
    },
    {
        "name": "none",
        "api_id": 26687243,
        "api_hash": "a9d8b94782781fbb2728c05facf55a4e",
        "session_file": "none",
    },
    {
        "name": "bt",
        "api_id": 6539148,
        "api_hash": "d17be4492970ef8725d06d6b469c9ac7",
        "session_file": "bt",
    },
    # Add more accounts as needed
]
current_account = accounts[0]  # Set the default account
client = TelegramClient(current_account["session_file"], current_account["api_id"], current_account["api_hash"])

TOKEN = '5896016729:AAFqCSS1t27VIEcYcGKcaKmKY-PbaVB5CK4'
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"
CHANNEL_ID = None  # This will be set by the 'setchannel' command

patterns = {
    "خماسي": ["a1aa1", "aa1a1", "aaa11", "a11aa", "a1a1a"],
    "سداسي": ["a1aa1a", "aa1a1a", "aa1aa1", "a1aaa1", "aaaa11", "aaa1a1", "a111aa", "aa111a", "aa11aa", "a1a1aa"],
    "رباعي": ["aa_1a", "a1_aa", "aa_a1", "aaa_1", "a1a_a", "a1a_1", "a_11a", "a11_a", "a_111"],
    "عشوائي": ["a1a1aaa111aa1", "a111aaaa111a1"],
}


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
        await client(functions.channels.UpdateUsernameRequest(channel=channel_id, username=username))
        return True
    except Exception as e:
        print(f"خطأ في تغيير اليوزر: {e}")
        return False


async def is_username_available(username):
    try:
        result = await client(functions.contacts.SearchRequest(q=username, limit=1))
        return not bool(result.users)
    except Exception as e:
        print(f"حدث خطأ {e}")
        return False


async def check_usernames(patterns_list, chat_id, chat_data):
    while not chat_data[chat_id]["stop"]:
        username = generate_username(random.choice(patterns_list))
        print(f"Checking username: @{username}")  # Print eachusername being checked
        if await is_username_available(username):
            if await set_chat_username(CHANNEL_ID, username):
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                message_text = f"❤️‍🔥New Username HUNTTED BY SoFe @x_xxi  \n Username ==> @{username} Date and time: {current_time}❤️‍🔥"
                await client.send_message(CHANNEL_ID, message_text)
                send_message(chat_id, f"تم ايجاد يوزر , يوزر القناة اصبح @{username}")
                break  # Stop checking when the channel username is updated
        time.sleep(2)  # Sleep for 2 seconds between checks


async def main_telethon():
    await client.start()
    print("Telethon client started.")


def get_chat_data(chat_data, chat_id):
    if chat_id not in chat_data:
        chat_data[chat_id] = {"stop": False, "current_patterns": []}
    return chat_data


ADMIN_IDS = [6286991122, 929366169]  # Replace with your admin IDs

def process_message(message, chat_data):
    chat_id = message["chat"]["id"]

    # Check if the "text" key exists in the message dictionary
    if "text" not in message:
        return

    text = message["text"].lower()
    user_id = message["from"]["id"]

    if user_id not in ADMIN_IDS:
        return

    if user_id not in ADMIN_IDS:
        return
    if text.startswith("/"):
        if text == "/start":
            keyboard = {
                "inline_keyboard": [
                    [{"text": "خماسي", "callback_data": "خماسي"}],
                    [{"text": "سداسي", "callback_data": "سداسي"}],
                    [{"text": "رباعي", "callback_data": "رباعي"}],
                    [{"text": "عشوائي", "callback_data": "عشوائي"}],
                ]
            }
            send_message(chat_id, "اختار اسم نمط اليوزر للبدء", reply_markup=keyboard)
        elif text.startswith("/stop"):
            chat_data[chat_id]["stop"] = True
            send_message(chat_id, "تم ايقاف البوت")
        elif text.startswith("/setaccount"):
            account_name = text.split()[1]
            global current_account
            for account in accounts:
                if account["name"] == account_name:
                    current_account = account
                    global client
                    client = TelegramClient(current_account["session_file"], current_account["api_id"], current_account["api_hash"])
                    client.loop.run_until_complete(main_telethon())
                    send_message(chat_id, f"تم اختيار الحساب ==> {account_name}")
                    break
            else:
                send_message(chat_id, f"لم يتم ايجاد الحساب '{account_name}'.")
        elif text.startswith("/setchannel"):
            channel_id = text.split()[1]
            if channel_id.startswith("@"):
                channel_id = channel_id[1:]
            global CHANNEL_ID
            CHANNEL_ID = channel_id
            send_message(chat_id, f"تم تغيير القناة: @{channel_id}")
        else:
            send_message(chat_id, "اكتب الأمر بشكل صحيح")


def process_callback_query(callback_query, chat_data):
    chat_id = callback_query["message"]["chat"]["id"]
    data = callback_query["data"]

    if data in patterns:
        chat_data[chat_id]["current_patterns"] = patterns[data]
        chat_data[chat_id]["stop"] = False
        send_message(chat_id, f"Starting to check usernames with pattern '{data}'")

        threading.Thread(target=client.loop.run_until_complete,
                         args=(check_usernames(patterns[data], chat_id, chat_data),)).start()


if __name__ == "__main__":
    def main():
        client.loop.run_until_complete(main_telethon())
        last_update_id = None
        chat_data = {}

        while True:
            updates = get_updates(last_update_id)
            if "result" in updates:
                for update in updates["result"]:
                    last_update_id = update["update_id"] + 1

                    if "message" in update:
                        chat_data = get_chat_data(chat_data, update["message"]["chat"]["id"])
                        process_message(update["message"], chat_data)
                    elif "callback_query" in update:
                        chat_data = get_chat_data(chat_data, update["callback_query"]["message"]["chat"]["id"])
                        process_callback_query(update["callback_query"], chat_data)

            time.sleep(1)


    main()
