# bot_1.py
from bot import *

BOT_TOKEN = "6030299293:AAERiihnla1k7Tti8OhMU47AhnhuHUMeHgU"  # Replace with actual bot token

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_bot())
        logging.info('-----------------------🧐 Service running in Lazy Mode 😴-----------------------')
    except KeyboardInterrupt:
        logging.info('-----------------------😜 Service Stopped Sweetheart 😝-----------------------')
