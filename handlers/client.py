from aiogram import types, Dispatcher
from create_bot import bot, dp


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Запись ко врачу')
        await message.delete()
    except:
        pass


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
