"""используем from для импорта aiogram """
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import BotCommand, Message, CallbackQuery
from keyboards.start import kb_start_next, kb_start_back
from models import User
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    """мы используем async def для определения функции""" 
    await msg.bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='set_time', description='Задать время рассылки'),
        BotCommand(command='help', description='Справка'),
        BotCommand(command='anketa', description='Анкета')])
    #user = User.get_or_create(tg_user=msg.)
    await msg.answer(text="страница 1", reply_markup=kb_start_next)


@router.callback_query(F.data == "next")
async def next_handler(callback_query: CallbackQuery):
    """мы используем async def для определения функции"""
    await callback_query.message.edit_text(text="страница 2",
                                           reply_markup=kb_start_back)


@router.callback_query(F.data == "back")
async def back_handler(callback_query: CallbackQuery):
    """мы используем async def для определения функции"""
    await callback_query.message.edit_text(text="страница 1",
                                           reply_markup=kb_start_next)

@router.message(Command("help"))
async def start_first_handler(msg: Message):
    """мы используем async def для определения функции"""
    await msg.answer(text="Крч ребята если бот лег то звонить павлОвой (+79109245056)")


