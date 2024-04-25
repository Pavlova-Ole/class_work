import asyncio 
 
from aiogram import Bot, Dispatcher, Router , F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup,  CallbackQuery
from aiogram.filters import Command 
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
 
bot = Bot(token="7173826357:AAFWJEthXIVu94kLaZwrQjECv2_mOjB8MPQ") 
dp = Dispatcher() 

router = Router() 
 
class Anketa(StatesGroup):
    name = State()
    age = State()
    gender = State()

@router.message(Command("anketa"))
async def anketa_handler(msg: Message, state: FSMContext):
    await state.set_state(Anketa.name)
    markup = InlineKeyboardMarkup(inline_keyboard= [[
        InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]])
    await msg.answer("Введите Ваше имя", reply_markup= markup)

@router.callback_query(F.data == 'cancel_anketa')
async def cancel_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.answer('Регистрация отменена')

@router.message(Anketa.name)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(Anketa.age)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Назад', callback_data='back_anketa'),
        InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),]])
    await msg.answer('Введите Ваш возраст', reply_markup=markup)


@router.message(Anketa.age)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext):
    try:
        await state.update_data(age=int(msg.text))
    except ValueError:
        await msg.answer('Вы не верно ввели возраст!')
        markup = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='Назад', callback_data='back_anketa'),
            InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),]])
        await msg.answer('Введите Ваш возраст', reply_markup=markup)
        return

    await state.set_state(Anketa.gender)
    markup = InlineKeyboardMarkup(inline_keyboard= [
        [ 
            InlineKeyboardButton(text='Назад', callback_data='back_anketa'),
            InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),
    ], [
        InlineKeyboardButton(text='Мужской', callback_data='gender_m'),
        InlineKeyboardButton(text='Женский', callback_data='gender_w'),
    ]])
    await msg.answer('Введите Ваш пол', reply_markup=markup)

@router.callback_query(F.data == 'back_anketa')
async def back_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == Anketa.gender:
        await state.set_state(Anketa.age)
        markup = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='Назад', callback_data='back_anketa'),
            InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),]])
        await callback_query.message.answer('Введите Ваш возраст', reply_markup=markup)

    elif current_state == Anketa.age:
        await state.set_state(Anketa.name)
        markup = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]])
        await callback_query.message.answer('Введите Ваше имя', reply_markup=markup)

@router.callback_query(F.data.startswith('gender_') and Anketa.gender)
async def set_age_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    gender = {'gender_m':'Мужской', 'gender_w':'Женский'}[callback_query.data]
    await state.update_data(gender=gender)
    await callback_query.message.answer(str(await state.get_data()))
    await state.clear()

@router.message(Anketa.gender)
async def set_age_by_anketa_handker(msg: Message, state: FSMContext):
    await msg.answer('Нужно пол выбрать кнопкой')


@router.message(Command("start")) 
async def start_handler(msg: Message): 
    await bot.set_my_commands([ 
        BotCommand(command='start', description='Запуск бота'), 
        BotCommand(command='set_time', description='Задать время рассылки'), 
        BotCommand(command='help', description='Справка'),
        BotCommand(command='anketa', description='Анкета')

    ])
    
    inline_markup = InlineKeyboardMarkup(inline_keyboard = [
            [InlineKeyboardButton(text='вперед', callback_data='next')]
            ])
    await msg.answer(text="страница 1", reply_markup=inline_markup) 
 
@router.callback_query(F.data == "next")
async def next_handler(callback_query: CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text='назад', callback_data='back')]
         ])
    
    await callback_query.message.edit_text(text="страница 2", reply_markup=inline_markup)


@router.callback_query(F.data == "back")
async def next_handler(callback_query: CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text='вперед', callback_data='next')]
         ])
    
    await callback_query.message.edit_text(text="страница 1", reply_markup=inline_markup)

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