"""используем import для asyncio """
import asyncio
from aiogram import Bot, Dispatcher
from handlers import include_routers

bot = Bot(token="7173826357:AAFWJEthXIVu94kLaZwrQjECv2_mOjB8MPQ")
dp = Dispatcher()


async def main():
    """определяем функцию"""
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
