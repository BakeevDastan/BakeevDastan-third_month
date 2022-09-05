from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from database import bot_db

class FSMAdmin(StatesGroup):
    photo_dish = State()
    name_dish = State()
    discr_dish = State()
    price_dish = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.photo_dish.set()
        await message.answer(f"Регистрация началась " 
        f"Отправьте фото блюда")
    else:
        await message.reply("Пишите в личку")



async def load_photo(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Напишите назване блюда")


async def load_name(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Напишите описание блюда")

async def load_disc(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['disc'] = message.text
    await FSMAdmin.next()
    await message.answer("Напишите стоимость блюда")


async def load_price(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = int(message.text)
        await bot.send_photo(message.from_user.id, data['photo'],
                            caption=f"Dish name: {data['name']}\n"
                                    f"Discription of the dish: {data['disc']}\n"
                                    f"Price of the dish: {data['price']} $")
    await bot_db.sql_command_insert(state)
    await state.finish()
    await message.answer("Регистрация закончилась, выше вы видите ваши данные)")


async def delete_data(message: types.Message):
    users = await bot_db.sql_command_all()
    for user in users:
        await bot.send_photo(message.from_user.id,
                             user[0],
                             caption=f"Блюдо: {user[1]}\n"
                                     f"Описание: {user[2]}\n"
                                     f"Цена: {user[3]}\n",
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(
                                     f"delete {user[1]}",
                                     callback_data=f"delete {user[1]}"
                                 )
                             ))


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Ваше меню удалено из базы данных",  show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


async def cancel_registration(message:types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Вы остановили регистрацию ")

def register_handlers_fsmmenu(dp:Dispatcher):
    dp.register_message_handler(cancel_registration, state="*", commands='cancel')
    dp.register_message_handler(cancel_registration,
                                Text(equals="cancel", ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=['start'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo_dish,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name_dish)
    dp.register_message_handler(load_disc, state=FSMAdmin.discr_dish)
    dp.register_message_handler(load_price, state=FSMAdmin.price_dish)
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete ")
    )