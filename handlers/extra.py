from aiogram import types, Dispatcher
from config import bot, ADMIN
import random 

async def echo(message: types.Message):
    if message.text.startswith("game") and message.from_user.id in ADMIN:
        emoji_lst = ['⚽️', '🏀','🎲', '🎯', '🎳' '🎰']
        random_emoji = random.choice(emoji_lst)
        await bot.send_dice(message.chat.id, emoji=random_emoji)
    elif message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text) * 2)
    else:
        await bot.send_message(message.chat.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)