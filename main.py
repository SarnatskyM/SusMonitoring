from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from keyboards.keyboard import *
from config.config import TOKEN, admins
from helper.status import *
import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#start func
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    if message.from_user.id in admins:
        getStatus()
        await message.answer(f"Здравствуй, {hbold(message.from_user.full_name)}.\nВаша роль - Администратор", reply_markup=start_keyboard, parse_mode="HTML")
        await message.answer("Выберите действие")
        await message.answer_sticker("https://chpic.su/_data/stickers/m/menhera_anime/menhera_anime_006.webp?v=1693440002", "rb")
    else:
        await message.answer(f"Я не понимаю кто вы?")
        await message.answer_sticker("https://chpic.su/_data/stickers/m/menhera_anime/menhera_anime_027.webp?v=1693440002", "rb")

# Main func keyboard 
@dp.message_handler(Text(equals=["🟢Статус бд"]))
async def btn_status(message: types.Message):
    if message.from_user.id in admins:
        status = getStatus()
        if status != 500:
            statusCard = f"🟢<b><i>Статус бд</i></b>\n{'-'*35}\n" \
                        f"Статус бд - {status['is_active']}\n" \
                        f"Количество операций - {status['operations']}\n" \
                        f"Количество ошибок - {status['rollbacks']}\n" \
                        f"Процент соединений в статусе ожидание - {status['idle_conns']}\n" \
                        f"Сред время ожидания - {status['mean_response_time']}\n" \
                        f"Disk usage - {status['disk_usage']}\n" \
                        f"Disk usage percantage - {status['disk_usage_percantage']}\n" \
                        f"Max operation duration - {status['max_operation_duration']}\n{'-'*35}\n\n" \
                        f"<b><i>Текущие подключения [{status['conns_num']}]:</i></b>\n"
            for conn in status['conns']:
                statusCard += f"<b>• last_query</b> - {conn['last_query']}\n" \
                              f"<b>• query_start</b> - {conn['query_start']}\n" \
                              f"<b>• pid</b> - {conn['pid']}\n{'*'*35}\n\n"
            await message.answer(statusCard, parse_mode="HTML")
        else:
            await message.answer("Ошибка при доступе к бэкенду")

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
@dp.message_handler(Text(equals=["🛠Перезапустить бд"]))
async def btn_reloadbd(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Подождите пару секунд.....")
        await message.answer_sticker("https://chpic.su/_data/stickers/m/menhera_anime/menhera_anime_045.webp?v=1693440002", "rb")
        

@dp.message_handler(Text(equals=["🚨Оборвать соединение"]))
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

async def checkStatus():
    while True:
        response = getStatus()
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Отказаться", callback_data="fail"))
        if response != 500:
            for user_id in admins:
                for alert in response['allerts']:
                    alertCard = f"<b>[{alert['data'] if alert['data'] else ''}] {alert['description']}</b> " \
                                f"\n\nТип ошибки - {alert['type'] if alert['type'] else 'Неизвестен'}"
                    if alert['type'] == 3:
                        kbbk = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Оборвать соединение', callback_data=f'pid:{alert["data"]}'))
                        await bot.send_message(user_id, alertCard, parse_mode='HTML', reply_markup=kbbk)
                    else:
                        await bot.send_message(user_id, alertCard, parse_mode='HTML')
        else:
            await bot.send_message(user_id, "Ошибка при доступе к бэкенду")
        
        await asyncio.sleep(30)


@dp.callback_query_handler(text_contains="pid:")
async def inline_kb_answer_callback_handler(call: types.CallbackQuery):
   pid = call.data.split(":")[1]
   response = disconnectCon(pid)
   if response == 500:
       await call.answer("Не удалось оборвать соединение")
   elif response:
       await call.answer("Соединение оборвано")
   else:
       await call.answer(f"<b><i>{response['data']['data']} - [{response['data']['type']}</b></i>\n{response['data']['description']}")
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(checkStatus())
    executor.start_polling(dp, loop=loop, skip_updates=True)