# from pyrogram import Client
from telethon import TelegramClient, events

API_ID = 7554243
API_HASH = "9c2dd8b31f65db8ff63abe5b73d879de"
LOTTERY_SKANNER_GROUP_ID = -1001141596012
LOTTERY_SKANNER_GROUP = 'LotterySkanner'
METROPOLIS_ID = -1001539175416
METROPOLIS = 'metropolisru'
client = TelegramClient('anon', API_ID, API_HASH)
brief = -1001100073584

# @client.on(events.NewMessage)
# async def my_event_handler(event):
#     if 'hello' in event.raw_text:
#         await client.send_message(LOTTERY_SKANNER_GROUP_ID, 'Hi!')

@client.on(events.NewMessage(chats=('brief', 'LotterySkanner', 'vestiru24')))
async def my_event_handler(event):
    if 'розыгрыш' in event.raw_text.lower():
        # await client.send_message(LOTTERY_SKANNER_GROUP_ID, event.raw_text)
        await client.forward_messages(LOTTERY_SKANNER_GROUP_ID, messages=event.raw_text)

client.start()
client.run_until_disconnected()
