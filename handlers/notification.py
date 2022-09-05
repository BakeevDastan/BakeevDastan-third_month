import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="ok!")


async def touch():
    video = open("img/papich.mp4", "rb")
    await bot.send_video(chat_id=chat_id, video=video,
                         caption="Touch touch!")

async def wake_up():
    video = open("img/gimn.mp4", "rb")
    await bot.send_video(chat_id=chat_id, video=video,
                         caption="Слава Україні!")


async def scheduler():
    aioschedule.every().day.at("12:36").do(touch)
    aioschedule.every().day.at("12:38").do(wake_up)
    

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)