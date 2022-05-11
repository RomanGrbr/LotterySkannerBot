# from pyrogram import Client
from telethon import TelegramClient, events

API_ID = 7554243
API_HASH = "9c2dd8b31f65db8ff63abe5b73d879de"
LOTTERY_SKANNER_GROUP_ID = -1001141596012
LOTTERY_SKANNER_GROUP = 'LotterySkanner'
METROPOLIS_ID = -1001539175416
metropolis = 'metropolisru'
client = TelegramClient('anon', API_ID, API_HASH)
brief = -1001100073584


@client.on(events.NewMessage(chats=('brief', 'vestiru24')))
async def my_event_handler(event):
    if 'розыгрыш' in event.raw_text.lower():
        await client.forward_messages(LOTTERY_SKANNER_GROUP_ID, event.message)

client.start()
client.run_until_disconnected()
