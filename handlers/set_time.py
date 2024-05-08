"""используем from для импорта aiogram """
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import BotCommand, Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from set_time import SetTime
from models import User
router = Router()

@router.message(Command("set_time"))
async def set_time_handler(msg: Message, state: FSMContext):
    """мы используем async def для определения функции""" 
    await msg.answer(text="Выберите время в формате чч:мм для рассылки картинок")
    await state.set_state(SetTime.time)

@router.message(SetTime.time)
async def set_time_by_notification_handler(msg: Message, state: FSMContext):
    """мы используем async def для определения функции"""
    await state.clear()