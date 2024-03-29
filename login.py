from telethon.sync import TelegramClient
from telethon.sessions import StringSession

from config import API_HASH, API_ID


# Авторизация и печать ключа сессии
with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())
