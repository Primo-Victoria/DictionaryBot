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
        await bot.send_message(message.from_user.id, 'Вводите команду /translate и после нее в строку пишите слово или предложение, которые хотите перевести'
                                                     '\nВот списки словарей для перевода:'
                                                     '\n/translate_from_ru_to_eng'
                                                     '\n/translate_from_eng_to_ru')
        await message.delete()

#@dp.message_handler(commands=['Developers'])
async def develop_command(message : types.Message):
        await bot.send_message(message.from_user.id, 'Бот был разработан молодыми разработчиками из Тулы. Тимур, Лера, Даня, Вова. TulaHack2022 ')
        await message.delete()

#@dp.message_handler(commands=['translate'])
async def translate_from_eng_to_ru(message : types.Message):
    if message.text == '/Translate':
        await message.delete()
    else:
        translator = Translator(from_lang="en", to_lang="ru")
        message.text = translator.translate(message.text)
        await message.answer(message.text)

#@dp.message_handler(commands=['translate'])
async def translate_from_ru_to_eng(message : types.Message):
    if message.text == '/Translate':
        await message.delete()
    else:
        translator = Translator(from_lang="ru", to_lang="en")
        message.text = translator.translate(message.text)
        await message.answer(message.text)

@dp.message_handler(commands=['Qr'])
async def qr_code(messege: types.Message):
    await bot.send_photo(messege.from_user.id, types.InputFile('/Users/rumit/Desktop/Dictionary/qr.jpeg'))


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(how_it_works, commands=['How_it_works'])
    dp.register_message_handler(develop_command, commands=['Developers'])
    dp.register_message_handler(translate_from_ru_to_eng, commands=['translate_from_ru_to_eng'])
    dp.register_message_handler(translate_from_eng_to_ru, commands=['translate_from_eng_to_ru'])
    dp.register_message_handler(qr_code, commands=['QR_code'])

