from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.web_app_info import WebAppInfo
import json

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot('6922972034:AAHRY5dZQ7w4pA3P0ZIn80rs9JqE3oN4FrU')
dp = Dispatcher(bot)

@dp.message_handler(commands=("start"))
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Автомобили в наличии 🚘', web_app=WebAppInfo(url='https://delightful-chebakia-2e4cca.netlify.app')))
    await message.answer('Кликайте на кнопку под сообщениями, оставляйте заявку и менеджер сообщит актуальную стоимость 🙌', reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app_handler(message: types.Message):
    admin_chat_id = 723280958 
    if message.from_user.id == admin_chat_id:
        res = json.loads(message.web_app_data.data)
        await message.answer(
            f"Клиент <a href='https://t.me/{message.from_user.username}'>{message.from_user.first_name}</a> оставил заявку на покупку автомобиля:\n"
            f"Двигатель: {res['engine']}\n"
            f"Трансмиссия: {res['transmission']}\n"
            f"Привод: {res['drive']}\n"
            f"Комплектация: {res['trim']}\n"
            f"Цвет: {res['color']}\n"
            f"VIN: {res['VIN']}\n"
            f"Цена: {res['price']}", parse_mode='HTML')
    else:
        # Игнорируем сообщения от других пользователей
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
