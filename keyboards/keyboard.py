from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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

fix_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗘Перезапустить бд"),
            KeyboardButton(text="🛇Оборвать соединение"),
            KeyboardButton(text="🗑Отчистить мусор")
        ],
        [
            KeyboardButton(text="Восстановление с контрольной точки")
        ],
        [
            KeyboardButton(text="← Назад")
        ]
    ],
    resize_keyboard=True
)


