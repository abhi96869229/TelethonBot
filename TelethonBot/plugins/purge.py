"""
• `{i}purgech <reply to message>`
    Purge all messages from the replied message.

• `{i}purgemech <reply to message>`
    Purge Only your messages from the replied message.

• `{i}purgeallch <reply to message>`
    Delete all msgs of replied user.
"""
import asyncio

from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from . import *


@ultroid_cmd(pattern="purgech$",allow_sudo=False)
async def fastpurger(purg):
    chat = await purg.get_input_chat()
    msgs = []
    count = 0
    if not purg.reply_to_msg_id:
        return await eod(purg, "`Reply to a message to purge from.`", time=10)
    async for msg in ultroid_bot.iter_messages(chat, min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await ultroid_bot.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await ultroid_bot.delete_messages(chat, msgs)
    done = await ultroid_bot.send_message(
        purg.chat_id,
        "__Fast purge complete!__\n**Purged** `"
        + str(len(msgs))
        + "` **of** `"
        + str(count)
        + "` **messages.**",
    )
    await asyncio.sleep(5)
    await done.delete()


@ultroid_cmd(pattern="purgemech$",allow_sudo=False)
async def fastpurgerme(purg):
    chat = await purg.get_input_chat()
    msgs = []
    count = 0
    if not purg.reply_to_msg_id:
        return await eod(purg, "`Reply to a message to purge from.`", time=10)
    async for msg in ultroid_bot.iter_messages(
        chat,
        from_user="me",
        min_id=purg.reply_to_msg_id,
    ):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await ultroid_bot.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await ultroid_bot.delete_messages(chat, msgs)
    done = await ultroid_bot.send_message(
        purg.chat_id,
        "__Fast purge complete!__\n**Purged** `" + str(count) + "` **messages.**",
    )
    await asyncio.sleep(5)
    await done.delete()


@ultroid_cmd(pattern="purgeallch$",allow_sudo=False)
async def _(e):
    xx = await eor(e, get_string("com_1"))
    if e.reply_to_msg_id:
        input = (await e.get_reply_message()).sender_id
        name = (await e.client.get_entity(input)).first_name
        try:
            nos = 0
            async for x in e.client.iter_messages(e.chat_id, from_user=input):
                await e.client.delete_messages(e.chat_id, x)
                nos += 1
            await xx.edit(
                f"**Purged **`{nos}`** msgs of **[{name}](tg://user?id={input})",
            )
        except ValueError:
            return await eod(xx, str(er), time=5)
    else:
        return await eod(
            xx,
            "`Reply to someone's msg to delete.`",
            time=5,
        )


@ultroid_cmd(
    pattern="del$",
)
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
        except BaseException:
            await eod(
                delme,
                f"Couldn't delete the message.\n\n**ERROR:**\n`{str(e)}`",
                time=5,
            )


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
