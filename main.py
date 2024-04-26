import asyncio 
 
from aiogram import Bot, Dispatcher, Router , F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup,  CallbackQuery
from aiogram.filters import Command 
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
 
bot = Bot(token="7173826357:AAFWJEthXIVu94kLaZwrQjECv2_mOjB8MPQ") 
dp = Dispatcher() 

router = Router() 
 






    
    inline_markup = InlineKeyboardMarkup(inline_keyboard = [
            [InlineKeyboardButton(text='вперед', callback_data='next')]
            ])
    
 





@router.callback_query()
async def callback_query_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(text=callback_query.data)


@router.message(Command("help")) 
async def start_handler(msg: Message): 
    await msg.answer(text="Крч ребята если бот лег то звонить павлОвой (+79109245056)") 
 
@router.message(Command("set_time")) 
async def start_handler(msg: Message): 
    await msg.answer(text="Выберите время в формате ЧЧ:ММ для рассылки картинок") 

async def main(): 
    await dp.start_polling(bot) 
 
dp.include_routers(router) 
 
if __name__ == '__main__': 
    asyncio.run(main())