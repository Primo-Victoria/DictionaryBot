from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client

from translate import Translator

#Базовые команды для бота
#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Напишите слово или предложение и я вам его переведу!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Для подключения бота, напишите ему: \nhttps://t.me/tul_trans_bot')

#@dp.message_handler(commands=['How_it_works'])
async def how_it_works(message : types.Message):
        await bot.send_message(message.from_user.id, 'You can enter you a word or sentence and bot translate it')
        await message.delete()

#@dp.message_handler(commands=['Developers'])
async def develop_command(message : types.Message):
        await bot.send_message(message.from_user.id, 'Бот был разработан молодыми разработчиками из Тулы. Тимур, Лера, Даня, Вова. TulaHack2022 ')
        await message.delete()

#@dp.message_handler(commands=['translate'])
async def text_translate_new(user : types.Message):
    translator = Translator(from_lang="en", to_lang="ru")
    user.text = translator.translate(user.text)
    message.answer(user.text)
async def text_translate(message : types.Message):
    await bot.send_message(message.from_user.id, 'Введите слово или предложение')
    await message.delete()

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(how_it_works, commands=['How_it_works'])
    dp.register_message_handler(develop_command, commands=['Developers'])
    dp.register_message_handler(text_translate, commands=['translate'])
