from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from config import TOKEN

import os

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)