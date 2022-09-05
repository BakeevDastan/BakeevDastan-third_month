<<<<<<< HEAD
from ast import Store
=======
<<<<<<< HEAD
from ast import Store
=======
>>>>>>> 552fb48 (all hw)
>>>>>>> 5618f37 (all hw)
from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN = config("TOKEN")
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
URL = "https://dosya-telegram-bot.herokuapp.com/"
>>>>>>> 552fb48 (all hw)
>>>>>>> 5618f37 (all hw)
ADMIN = [1259265155, ]
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
