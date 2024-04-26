from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_anketa=InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Отмена', 
            callback_data='cancel_anketa')]])
kb_start = InlineKeyboardMarkup(inline_keyboard= [
    [
        InlineKeyboardButton(
            text = 'Вперед',
            callback_data='next')]])