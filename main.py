import asyncio
import logging
import sys

from pprint import pprint
from models import shoose_sport, sections, sport_list
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import hbold
from keyboard import kb, test_kb1

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7081007147:AAFx8B6HBYQ-o88bNjJbgwPKucbo-dw1vuA"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
number = 0
async def on_startup(_):
    print('Бот был запущен')
decit = {}

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    # urlkb = InlineKeyboardMarkup(inline_keyboard=1)
    # kb = [
    #     [
    #         KeyboardButton(text='Хочу выбрать секцию'),
    #         KeyboardButton(text='Хочу чтобы мне выбрали спорт'),
    #         KeyboardButton(text='Програмист учится')
    #
    #     ]
    # ]
    # keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}! "
                         f"\nЯ пока мало чего умею, но над мной работают. "
                         f"пока я буду только тебя дразнить",
                         reply_markup=kb())



@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        if message.text.lower() == 'хочу выбрать секцию':
            await message.answer(f'тут ты должен назвать секцию. '
                                 '\n<b>Вот доступные виды спорта:</b>')
            l = []
            for i in sport_list():
                await message.answer(str(i))
            await message.answer('Напиши название спорта:')

        elif message.text.lower() == 'хочу чтобы мне выбрали спорт':
            await message.answer("Сейчас ты пройдешь тест, который должен определить, какой спорт тебе подойдет")
            await message.answer(text='Хотел бы ты, чтобы спорт был с клюшкой / битой?', reply_markup=test_kb1())


        else:
            # Send a copy of the received message
            mas = sections(message.text.lower())
            for i in range(len(mas)):
                await message.answer(str(mas[i]))

    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Ты вызвал ошибку, как ты меня смог сломать<b>!?</b>\n"
                             "но я все еще продолжаю работать")
@dp.callback_query()
async def callback(callback: types.CallbackQuery):
    global number
    qust = {
        '0': 'спорт должен быть командный?1',
        '1': 'спорт должен быть командный?2',
        '2': 'спорт должен быть командный?3',
        '3': 'спорт должен быть командный?4',
        '4': 'спорт должен быть командный?5',
        '5': 'спорт должен быть командный?6',
        '6': 'спорт должен быть командный?7',
        '7': 'спорт должен быть командный?8',
        '8': 'спорт должен быть командный?9',
        '9': 'спорт должен быть командный?10',
        '10': 'спорт должен быть командный?11',
        '11': 'спорт должен быть командный?12',
        '12': 'спорт должен быть командный?13',
        '13': 'спорт должен быть командный?14',
    }

    if callback.data.startswith('тест'):
        if number < 13:
            # quest(number)
            await callback.message.edit_text(qust[f"{number}"], reply_markup=test_kb1())
            decit[qust[f"{number}"]] = callback.data.split()[-1]
            number += 1

        else:
            number = 0
            decit.clear()
    print(decit)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    # And the run events dispatchingя
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())