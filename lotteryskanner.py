import re
from telethon.sync import TelegramClient, events, utils
from config import (API_HASH, API_ID, SESSION_STRING, TARGET_CHANNEL)

client = TelegramClient(SESSION_STRING, API_ID, API_HASH)

lotteryskanner = -1001569559960
brief = -1001099350027
vesti24 = -1001001872252
nezigar = -1001096463945

@client.on(events.NewMessage(chats=[lotteryskanner, brief, vesti24, nezigar]))
async def handler_new_message(event):
    try:
        if re.findall(r'розыгры', event.raw_text.lower()):
            await client.forward_messages(int(TARGET_CHANNEL), event.message)
        # elif event:
        #     chat_from = event.chat if event.chat else (await event.get_chat())
        #     chat_title = utils.get_display_name(chat_from)
        #     chat = f'Название **{chat_title}**, id: **{event.chat_id}**'
        #     await client.send_message(int(TARGET_CHANNEL), chat)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
