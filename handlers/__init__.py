"""используем from для импорта aiogram """
from aiogram import Dispatcher
from handlers import anketa, start


def include_routers(dp: Dispatcher):
    """определяем функцию"""
    dp.include_routers(
        start.router,
        anketa.router
    )
