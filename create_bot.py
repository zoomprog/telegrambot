from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(config.TOKEN_API)
dp = Dispatcher(bot, storage=storage)
