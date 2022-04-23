from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN

import os

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Напишите слово или предложение и я вам его переведу!')
        await message.delete()
    except:
        await message.reply('Для подключения бота, напишите ему: \nhttps://t.me/tul_trans_bot')

@dp.message_handler(commands=['How_it_works?'])
async def command_start(message : types.Message):
        await bot.send_message(message.from_user.id, 'You can enter you a word or sentence and bot translate it')
        await message.delete()

@dp.message_handler(commands=[''])
async def command_start(message : types.Message):
        await bot.send_message(message.from_user.id, 'You can enter you a word or sentence and bot translate it')
        await message.delete()

@dp.message_handler()
async def echo_send(message : types.Message):
    #await message.answer(message.text)
    await message.reply(message.text)
    #await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)