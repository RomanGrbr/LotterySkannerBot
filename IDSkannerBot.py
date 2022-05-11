from config import TOKEN_BOT, API_ID, API_HASH
from telethon.sync import TelegramClient
import logging
from telethon import events
from telethon.tl.custom import Message

class Bot(TelegramClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.me = None

bot = Bot('bot', API_ID, API_HASH)
bot.parse_mode = 'HTML'
logging.basicConfig(level=logging.INFO)

async def start():
    await bot.connect()
    bot.me = await bot.sign_in(bot_token=TOKEN_BOT)
    # await bot.run_until_disconnected()


# def run():
#     bot.loop.run_until_complete(start())

@bot.on(events.ChatAction())
async def on_join(event: events.ChatAction.Event):
    if event.is_group and event.user_added and event.user_id == bot.me.id:
        await bot.send_message(event.chat.id, 'Приветствую, господа!')

@bot.on(events.NewMessage(func=lambda e: e.text.lower() == 'ты кто?'))
async def who_are_you(event: Message):
    await event.respond('Я умный, красивый, в меру упитанный мужчина в полном расцвете сил!')

if __name__ == '__main__':
    # run()
    bot.start()
    bot.run_until_disconnected()
