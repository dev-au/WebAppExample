from fastapi import APIRouter, Form
from starlette.requests import Request
from aiogram.utils.web_app import check_webapp_signature, parse_webapp_init_data
from aiogram.utils import formatting
from config import template, bot
from loader import WEBAPP_URL

auth_router = APIRouter(prefix=WEBAPP_URL)


@auth_router.get('/')
async def authorization_page(request: Request):
    return template.TemplateResponse(request, name='signup.html')


@auth_router.post('/signup')
async def signup_user(request: Request, username: str = Form(...), email: str = Form(...), postcode: str = Form(...),
                      password: str = Form(...), auth: str = Form(...)):
    user_data = parse_webapp_init_data(auth)
    signup_data = formatting.Text(f"Siz muvaffaqiyatli ro'yxatdan o'tdingiz:\n"
                                  f"Username: {username}\n"
                                  f"Email: {email}\n"
                                  f"Postcode: {postcode}\n"
                                  f"Parol: ", formatting.Spoiler(password))
    await bot.send_message(chat_id=user_data.user.id, **signup_data.as_kwargs())
    return template.TemplateResponse(request, name='success.html')