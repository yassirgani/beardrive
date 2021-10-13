import telethon
from telethon import errors, functions, types, events , helpers
import asyncio
import aiohttp
import urllib.parse
from . import (
    Config, StreamTools
)
import io
import re
import os.path
import requests
from telethon.sessions import StringSession

class BareServer(Config, StreamTools):
    client: telethon.TelegramClient
    
    def init(self, loop: asyncio.AbstractEventLoop):
        
        self.client = telethon.TelegramClient(
            StringSession(), #self.config.SESS_NAME,
            self.config.APP_ID,
            self.config.API_HASH,
            loop=loop
        ).start(bot_token=self.config.BOT_TOKEN)
        
        
        @self.client.on(events.NewMessage)
        async def download(event : events.NewMessage.Event):
            if event.is_private :
                try:
                    await event.client(functions.channels.GetParticipantRequest(channel=self.config.channel,participant=event.sender_id))
                except errors.UserNotParticipantError:
                    await event.reply(f"برای حمایت از ما ابتدا در کانال ما عضو شوید🙏🏻😊\n\n@{self.config.channel}\n\nپس از عضویت دستور /start را ارسال کنید !.")
                    return
                if event.file :
                    hash = self.encode(f"{event.sender_id}:{event.id}")
                    url = f"{hash}/{urllib.parse.quote(self.get_file_name(event))}"
                    await event.reply(f"لینک با موفقیت تولید شد⚡️!  :   {self.config.ROOT_URI}/w/{url}")
                    return

                await event.reply("✨خوش آمدید \n لطفا یک فایل برای من ارسال کنید تا آن را به لینک تبدیل کنم! \n 🚀 @RocketWorld")
