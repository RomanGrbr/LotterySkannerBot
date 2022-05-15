import re

from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, PeerChannel

from config import API_HASH, API_ID, SESSION_STRING, TARGET_CHANNEL
from dbhelper import DBHelper

client = TelegramClient(SESSION_STRING, API_ID, API_HASH)
client.connect()
db = DBHelper()
db.setup()

async def channel_update():
    id_list = db.get_items()
    for i in id_list:
        db.delete_item(i)
    
    get_dialogs = GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=30,
        hash=0
    )

    dialogs = client(get_dialogs)
    for d in dialogs.dialogs:
        peer = d.peer
        if isinstance(peer, PeerChannel):
            id = peer.channel_id
            db.add_item(id)


channel_update()
print(db.get_items())

# my_channel = set()
# get_dialogs = GetDialogsRequest(
#     offset_date=None,
#     offset_id=0,
#     offset_peer=InputPeerEmpty(),
#     limit=30,
#     hash=0
# )

# dialogs = client(get_dialogs)
# for d in dialogs.dialogs:
#     peer = d.peer
#     if isinstance(peer, PeerChannel):
#         id = peer.channel_id
#         my_channel.add(id)
# print(my_channel)

@client.on(events.NewMessage(chats=db.get_items()))
async def handler_new_message(event):
    try:
        if re.findall(r'розыгры', event.raw_text.lower()) or (
            re.findall(r'конкурс', event.raw_text.lower())):
            await client.forward_messages(int(TARGET_CHANNEL), event.message)
    except Exception as e:
        print(e)

@client.on(events.NewMessage(chats=int(TARGET_CHANNEL)))
async def handler(event):
    if event.raw_text.lower() == '/channel':
        channel_update()
        await client.send_message(int(TARGET_CHANNEL), 'channel update')


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
