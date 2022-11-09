from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
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


# Имя

# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Фамилия: ')


# Фамилия
# dp.message_handler(state=FSMAdmin.surname)
async def load_surname(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await FSMAdmin.next()
    await message.reply('Отчество: ')


# Отчество
# dp.message_handler(state=FSMAdmin.patronymic)
async def load_patronymic(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text
    await FSMAdmin.next()
    await message.reply('Снилс: ')


# Снилс
# dp.message_handler(state=FSMAdmin.snils)
async def load_snils(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['snils'] = message.text
    await FSMAdmin.next()
    await message.reply('Город проживания: ')


# Место проживания и выводит все данные
# dp.message_handler(state=FSMAdmin.city)
async def load_city(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


# Выход из состояния
# dp.register_message_handler(state='*', commands='отмена')
# dp.message_handler(Text(equals='отмена',ignore_case=True),state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(cm_start, commands=['Регистрация'], state=None)
    dp.register_message_handler(load_name, content_types='name', state=FSMAdmin.name)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_surname, state=FSMAdmin.surname)
    dp.register_message_handler(load_patronymic, state=FSMAdmin.patronymic)
    dp.register_message_handler(load_snils, state=FSMAdmin.snils)
    dp.register_message_handler(load_city, state=FSMAdmin.city)

