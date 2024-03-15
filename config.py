from aiogram.fsm.storage.memory import MemoryStorage
from fastapi.templating import Jinja2Templates

from loader import *
from aiogram import Dispatcher, Bot

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

local_storage = MemoryStorage()
dp = Dispatcher(storage=local_storage)

template = Jinja2Templates('templates')
