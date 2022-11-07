from config import BANNED_WORD
from aiogram import types, Dispatcher
from create_bot import dp, bot


async def banned_word(message: types.Message):
    text = message.text.lower()
    list(text)
    for word in BANNED_WORD:
        if word in text[0]:
            await message.delete()

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(banned_word)
