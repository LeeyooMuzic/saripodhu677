#G-Network Music Projects
#Copyright (C) 2022 By @Groot_Network
#Don't Any Value In This Repo If You Edit Your Github Will Get Banned 😌

import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME, BOT_USERNAME
from config import BOT_NAME
from config import BOT_USERNAME

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/0a87707652242961c79f2.jpg",
        caption=f"""**
❥❥━─────➸➽♦️❥❥━─────➸➽

😒 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 **{message.from_user.mention()} 👋**

💠 𝗧𝗵𝗶𝘀 𝗶𝘀 𝗧𝗵𝗲 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}),** 

💠 𝗔 𝗕𝗼𝘁 𝗙𝗼𝗿 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 𝗛𝗶𝗴𝗵 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗮𝗻𝗱 𝗨𝗻𝗯𝗿𝗲𝗮𝗸𝗮𝗯𝗹𝗲 𝗠𝘂𝘀𝗶𝗰 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽𝘀 𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝘁.

💠 𝗝𝘂𝘀𝘁 𝗔𝗱𝗱 𝗠𝗲 𝘁𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 & 𝗠𝗮𝗸𝗲 𝗮𝘀 𝗮 𝗔𝗱𝗺𝗶𝗻 𝗪𝗶𝘁𝗵 𝗡𝗲𝗲𝗱𝗲𝗱 𝗔𝗱𝗺𝗶𝗻 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻𝘀 𝘁𝗼 𝗣𝗲𝗿𝗳𝗼𝗿𝗺 𝗮 𝗥𝗶𝗴𝗵𝘁 𝗔𝗰𝘁𝗶𝗼𝗻𝘀, 𝗡𝗼𝘄 𝗟𝗲𝘁'𝘀 𝗘𝗻𝗷𝗼𝘆 𝗬𝗼𝘂𝗿 𝗠𝘂𝘀𝗶𝗰!

❥❥━─────➸➽♦️❥❥━─────➸➽**""",
    reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("🌱❰𝗚𝗿𝗼𝗼𝘁 𝗡𝗲𝘁𝘄𝗼𝗿𝗸❱✨", url=f"https://t.me/Groot_Network"),
           ],[
           InlineKeyboardButton("🌸❰𝗨𝗽𝗱𝗮𝘁𝗲𝘀❱✨", url="https://t.me/RJbr0"),  
           InlineKeyboardButton("👻❰𝗢𝘄𝗻𝗲𝗿❱✨", url="https://t.me/MyNameIsGroot"),
           ],[
           InlineKeyboardButton("🥀❰𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗼𝗱𝗲❱✨", url="https://t.me/TeluguFriendsClub")
           ]]
           )
     )
    
@Client.on_message(command(["Groot"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/0c448c9873a3dcb62673a.jpg",
        caption=f"""**🥀🖤 ʸᵒᵘʳ 𝗛𝗘𝗔𝗥𝗧 ⁱˢ 𝗠𝗬 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗜𝗕𝗜𝗟𝗜𝗧𝗬🖤🥀**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "@𝗠𝘆𝗡𝗮𝗺𝗲𝗜𝘀𝗚𝗿𝗼𝗼𝘁", url=f"https://t.me/MyNameIsGroot")
                ]
            ]
        ),
    )
