from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import config


bot = Bot(config.TOKEN_API)
dp = Dispatcher(bot)
