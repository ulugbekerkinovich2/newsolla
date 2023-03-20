import asyncio
import datetime

from data.config import ADMINS
from loader import bot


async def my_func():
    now = datetime.datetime.now()
    print(now.weekday())

    if now.weekday() == 0 and now.hour == 9 and now.minute == 55:
        await bot.send_message(chat_id=ADMINS, text={now.hour+5, now.minute})
        chat_id = 935920479
        name = 'Ulugbek'
        link = 'https://www.youtube.com/watch?v=jSfbVGb6lnw&list=RDMMjSfbVGb6lnw&start_radio=1'
        await bot.send_message(chat_id=chat_id, text=f'{name} uchun link {link}')


async def main():
    while True:
        # now = datetime.datetime.now()
        # await bot.send_message(chat_id=ADMINS, text=f'{now.hour+5, now.minute}  ok')
        await my_func()
        await asyncio.sleep(59)  # sleep for 1 minute


if __name__ == '__main__':
    asyncio.run(main())