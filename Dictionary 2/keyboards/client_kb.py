from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/How_it_works')
b2 = KeyboardButton('/Developers')
b3 = KeyboardButton('/Translate')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3)