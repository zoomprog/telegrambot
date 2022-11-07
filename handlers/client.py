from aiogram import types, Dispatcher
from create_bot import dp, bot


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать хозяин!!!')
        await message.delete()
    except:
        await message.reply('Вы не подписаны')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
