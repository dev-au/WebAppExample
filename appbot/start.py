from aiogram import types, F, filters
from config import dp
from loader import WEBHOOK_URL, WEBAPP_URL

answer_web_app_keyboard = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text='Avtorizatsiya', web_app=types.WebAppInfo(url=WEBHOOK_URL + WEBAPP_URL))
        ]
    ]
)


@dp.message(filters.CommandStart())
async def command_start(message: types.Message):
    await message.answer('Assalomu alaykum', reply_markup=answer_web_app_keyboard)