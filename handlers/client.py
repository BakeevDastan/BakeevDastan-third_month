from re import L
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from database.bot_db import sql_command_random
from parser.security import parser

async def first_quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Next quiz", callback_data='button_call_1')
    markup.add(button_call_1)
    question = "Кто умер в трилогии Толкина ' Властелин колец Братсвтво кольца'"
    answer = [
        "Фарамир",
        "Боромир",
        "Гэндальф",
        "Голум (Смегол)"
    ]
    await bot.send_poll(
    chat_id = message.chat.id,
    question=question,
    options=answer,
    is_anonymous=False,
    type='quiz',
    correct_option_id=1,
    explanation="Надо знать такие моменты из фильма))",
    reply_markup=markup
    )


async def show_meme(message: types.Message):
    photo = open("img\img.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, 'Это должно ответом на сообщение')


async def show_random_user(message: types.Message):
    await sql_command_random(message)


async def news_parser(message:types.Message):
    news = parser()
    for i in news:
        await bot.send_message(
            message.from_user.id,
            f"#{i['Time and year']}\n\n"
            f"{i['Title']}\n"
            f"{i['Description']}\n"
            f"{i['Link']}\n"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(first_quiz, commands=['quiz'])
    dp.register_message_handler(show_meme, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(show_random_user, commands=['get'])
    dp.register_message_handler(news_parser, commands=['parser'])