from ast import Store
from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN = config("TOKEN")
URL = "https://dosya-telegram-bot.herokuapp.com/"
ADMIN = [1259265155, ]
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
