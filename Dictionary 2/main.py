from aiogram.utils import executor
from create_bot import dp

from handlers import client, admin, other

client.register_handlers_client(dp)
#admin
other.register_handlers_other(dp)

async def on_startup(_):
    print('Бот в сети')

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)