from aiogram.utils import executor
from database import bot_db
import asyncio
from distutils.command.config import config
from aiogram.utils import executor
from config import dp, URL, bot
import logging
from handlers import client, callback, extra,fsm_menu, admin , notification , inline
from decouple import config


async def on_startup(_):
    await bot.set_webhook(URL)
    asyncio.create_task(notification.scheduler())
    bot_db.create_sql()


async def on_shutdown(dp):
    await bot.delete_webhook()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_menu.register_handlers_fsmmenu(dp)
notification.register_handlers_notification(dp)
inline.register_handlers_inline(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_shutdown=on_shutdown,
        on_startup=on_startup,
        skip_updates=True,
        host='0.0.0.0',
        port=config("PORT", cast=int)
    )
