# from telethon import events
# from telethon.tl.custom import Message
# from IDSkannerBot import bot

# @bot.on(events.ChatAction())
# async def on_join(event: events.ChatAction.Event):
#     if event.is_group and event.user_added and event.user_id == bot.me.id:
#         await bot.send_message(event.chat.id, 'Приветствую, господа!')


# @bot.on(events.ChatAction(func=lambda e: e.is_group and e.user_added and e.user_id == bot.me.id))
# async def on_join(event: events.ChatAction.Event):
#     await event.respond('Приветствую, господа!')


# @bot.on(events.NewMessage(func=lambda e: e.text.lower() == 'ты кто?'))
# async def who_are_you(event: Message):
#     await event.respond('Я умный, красивый, в меру упитанный мужчина в полном расцвете сил!')
