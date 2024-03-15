from aiogram.types import MenuButtonWebApp, WebAppInfo, Update
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from config import bot, dp

from loader import *
from setup import load_project

app = FastAPI()


@app.on_event('startup')
async def start_project():
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text='Auth', web_app=WebAppInfo(url=WEBHOOK_URL + WEBAPP_URL)))
    await bot.set_webhook(url=WEBHOOK_URL + WEBHOOK_PATH)
    await bot.send_message(BOT_ADMIN, 'I am running')


@app.post(WEBHOOK_PATH)
async def bot_webhook(data: dict):
    update = Update(**data)
    await dp.feed_update(bot, update)


app.include_router(load_project.auth_router)

app.mount("/static", StaticFiles(directory="static"), name="static")