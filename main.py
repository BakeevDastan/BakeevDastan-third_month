<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5618f37 (all hw)
from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra,fsm_menu, admin , notification
from database import bot_db
import asyncio



async def on_startup(_):
<<<<<<< HEAD
=======
=======
from distutils.command.config import config
from aiogram.utils import executor
from config import dp, URL, bot
import logging
from handlers import client, callback, extra,fsm_menu, admin , notification , inline
from database import bot_db
import asyncio
from decouple import config

async def on_startup(_):
    await bot.set_webhook(URL)
>>>>>>> 552fb48 (all hw)
>>>>>>> 5618f37 (all hw)
    asyncio.create_task(notification.scheduler())
    bot_db.create_sql()


<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
async def on_shutdown(dp):
    await bot.delete_webhook()

>>>>>>> 552fb48 (all hw)
>>>>>>> 5618f37 (all hw)

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_menu.register_handlers_fsmmenu(dp)
notification.register_handlers_notification(dp)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
inline.register_handlers_inline(dp)

>>>>>>> 552fb48 (all hw)
>>>>>>> 5618f37 (all hw)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
<<<<<<< HEAD
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
=======
<<<<<<< HEAD
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
=======
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_shutdown=on_shutdown,
        on_startup=on_startup,
        skip_updates=True,
        host='0.0.0.0',
        port=config("PORT", cast=int)
    )
>>>>>>> 552fb48 (all hw)
>>>>>>> 5618f37 (all hw)
