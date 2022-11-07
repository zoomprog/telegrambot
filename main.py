import logging
from aiogram import Bot, Dispatcher, executor, types
import config
import os

bot = Bot(config.TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('ON')


'''***************************************Клиентскачя часть*********************************************************************'''


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать хозяин')
        await message.delete()
    except:
        await message.reply('Вы не подписаны')


'''****************************************Админская часть********************************************************************'''
'''*****************************************Общая часть*******************************************************************'''


@dp.message_handler()
async def banned_word(message: types.Message):
    text = message.text.lower()
    list(text)
    for word in config.BANNED_WORD:
        if word in text[0]:
            await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

if __name__ == '__main__':
    executor.start_polling(dp)
