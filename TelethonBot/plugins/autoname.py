from telethon import events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.errors import FloodWaitError
import asyncio
import time
import shutil
from pytz import timezone
from . import *


@ultroid_cmd(pattern="autoname")  # pylint:disable=E0602
async def _(ult):
    if (await bot.get_me()).last_name:
        DEFAULTUSER = (await bot.get_me()).first_name + " " + (await bot.get_me()).last_name
    else:
        DEFAULTUSER = (await bot.get_me()).first_name
    udB.set("OLDNAME", str(DEFAULTUSER))
    udB.set("AUTONAME", "True")
    await eor(ult, "Auto Name has been started Master")
    while True:
        if udB.get("TIMEZONE") is not "None":
            tym = datetime.now(timezone(udB.get("TIMEZONE")))
        else:
            tym = datetime.now(timezone('Asia/Kolkata'))
        ge = udB.get("AUTONAME")
        if not ge == "True":
            return
        DMY = tym.strftime("%d.%m.%Y")
        HM = tym.strftime("%H:%M")
        Naam = udB.get("OLDNAME")
        name = f"⌚{HM} 🔥{Naam}🔥 📅{DMY}"
        try:
            await bot(UpdateProfileRequest(  # pylint:disable=E0602
                first_name=name
            ))
        except FloodWaitError as ex:
            await asst.send_message(
                    Var.LOG_CHANNEL,
                    f"Floodwait of {ex.seconds}.",
                )
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(60)


@ultroid_cmd(pattern="stopname")
async def stoppo(ult):
    name = udB.get("OLDNAME")
    gt = udB.get("AUTONAME")
    await bot(UpdateProfileRequest(
        first_name=name))
    if not gt == "True":
        return await eor(ult, "AUTONAME was not in use !!")
    udB.set("AUTONAME", "None")
    await eor(ult, "AUTONAME Stopped !!")