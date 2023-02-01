from handlers import dp
from aiogram import executor


async def on_start(_):
    print('Bot started')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)