import json
import os
import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    now = datetime.datetime.now()
    await message.answer(f"<b>Hayrli kun {message.from_user.full_name}, kuningiz barakali o'tsin</b>",
                          parse_mode='HTML',
                          reply_markup=ReplyKeyboardRemove())
    print(message.from_user.id)
    print(message.from_user.username)

    # Check if the JSON file already exists
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
                'last_login_time': f'{now.day}:{now.month}:{now.year} --> {now.time()}'
            })
        else:
            # If the user is not registered, add the user data to the file
            data = {
                "telegram_id": message.from_user.id,
                "username": message.from_user.username,
                'fullname': message.from_user.full_name,
                'register_time': f'{now.day}:{now.month}:{now.year} --> {now.time()}'
            }
    else:
        # If the file doesn't exist, add the user data to a new file
        data = {
            "telegram_id": message.from_user.id,
            "username": message.from_user.username,
            'fullname': message.from_user.full_name,
            'register_time': f'{now.day}:{now.month}:{now.year} --> {now.time()}'
        }

    with open(file_name, "w") as outfile:
        json.dump(data, outfile)

    if "last_login_time" in data:
        await message.answer("Sizning ma'lumotlaringiz muvaffaqiyatli yangilandi!")
    else:
        await message.answer("Siz muvaffaqiyatli ro'yxatdan o'tdingiz!")
