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
