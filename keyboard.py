from aiogram.types import ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def kb():
    kb = [
        [
            KeyboardButton(text='Хочу выбрать секцию'),
            KeyboardButton(text='Хочу чтобы мне выбрали спорт')
        ]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def test_kb1():
    kb = [
        [
            InlineKeyboardButton(text="да", callback_data='тест да'),
            InlineKeyboardButton(text="нет", callback_data='тест нет')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def test_kb2():
    kb = [
        [
            InlineKeyboardButton(text="земля", callback_data='тест земля'),
            InlineKeyboardButton(text="горы", callback_data='тест горы'),
            InlineKeyboardButton(text="вода", callback_data='тест вода'),
            InlineKeyboardButton(text="воздух", callback_data='тест воздух')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def test_kb3():
    kb = [
        [
            InlineKeyboardButton(text="зима", callback_data='тест зима'),
            InlineKeyboardButton(text="лето", callback_data='тест лето')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def test_kb4():
    kb = [
        [
            InlineKeyboardButton(text="помещение", callback_data='тест помещение'),
            InlineKeyboardButton(text="улица", callback_data='тест улица')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard
