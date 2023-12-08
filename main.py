from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6922972034:AAHRY5dZQ7w4pA3P0ZIn80rs9JqE3oN4FrU')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть', web_app=WebAppInfo(url='https://delightful-chebakia-2e4cca.netlify.app')))
    await message.answer('Привет', reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
