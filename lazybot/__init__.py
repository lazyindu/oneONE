import logging
import logging.config
from pyrogram import Client, types
from database.ia_filterdb import Media
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from aiohttp import web

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
logger = logging.getLogger(__name__)

class LazyPrincessXBot(Client):
    def __init__(self, name, bot_token):
        super().__init__(
            name=name,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=bot_token,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially."""
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1

multi_clients = {}
work_loads = {}
