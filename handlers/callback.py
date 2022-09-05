from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def second_quiz(call: types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Next quiz", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Любимая мышка Папича"
    answer = [
        "Genius NetScroll 120",
        "Roccat Burst Core",
        "Razer Viper 8K",
        "SteelSeries Rival 5"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Легкая легчайшая, для кого ? Для ВЕЛИЧАЙШЕГО",
        reply_markup=markup
    )
async def thid_quiz(call: types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Next quiz", callback_data='button_call_3')
    markup.add(button_call_3)

    question = "На каком героее EvilArthas апнул 7к"
    answer = [
        "Slark",
        "Wraith King",
        "Luna",
        "Legion Comander"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Легкая легчайшая, для кого ? Для ВЕЛИЧАЙШЕГО",
        reply_markup=markup
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(second_quiz, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(thid_quiz, lambda call: call.data == "button_call_2")