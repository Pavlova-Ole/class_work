from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.start import *

router = Router()


@router.message(Command("help"))
async def start_handler(msg: Message):
    await msg.answer(text="Крч ребята если бот лег то звонить павлОвой (+79109245056)")
