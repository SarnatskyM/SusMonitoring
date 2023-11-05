from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

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
            KeyboardButton(text="🚨Разорвать соединение"),
            KeyboardButton(text="🗑Вынести мусор"),
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

get_table = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="some-ints"),
            KeyboardButton(text="some-text"),
            KeyboardButton(text="int2text"),
        ],
    ],
    resize_keyboard=True
)


get_type = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="standart"),
            KeyboardButton(text="full"),
        ],
    ],
    resize_keyboard=True
)



