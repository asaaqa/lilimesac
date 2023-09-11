import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from FallenMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from FallenMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["اسمراني","اسسمر","اسممر","اسمر"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ASAKIOP")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━━𓆩𝐉𝐔𝐋𝐈𝐀𓆪━━⩺\n\n‍ ¦dev :{name}\n ¦user :@{usr.username}\n ¦id :`{usr.id}`\n ¦bio :{usr.bio}\n\n**⩹━━𓆩𝐉𝐔𝐋𝐈𝐀𓆪━━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
 @app.on_message(
    command(["السورس" ,"السوورس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Aaaahmm")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━━𓆩𝐉𝐔𝐋𝐈𝐀𓆪━━⩺\n\n‍ ¦dev :{name}\n ¦user :@mcsec7\n ¦id :`{usr.id}`\n ¦bio :{usr.bio}\n\n**⩹━━𓆩𝐉𝐔𝐋𝐈𝐀𓆪⁩━━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/Aaaahmm")
                ],
            ]
        ),
    )
