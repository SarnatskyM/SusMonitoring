from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#keyboard in start
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🟢Статус бд"),
            KeyboardButton(text="🔴Текущие ошибки"),
        ],
        [
            KeyboardButton(text="⚙Настройки")
        ]
    ],
    resize_keyboard=True
)
# keyboard in settings
fix_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚨Оборвать соединение"),
            KeyboardButton(text="🗑Отчистить мусор")
        ],
        [
            KeyboardButton(text="🛠Перезапустить бд и восстановить с контрольной точки")
        ],
        [
            KeyboardButton(text="← Назад")
        ]
    ],
    resize_keyboard=True
)



