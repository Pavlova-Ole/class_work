"""используем import для asyncio """
import asyncio
from aiogram import Bot, Dispatcher
from handlers import include_routers
from datetime import time, timedelta, datetime
from models import User

bot = Bot(token="7173826357:AAFWJEthXIVu94kLaZwrQjECv2_mOjB8MPQ")
dp = Dispatcher()
    

async def get_time_notify():
    now = datetime.now()
    users = User.filter(User.time > now).order_by(User.time.asc())
    if users.count() > 0:
        return (users.first()).time 

async def send_admin():
    global SEND_TIME
    SEND_TIME = await get_time_notify()
    await bot.send_message(976297325, "Бот запущен!")
    while True:
        print(datetime.now().time(), SEND_TIME)
        now_time = datetime.now().time()
        now_time = time(now_time.hour, now_time.minute)
        if SEND_TIME and SEND_TIME == now_time:
            # рассылка уведомлений всем пользователям
            for user in User.filter(time=SEND_TIME):
                await bot.send_message(user.tg_user, 'чири чири')

            SEND_TIME = await get_time_notify()
            print(SEND_TIME)   

               
        now_time = (datetime.now() + timedelta(minutes=1))
        now_time = datetime(now_time.year, now_time.month, now_time.day, 
                            now_time.hour, now_time.minute)
        seconds = (now_time - datetime.now()).seconds + 1
        print(datetime.now().time(), now_time.time(), seconds)
        await asyncio.sleep(seconds)

async def on_startup():
    asyncio.create_task(send_admin())

async def main():
    '''Старт бота'''
    dp.startup.register(send_admin)
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
