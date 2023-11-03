from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from keyboards.keyboard import *
from lang.ru import *
from config.config import TOKEN, admins

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#start func
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    if message.from_user.id in admins:
        await message.answer(ru_text['hello'], reply_markup=start_keyboard, parse_mode="HTML")
        await message.answer("Выберите действие")
        await message.answer_sticker("https://chpic.su/_data/stickers/m/menhera_anime/menhera_anime_006.webp?v=1693440002", "rb")
    else:
        await message.answer(f"Я не понимаю кто вы?")
        await message.answer_sticker("https://chpic.su/_data/stickers/m/menhera_anime/menhera_anime_027.webp?v=1693440002", "rb")

# Main func keyboard 
@dp.message_handler(Text(equals=["🟢Статус бд"]))
async def btn_status(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Статус бд")

@dp.message_handler(Text(equals=["🔴Текущие ошибки"]))
async def bts_errors(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Текущее ошибки")
# ---------------------------


# for keyboard rotations
@dp.message_handler(Text(equals=["⚙Настройки"]))
async def btn_settings(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Текущие настройки", reply_markup=fix_keyboard)

@dp.message_handler(Text(equals=["← Назад"]))
async def btn_back(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Выберите действие", reply_markup=start_keyboard)
# ---------------------------


# Fixing func keyboard 
@dp.message_handler(Text(equals=["🗘Перезапустить бд"]))
async def btn_reloadbd(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Подождите пару секунд.....")
        await message.answer_sticker("https://chpic.su/_data/stickers/m/menhera_anime/menhera_anime_045.webp?v=1693440002", "rb")
        

@dp.message_handler(Text(equals=["🛇Оборвать соединение"]))
async def btn_disconnect(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Подождите пару секунд.....")
        await message.answer_sticker("https://chpic.su/_data/stickers/m/menhera_anime/menhera_anime_045.webp?v=1693440002", "rb")

@dp.message_handler(Text(equals=["🗑Отчистить мусор"]))
async def btn_clear(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Подождите пару секунд.....")
        await message.answer_sticker("https://chpic.su/_data/stickers/m/menhera_anime/menhera_anime_045.webp?v=1693440002", "rb")

@dp.message_handler(Text(equals=["Восстановление с контрольной точки"]))
async def btn_recovery(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Подождите пару секунд.....")
        await message.answer_sticker("https://chpic.su/_data/stickers/m/menhera_anime/menhera_anime_045.webp?v=1693440002", "rb")
# ---------------------------
    
if __name__ == "__main__":
    executor.start_polling(dp)