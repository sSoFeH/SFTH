import random
import time
import webbrowser
import requests
from telethon.sync import TelegramClient
from telethon import functions, types

token = '6129224272:AAG3WWUEnYR_BSumVOvQe-Gds-H93KdOYtk'
ID = '929366169'
api_id = '26687243'
api_hash = 'a9d8b94782781fbb2728c05facf55a4e'
phone_number = '+48699536846'
channel_username = 'ChatDonee'



with TelegramClient('none', api_id, api_hash) as client:
    X = 1
    ABC = 'ASDFGHJKLQWERTYUIOPZXCVBNM'
    klshy = 'ASDFGHJKLZXCVBNMQWERTYUIOP1234567890'
    Extrra = 1
    while True:
        F = ''.join(random.sample(ABC, Extrra))
        G = ''.join(random.sample(klshy, Extrra))
        Ali = (F + F + F + F + G + F)
        extra = (F + G + F + F + G)
        Extra = (F + F + G + F + G)
        eXtra = (F + F + F + G + F)
        LL = (F + G + F + G + G)
        LL = (F + F + G + F + F + F)
        LL = (F + G + F + F + F + F)
        ZZ = (F + F + F + F + G + F)
        MM = (F + F + F + G + F + F)
        T = (G+F+F+G+G+G+G+F+G+F+F)
        EXTRA = Ali, extra, T, Extra, eXtra, LL, ZZ, MM
        user = str("".join(random.choice(EXTRA)))
        url = f"https://t.me/{user}"
        req = requests.get(url)
        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            print(f"'\033[1;32m [ {X} ] متـاح : {user} ")
            try:
                req = requests.post(
                    f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Welcome.\n========\nحـصلتلك يـوزر راقـي ✅ \n- - - - - - - - - - - - - - - -\n@{user} \nاداة : @x_xxi"
                )
            except NameError:
                pass
            else:
                print(f"\033[2;39m [ {X} ] مـحجـوز >> {user} ")

            # Change channel username and send a message with the new username
            try:
                client(functions.channels.UpdateUsernameRequest(
                    channel=channel_username,
                    username=user
                ))
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                message = f"New username: {user}\nTime: {current_time}"
                client(functions.messages.SendMessageRequest(
                    peer=channel_username,
                    message=message
                ))
            except Exception as e:
                print("Failed to change the username:", str(e))
            else:
                print("Username changed successfully!")
                break

            X += 1
            time.sleep(1)
