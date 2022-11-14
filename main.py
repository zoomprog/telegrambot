from aiogram import executor
from create_bot import dp
import db


from handlers import client, admin, other


async def on_startup(_):
    await db.db_connect()
    print("Подключено к бд")


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
