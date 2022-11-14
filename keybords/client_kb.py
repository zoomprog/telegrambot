from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

prdusts_cb = CallbackData('product', 'id', 'action')

btnStart = KeyboardButton("Start")
btnReg = KeyboardButton("Регистрация")
btnInf = KeyboardButton("Об проекте")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(btnStart).add(btnReg).add(btnInf)


def get_start_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Мои данные', callback_data='get_all_products')],
        [InlineKeyboardButton('Добавить новые данные', callback_data='add_new_product')]
    ])
    return ikb
