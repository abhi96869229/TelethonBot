from pyrogram import Client, filters
import asyncio
from uxh import app
from uxh import USER_PREFIX
from uxh import SUDO_USERS
from uxh import edit_or_reply


@app.on_message(filters.user(SUDO_USERS) & filters.command('bigspam',USER_PREFIX),)
async def bigspam(client, message):
    if (message.text and 
        len(message.text.split()) == 1
        or message.caption
        and len(message.caption.split()) == 1
    ):
        await edit_or_reply(
            message,
            text=" Usage : ` *spam <number of times> - <text> `" ,
        )
        return
    
    if message.caption:
        text = message.caption.split(None, 1)[1]
    else:
        text = message.text.split(None, 1)[1]
    
    inpt = text
   ## inpt = inpt.replace('*spam','')
    inpt = inpt.split('-')
    time = int(inpt[0])
    time = time
    spamtext = inpt[1]
    
    for x in range(time):
        await app.send_message(message.chat.id,spamtext)
    
    