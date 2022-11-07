from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

btnMain = KeyboardButton('Главное меню')
btnStart = KeyboardButton("Start")
btnReg = KeyboardButton("Регистрация")
btnInf = KeyboardButton("Об проекте")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(btnStart).add(btnReg).add(btnInf)
