# bot_0.py
from bot import *

BOT_TOKEN = "6583397612:AAEQ4vI-NdK02bzPp2egcOVzTZbvaW6NAx8"  # Replace with actual bot token

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_bot())
        logging.info('-----------------------🧐 Service running in Lazy Mode 😴-----------------------')
    except KeyboardInterrupt:
        logging.info('-----------------------😜 Service Stopped Sweetheart 😝-----------------------')
