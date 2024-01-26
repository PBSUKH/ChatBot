#bad op

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from Mickey import MickeyBot
from Mickey.database.chats import add_served_chat
from Mickey.database.users import add_served_user
from Mickey.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    START,
)


@MickeyBot.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁α∂ ❤️ᥫ᭡፝֟፝֟  🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁αву ❤️ᥫ᭡፝֟፝֟  ꨄ︎ 🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁α∂ ❤️ᥫ᭡፝֟፝֟..__")
        await asyncio.sleep(0.2)
        await accha.edit("__🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁α∂ ❤️ᥫ᭡፝֟፝֟  🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁αву ❤️ᥫ᭡፝֟፝֟  ꨄ 🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁α∂ ❤️ᥫ᭡፝֟፝֟.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁α∂ ❤️ᥫ᭡፝֟፝֟  🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁αву ❤️ᥫ᭡፝֟፝֟  ꨄ︎ 🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁α∂ ❤️ᥫ᭡፝֟፝֟..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**๏ ʜᴇʏ, ɪ ᴀᴍ {MickeyBot.name}**\n**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**\n**──────────────**\n**๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ||</b> 
<b>||©️ [🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁α∂ ❤️ᥫ᭡፝֟፝֟](https://t.me/II_BAD_BBY_II) ||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@MickeyBot.on_cmd("help")
async def help(client: MickeyBot, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)




@MickeyBot.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
