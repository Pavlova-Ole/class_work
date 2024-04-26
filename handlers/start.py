from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import BotCommand, Message, CallbackQuery
from keyboards.start import *

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    from main import bot
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='set_time', description='Задать время рассылки'),
        BotCommand(command='help', description='Справка'),
        BotCommand(command='anketa', description='Анкета')])
    await msg.answer(text="страница 1", reply_markup=kb_start_next)


@router.callback_query(F.data == "next")
async def next_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text="страница 2", reply_markup=kb_start_back)


@router.callback_query(F.data == "back")
async def next_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text="страница 1", reply_markup=kb_start_next)


@router.message(Command("help"))
async def start_handler(msg: Message):
    await msg.answer(text="Крч ребята если бот лег то звонить павлОвой (+79109245056)")


@router.message(Command("set_time"))
async def start_handler(msg: Message):
    await msg.answer(text="Выберите время в формате ЧЧ:ММ для рассылки картинок")
