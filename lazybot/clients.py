    # Credit @LazyDeveloper.
    # Please Don't remove credit.
    # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey
    # 🥰  Thank you for giving me credit @LazyDeveloperr  🥰

    # for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
# import asyncio
# import logging
# from info import *
# from pyrogram import Client
# from util.config_parser import TokenParser
# from . import multi_clients, work_loads, LazyPrincessBot

# class TokenParser:
#     def parse_from_env(self):
#         tokens = BOT_TOKEN
#         return {i: token for i, token in enumerate(tokens)}

# async def initialize_clients():
#     multi_clients[0] = LazyPrincessBot
#     work_loads[0] = 0
#     all_tokens = TokenParser().parse_from_env()
#     if not all_tokens:
#         print("No additional clients found, using default client")
#         return
    
#     async def start_client(client_id, token):
#         try:
#             print(f"Starting - Client {client_id}")
#             if client_id == len(all_tokens):
#                 await asyncio.sleep(2)
#                 print("This will take some time, please wait...")
#             client = await Client(
#                 name=str(client_id),
#                 api_id=API_ID,
#                 api_hash=API_HASH,
#                 bot_token=token,
#                 sleep_threshold=SLEEP_THRESHOLD,
#                 no_updates=True,
#                 in_memory=True
#             ).start()
#             work_loads[client_id] = 0
#             return client_id, client
#         except Exception:
#             logging.error(f"Failed starting Client - {client_id} Error:", exc_info=True)
    
#     clients = await asyncio.gather(*[start_client(i, token) for i, token in all_tokens.items()])
#     multi_clients.update(dict(clients))
#     if len(multi_clients) != 1:
#         MULTI_CLIENT = True
#         print("Multi-Client Mode Enabled")
#     else:
#         print("No additional clients were initialized, using default client")

import asyncio
import logging
from info import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client
from . import multi_clients, work_loads, LazyPrincessBot

async def initialize_clients():
    logging.info("Initializing Clients")
    multi_clients[0] = LazyPrincessBot
    work_loads[0] = 0

    all_tokens = {i: token for i, token in enumerate(BOT_TOKEN)}
    logging.info(f"Found tokens: {all_tokens}")

    if not all_tokens:
        logging.warning("No additional clients found, using default client")
        return

    async def start_client(client_id, token):
        try:
            logging.info(f"Starting - Client {client_id}")
            client = Client(
                name=f"client_{client_id}",
                api_id=API_ID,
                api_hash=API_HASH,
                bot_token=token,
                sleep_threshold=60,
                no_updates=True,
                in_memory=True
            )
            await client.start()
            work_loads[client_id] = 0
            logging.info(f"Client {client_id} started successfully")
            return client_id, client
        except Exception as e:
            logging.error(f"Failed starting Client - {client_id}. Error: {e}", exc_info=True)
            return None

    clients = await asyncio.gather(*[start_client(i, token) for i, token in all_tokens.items()])
    multi_clients.update({client_id: client for client_id, client in clients if client is not None})

    if len(multi_clients) > 1:
        logging.info("Multi-Client Mode Enabled")
    else:
        logging.warning("No additional clients were initialized, using default client")
