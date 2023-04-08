import os

from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("TOKEN")  # Bot toekn
BOT_TOKEN = os.environ.get('TOKEN')  # Bot token
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
ADMINS = os.environ.get("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
