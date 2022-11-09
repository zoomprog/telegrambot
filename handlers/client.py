from aiogram import types, Dispatcher
from create_bot import bot, dp
from keybords import kb_client


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Запись ко врачу', reply_markup=kb_client)


async def bot_message(message: types.Message):
    if message.text == 'Регистрация':
        await bot.send_message(message.from_user.id, '/Регистрация')
    elif message.text == 'Об проекте':
        await bot.send_message(message.from_user.id,
                               'Мой проект берет ваши данные и переносит на медицинский сайт, чтобы записать вас ко врачу и потом, вы уже получаете уведомление о записи')
    elif message.text == 'Start':
        await bot.send_message(message.from_user.id, '/start')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(bot_message)
