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

@bot.message_handler(func=lambda message: message.text == 'صيدد')
async def hunterusername(event):
    choice = str(event.pattern_match.group(1))
    await event.edit(f"**- تم تفعيل الصيد بنجاح الان**")
    try:
        ch = await jmbot(
            functions.channels.CreateChannelRequest(
                title="HUNTTING BY SOFE",
                about="This Channel To Huntting Usernames By ==> @SoFeThon -- @x_xxi ❤️‍🔥",
            )
        )
        ch = ch.updates[1].channel_id
    except Exception as e:
        await jmbot.send_message(
            event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
        )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "start":
        bot.send_message(call.message.chat.id, "Starting the code.")
        handle_start(call.message)
    elif call.data == "stop":
        bot.send_message(call.message.chat.id, "Stopping the code.")
        handle_stop(call.message)

bot.polling()


a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"

trys, trys2 = [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    session = requests.Session()
    response = session.get(url, headers=headers)

    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "ثلاثيات":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "خماسي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "خماسي حرفين":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسيات":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سباعيات":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "بوتات":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        username = "".join(f)
        username = username + "bot"

    elif choice == "تيست":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], d[0], c[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    else:
        raise ValueError("Invalid choice for username generation.")
    return username


@jmbot.ar_cmd(pattern="الصيد")
async def _(event):
    await event.edit(
        """
أوامر الصيد الخاصة بسورس صوفي : 

ٴ— — — — — — — — — —

النوع :(  سداسي حرفين/ ثلاثيات/ سداسيات/ بوتات/ خماسي حرفين/خماسي /سباعيات )

الامر:  `.صيد` + النوع
- يقوم بصيد معرفات عشوائية حسب النوع

الامر:  `تثبيت` + معرف
* وظيفة الامر : يقوم بالتثبيت على المعرف عندما يصبح متاح يأخذه

ٴ— — — — — — — — — —
الامر:   `.حالة الصيد`
• لمعرفة عدد المحاولات للصيد

الامر:  `.حالة التثبيت`
• لمعرفة عدد المحاولات للصيد

تواصل مع المطور ان لم تفهم -- @x_xxi

"""
    )


@jmbot.ar_cmd(pattern="صيد (.*)")
async def hunterusername(event):
    choice = str(event.pattern_match.group(1))
    await event.edit(f"**- تم تفعيل الصيد بنجاح الان**")
    try:
        ch = await jmbot(
            functions.channels.CreateChannelRequest(
                title="HUNTTING BY SOFE",
                about="This Channel To Huntting Usernames By ==> @SoFeThon -- @x_xxi ❤️‍🔥",
            )
        )
        ch = ch.updates[1].channel_id
    except Exception as e:
        await jmbot.send_message(
            event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
        )
        sedmod = False

    isclaim.clear()
    isclaim.append("on")
    sedmod = True
    while sedmod:
        username = gen_user(choice)
        if username == "error":
            await event.edit("**- يرجى وضع النوع بشكل صحيح**")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await jmbot(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_file(
                    event.chat_id,
                    "https://t.me/SoFeThon/12",
                    caption=" Hunted\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nBy The Best ==> @SoFeThon -- @x_xxi ".format(
                        username, trys, choice
                    ),
                )
                await event.client.send_file(
                    ch,
                    "https://t.me/SoFeThon/12",
                    caption="HUNTED BY SOFE!! \n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Type: {}\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThe BEST ==> @SoFeThon -- @x_xxi ".format(
                        username, trys, choice
                    ),
                )
                await event.client.send_message(
                    "@x_xxi", f"- Done : @{username} !\n- By => @SoFeThon -- @x_xxi !"
                )
                sedmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await jmbot.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                )
                sedmod = False
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                else:
                    await jmbot.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    sedmod = False
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")


@jmbot.ar_cmd(pattern="تثبيت (.*)")
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        ch = ch.replace("@", "")
        await event.edit(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except:
        try:
            ch = await jmbot(
                functions.channels.CreateChannelRequest(
                    title="HUNTING SOFE",
                    about="This Channel To Huntting Usernames By ==> @SoFeThon -- @x_xxi ❤️‍🔥",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم بنجاح بدأ التثبيت**")
        except Exception as e:
            await jmbot.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    isauto.clear()
    isauto.append("on")
    username = str(msg[1])

    swapmod = True
    while swapmod:
        isav = check_user(username)
        if isav == True:
            try:
                await jmbot(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_file(
                    ch,
                    "https://t.me/SoFeThon/12",
                    caption=" Hunted\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nBy The Best ==> @SoFeThon -- @x_xxi ".format(
                        username, trys2
                    ),
                )
                await event.client.send_file(
                    event.chat_id,
                    "https://t.me/SoFeThon/12",
                    caption=" Hunted\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nBy The Best ==> @SoFeThon -- @x_xxi ".format(
                        username, trys2
                    ),
                )
                await event.client.send_message(
                    "@x_xxi",
                    f"- Hunted!! : @{username} !\n- By The Best : @SoFeThon - x_xxi !\n- Hunting Log {trys2}",
                )
                swapmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف **-  @{username} غير صالح . **"
                )
                swapmod = False
                break
            except telethon.errors.FloodError as e:
                await jmbot.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                swapmod = False
                break
            except Exception as eee:
                await jmbot.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                swapmod = False
                break
        else:
            pass
        trys2[0] += 1

    isclaim.clear()
    isclaim.append("off")


@jmbot.ar_cmd(pattern="ايقاف الصيد")
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        return await event.edit("**- تم بنجاح ايقاف عملية الصيد**")
    elif "off" in isclaim:
        return await event.edit("**- لم يتم تفعيل الصيد بالأصل لأيقافه**")
    else:
        return await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@jmbot.ar_cmd(pattern="ايقاف التثبيت")
async def _(event):
    if "on" in isauto:
        isauto.clear()
        isauto.append("off")
        return await event.edit("**- تم بنجاح ايقاف عملية التثبيت**")
    elif "off" in isauto:
        return await event.edit("**- لم يتم تفعيل التثبيت بالأصل لأيقافه**")
    else:
        return await event.edit("**-لقد حدث خطأ ما وتوقف الامر لديك**")


@jmbot.ar_cmd(pattern="حالة الصيد")
async def _(event):
    if "on" in isclaim:
        await event.edit(f"**- الصيد وصل لـ({trys[0]}) **من المحاولات")
    elif "off" in isclaim:
        await event.edit("**- الصيد بالاصل لا يعمل .**")
    else:
        await event.edit("- لقد حدث خطأ ما وتوقف الامر لديك")


@jmbot.ar_cmd(pattern="حالة التثبيت")
async def _(event):
    if "on" in isauto:
        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif "off" in isauto:
        await event.edit("**- التثبيت بالاصل لا يعمل .**")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")
