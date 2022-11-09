from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp
from aiogram import types
from aiogram.dispatcher import Dispatcher


class FSMAdmin(StatesGroup):
    name = State()
    surname = State()
    patronymic = State()
    snils = State()
    city = State()


# Начало диалога загрузки нового пункта регестрации
@dp.message_handler(commands='Регистрация', )
async def cm_start(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply('Имя:')


# первый ответ и словарь

@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Фамилия: ')


dp.message_handler(state=FSMAdmin.surname)


async def load_surname(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await FSMAdmin.next()
    await message.reply('Отчество: ')


dp.message_handler(state=FSMAdmin.patronymic)
async def load_patronymic(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text
    await FSMAdmin.next()
    await message.reply('Снилс: ')


dp.message_handler(state=FSMAdmin.snils)
async def load_snils(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['snils'] = message.text
    await FSMAdmin.next()
    await message.reply('Город проживания: ')


dp.message_handler(state=FSMAdmin.city)
async def load_сшен(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await FSMAdmin.next()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Регистрация'], state=None)
    dp.register_message_handler(load_name, content_types='name', state=FSMAdmin.name)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_surname, state=FSMAdmin.surname)
    dp.register_message_handler(load_patronymic, state=FSMAdmin.patronymic)
    dp.register_message_handler(load_snils, state=FSMAdmin.snils)
