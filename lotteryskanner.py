import re

from telethon.sync import TelegramClient, events

from config import API_HASH, API_ID, SESSION_STRING, TARGET_CHANNEL

client = TelegramClient(SESSION_STRING, API_ID, API_HASH)
client.connect()

my_channel = set()

async def get_dialog():
    async for dialog in client.iter_dialogs():
        if str(dialog.id).startswith('-100'):
            my_channel.add(dialog.id)
            print(dialog.name)


@client.on(events.NewMessage(chats=my_channel))
async def handler_new_message(event):
    try:
        if re.findall(r'розыгр', event.raw_text.lower()) or (
            re.findall(r'конкурс', event.raw_text.lower())) or (
            re.findall(r'дарим', event.raw_text.lower())) or (
            re.findall(r'выиграть', event.raw_text.lower())):
            await client.forward_messages(int(TARGET_CHANNEL), event.message)
    except Exception as e:
        print(e)

@client.on(events.NewMessage(chats=int(TARGET_CHANNEL)))
async def handler_commads(event):
    try:
        if event.raw_text == '/update':
            await get_dialog()
            await client.send_message(int(TARGET_CHANNEL), f'my_channel update {str(my_channel)}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    client.start()
    client.loop.run_until_complete(get_dialog())
    client.run_until_disconnected()
