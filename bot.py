import logging
import logging.config
# Credit @LazyDeveloper.
# Please Don't remove credit.
# Born to make history @LazyDeveloper !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @LazyDeveloperr  🥰
# for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
# rip paid developers 🤣 - >> No need to buy paid source code while @LazyDeveloperr is here 😍😍
# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import os
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from telethon import TelegramClient, functions, types
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from aiohttp import web
from plugins import web_server

import asyncio
from pyrogram import idle
from lazybot import LazyPrincessBot

from util.keepalive import ping_server
from lazybot.clients import initialize_clients


PORT = "8080"
LazyPrincessBot.start()
loop = asyncio.get_event_loop()


async def Lazy_start():
    print('\n')
    print(' Initalizing Telegram Bot ')
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    bot_info = await LazyPrincessBot.get_me()
    LazyPrincessBot.username = bot_info.username
    await initialize_clients()
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    b_users, b_chats , lz_verified = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    temp.LAZY_VERIFIED_CHATS = lz_verified
    await Media.ensure_indexes()
    me = await LazyPrincessBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    LazyPrincessBot.username = '@' + me.username
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0" if ON_HEROKU else BIND_ADRESS
    await web.TCPSite(app, bind_address, PORT).start()
    logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info(LOG_STR)
    await idle()

async def create_channel_and_add_bot():
    # await client.start()

    # Step 1: Create the channel
    result = await LazyPrincessBot(functions.channels.CreateChannel(
        title='lazyChannel',
        about='Thanks for your contribution',
        megagroup=False
    ))

    channel_id = result.chats[0].id
    print(f"Channel created: {channel_id}")

    # Step 2: Invite bot to the channel
    me = await LazyPrincessBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    await LazyPrincessBot(functions.channels.InviteToChannel(
        channel=channel_id,
        users=[temp.U_NAME]
    ))
    print(f"Bot invited to channel")

    # Step 3: Promote bot to admin
    await LazyPrincessBot(functions.channels.EditAdmin(
        channel=channel_id,
        user_id=temp.ME,
        admin_rights=types.ChatAdminRights(
            change_info=True,
            post_messages=True,
            edit_messages=True,
            delete_messages=True,
            ban_users=True,
            invite_users=True,
            pin_messages=True,
            add_admins=False,
        ),
        rank='Admin'
    ))
    print(f"Bot promoted to admin")

# async def promote_bot_to_admin(channel_id):
#     # async with LazyPrincessBot:
#     bot_info = await LazyPrincessBot.get_me()
#     result = await LazyPrincessBot.invoke(
#         functions.channels.EditAdmin(
#             channel=channel_id,
#             user_id=bot_info.id,
#             admin_rights=types.ChatAdminRights(
#                 change_info=True,
#                 post_messages=True,
#                 edit_messages=True,
#                 delete_messages=True,
#                 ban_users=True,
#                 invite_users=True,
#                 pin_messages=True,
#                 add_admins=False,
#             ),
#             rank="Admin"
#         )
#     )
#     print(f'Bot promoted to admin: {result}')

# async def create_lazy_channel():
#     # async with LazyPrincessBot:
#     result = await LazyPrincessBot.invoke(
#         functions.channels.CreateChannel(
#             title="lazyChannel",
#             about="Thanks for your contribution",
#             megagroup=False
#         )
#     )
#     print(f"Channel created: {result}")
#     return result

# async def delete_lazy_channel(channel_id):
#     # async with LazyPrincessBot:
#     result =  await LazyPrincessBot.invoke(
#         functions.channels.DeleteChannel(
#             channel=channel_id
#         )
#     )
#     print(f'channel deleted successfully : {result}')

if __name__ == '__main__':
    try:
        loop.run_until_complete(Lazy_start())
        logging.info('-----------------------🧐 Service running in Lazy Mode 😴-----------------------')
    except KeyboardInterrupt:
        logging.info('-----------------------😜 Service Stopped Sweetheart 😝-----------------------')
