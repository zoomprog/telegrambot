from aiogram import executor
from create_bot import dp

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


if __name__ == '__main__':
    executor.start_polling(dp)
