from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.start import *

router = Router()


@router.message(Command("set_time"))
async def start_handler(msg: Message):
    await msg.answer(text="Выберите время в формате ЧЧ:ММ для рассылки картинок")
