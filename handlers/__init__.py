"""используем from для импорта aiogram """
from aiogram import Dispatcher
from handlers import anketa, start


def include_routers(dp: Dispatcher):
    """мы используем def для определения функции"""
    dp.include_routers(
        start.router,
        anketa.router
    )
