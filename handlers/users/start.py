import json
import os
import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    now = datetime.datetime.now()
    await message.answer(f"<b>Hayrli kun {message.from_user.full_name}, kuningiz barakali o'tsin</b>",
                         parse_mode='HTML',
                         reply_markup=ReplyKeyboardRemove())
    print(message.from_user.id)
    print(message.from_user.username)
    await bot.send_message(chat_id=ADMINS[0], text=f'🗒 User Info:\n\n'
                                                   f'- Name: {message.from_user.full_name}\n'
                                                   f'- Username: @{message.from_user.username}\n'
                                                   f'- Telegram ID: {message.from_user.id}\n')

    # Check if the JSON file already exists..
    file_name = f"_{message.from_user.full_name}_.json"
    if os.path.exists(file_name):
        with open(file_name, "r") as infile:
            data = json.load(infile)

        # Check if the user data is already present in the file
        if data.get("telegram_id") == message.from_user.id:
            # If the user is already registered, update the data in the file
            data.update({
                "username": message.from_user.username,
                'fullname': message.from_user.full_name,
                'username': f"@{message.from_user.username}",
                'last_login_time': f'{now.day}:{now.month}:{now.year} --> {now.time()}'
            })
        else:
            # If the user is not registered, add the user data to the file
            data = {
                "telegram_id": message.from_user.id,
                "username": f"@{message.from_user.username}",
                'fullname': message.from_user.full_name,
                'register_time': f'{now.day}:{now.month}:{now.year} --> {now.time()}'
            }
    else:
        # If the file doesn't exist, add the user data to a new file
        data = {
            "telegram_id": message.from_user.id,
            "username": f"@{message.from_user.username}",
            'fullname': message.from_user.full_name,
            'register_time': f'{now.day}:{now.month}:{now.year} --> {now.time()}'
        }

    with open(file_name, "w") as outfile:
        json.dump(data, outfile)

    if "last_login_time" in data:
        await message.answer("Sizning ma'lumotlaringiz muvaffaqiyatli yangilandi!")
        await message.answer("Tez kunlarda sizga yangiliklar to'g'risida ma'lumot beriladi")
    else:
        await message.answer("Siz muvaffaqiyatli ro'yxatdan o'tdingiz!")
    with open(f"_{message.from_user.full_name}_.json", "r") as infile:
        data = json.load(infile)

