import asyncio
import logging
from pyrogram import Client
from info import *
from . import multi_clients, work_loads, LazyPrincessXBot

class TokenParser:
    def parse_from_env(self):
        tokens = BOT_TOKEN
        return {i: token for i, token in enumerate(tokens)}

async def initialize_clients():
    multi_clients[0] = LazyPrincessXBot("default_bot", BOT_TOKEN[0])
    work_loads[0] = 0
    all_tokens = TokenParser().parse_from_env()
    if not all_tokens:
        print("No additional clients found, using default client")
        return
    
    async def start_client(client_id, token):
        try:
            print(f"Starting - Client {client_id}")
            client = LazyPrincessXBot(name=f"bot_{client_id}", bot_token=token)
            await client.start()
            work_loads[client_id] = 0
            return client_id, client
        except Exception as e:
            logging.error(f"Failed starting Client - {client_id} Error: {e}", exc_info=True)
    
    clients = await asyncio.gather(*[start_client(i, token) for i, token in all_tokens.items()])
    clients = [client for client in clients if client is not None]  # Filter out failed clients
    multi_clients.update(dict(clients))
    
    if len(multi_clients) > 1:
        print("Multi-Client Mode Enabled")
    else:
        print("No additional clients were initialized, using default client")

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError as e:
        if str(e) == "There is no current event loop in thread 'MainThread'.":
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    loop.run_until_complete(initialize_clients())
