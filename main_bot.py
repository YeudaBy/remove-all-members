from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


app_id = 000000
app_key = '#########################'
token = "123456abcdefghijklmnopqrstzw"

app = Client("remove", app_id, app_key, bot_token=token)


TEXT_STARTED = 'הרובוט מתחיל בהסרת {} משתמשים מהקבוצה 🥾'
TEXT_FINISH = 'הרובוט סיים להסיר {} משתמשים מהקבוצה'
TEXT_ERROR = 'משהו נכשל. בדוק אם קיבלתי הרשאות ניהול מספיקות, או שלח זה למפתח:\n {}'
TEXT_PRIVATE = '''
היי, אני רובוט שיעזור לכם להסיר את כל המשתמשים מהקבוצה שלכם 🥾

הוסיפו אותי לקבוצה, ואל תשכחו לתת לי ניהול מתאים כדי שאוכל להסיר אותם.
הוספתם? מעולה. עכשיו תשלחו בקבוצה /kick ואני אתחיל בעבודה שלי.


הרובוט נוצר ע"י [מקליד תמיד](tg://user?id=789248230). ניתן לפנות לכל בקשה או הערה, ואשתדל לעזור בשמחה.    
'''


members_count_kicks = 0


@app.on_message(filters.group & filters.command("kick"))
def main(c,m):
    chat = m.chat
    global members_count_kicks
    status_me = chat.get_member("me")
    if status_me.status in ["administrator","creator"]:
        try:
            members_count = str(chat.members_count)
            c.send_message(chat.id,TEXT_STARTED.format(members_count))
            for member in c.iter_chat_members(chat.id):
                if member.status in ["administrator","creator"]:
                    pass
                else:
                    chat.kick_member(member.user.id)
                    members_count_kicks += 1
            c.send_message(chat.id, TEXT_FINISH.format(members_count_kicks))
        except Exception as e:
            c.send_message(chat.id,TEXT_ERROR.format(str(e)))
    else:
        c.send_message(chat.id,TEXT_ERROR.format("no admin"))


@app.on_message(filters.group & filters.service)
def service(c,m):
    m.delete()

@app.on_message(filters.private)
def start(c,m):
    m.reply(TEXT_PRIVATE,disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup(
          [[InlineKeyboardButton(text="לערוץ שלי 🎀",
                       url="https://t.me/m100achuzyou")],
           [InlineKeyboardButton(text="עדכוני רובוטים",
                       url="https://t.me/M100achuzBots")]
           ]))


app.run()
