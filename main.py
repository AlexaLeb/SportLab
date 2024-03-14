import asyncio
import logging
import sys
from pprint import pprint
from models import sections, sport_list, advise_sport
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from keyboard import kb, test_kb1, test_kb2, test_kb3, test_kb4
from airtable import get_data,  create_data, update_data, update_data1

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7081007147:AAFx8B6HBYQ-o88bNjJbgwPKucbo-dw1vuA"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)



async def on_startup(_):
    print('Бот был запущен')



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
    dat = get_data()
    l = []
    for i in dat:
        if i['fields'] == message.from_user.id:
            l.append(1)
    if len(l) == 0:
        create_data(str(message.from_user.id))

    await message.answer(f"Привет, {hbold(message.from_user.full_name)}! "
                         f"\nЯ пока мало чего умею, но над мной работают. "
                         f"я могу подобрать тебе секцию если ты напишешь его название или можешь пройти тестик"
                         f"по этим ответам я постараюсь подобрать тебе сам вид спорта",
                         reply_markup=kb())


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender
    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    update_data1([message.from_user.id, {'счетчик для опроса': 0}])
    try:
        if message.text.lower() == 'хочу выбрать секцию':
            await message.answer(f'тут ты должен назвать секцию. '
                                 '\n<b>Вот доступные виды спорта:</b>')
            text = ''
            sport = sport_list()
            for i in range(0, len(sport)):
                # await message.answer(str(i))
                text += f'{i+1}. {sport[i]}\n'
            await message.answer(text)
            await message.answer('Напиши название спорта:')

        elif message.text.lower() == 'хочу чтобы мне выбрали спорт':
            await message.answer("Сейчас ты пройдешь тест, который должен определить, какой спорт тебе подойдет")
            await message.answer(text='Хотел бы ты, чтобы спорт был с клюшкой / битой?', reply_markup=test_kb1())

        else:
            # Send a copy of the received message
            mas = sections(message.text.lower())
            if mas[0] != 'В нашей базе данных нет этого спорта или секции. Может быть ты написал свой запрос с ошибкой, проверь':
                await message.answer(f'Найдено секций - {len(mas)} ')
            for i in range(len(mas)):
                await message.answer(str(mas[i]))

    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Я тебя не понял, можешь уточнить свой запрос пожалуйста<b>!?</b>")


@dp.callback_query()
async def callback(callback: types.CallbackQuery):
    qust = {
        0: 'Хотел бы ты, чтобы спорт был с клюшкой / битой?',
        1: 'Спорт должен быть командный?',
        2: 'Спорт должен быть связан с борьбой?',
        3: 'Спорт должен быть с мячом?',
        4: 'Спорт должен быть с ракеткой?',
        5: 'Какая у спорта должна быт стихия? (где он проходит)',
        6: 'Какой сезонности этот спорт?',
        7: 'Ты силен физически?',
        8: 'Спорт должен быть связан с оружием?',
        9: 'Спорт может быть травмоопасный?',
        10: 'Спорт может быть дорогой?',
        11: 'Спорт должен быть популярен в России?',
        12: 'В помещении или на улице?',
        13: 'Спорт должен быть связан с животными?'
    }

    typ = {
        0: 'С клюшкой?',
        1: 'Командный?',
        2: 'Связан с борьбой?',
        3: 'С мячом?',
        4: 'Есть ракетка?',
        5: 'Стихия',
        6: 'Сезонность',
        7: 'Сильно физически активный?',
        8: 'связан с оружием?',
        9: 'травмоопасный?',
        10: 'достаточно большие финансовые вложения',
        11: 'популярный в России',
        12: 'в помещении или на улице',
        13: 'связан с животными'
    }

    if callback.data.startswith('тест'):

        local = []
        data = get_data()
        a = True
        c = 0
        while a and c < 100000:
            for i in data:
                if int(i['fields']['Name']) == int(callback.from_user.id):
                    print('нашел')
                    print(i['fields']['Name'])
                    number = i['fields']['счетчик для опроса']
                    id = i['id']
                    local.append(number)
                    local.append(id)
                    print(number)
                    a = False
                    break

                else:
                    c += 1
        if c == 100000:
            await callback.message.answer('ошибочка, попробуй перезапусить меня через /start')
        number, id = local

        if number < 13 and number != 4 and number != 5 and number != 11:
            await callback.message.edit_text(qust[number+1], reply_markup=test_kb1())
            num = number + 1
            update_data([id, {'счетчик для опроса': num, typ[number]: callback.data.split()[-1]}])
        elif number == 13:
            await callback.message.edit_text('Спасибо за прохождение теста!')
            update_data([id, {typ[number]: callback.data.split()[-1]}])
            await callback.message.answer('Подожди, я думаю какой спорт тебе подходит)')

            l = advise_sport(str(callback.from_user.id))
            text = ''
            if len(l) > 0:
                await callback.message.answer('Вам подходит:')
                for i in range(0, len(l)):
                    text += f'{i+1}. {l[i]}\n'
                await callback.message.answer(text)
                await callback.message.answer('Скопируйте и напишите мне название спорта и я предложу вам секцию')
            else:
                await callback.message.answer('Вам не подошел ни один вид спорта, попробуйте еще раз')
        elif number == 4:
            await callback.message.edit_text(qust[number+1], reply_markup=test_kb2())
            update_data([id, {'счетчик для опроса': number+1, typ[number]: callback.data.split()[-1]}])
        elif number == 5:
            await callback.message.edit_text(qust[number+1], reply_markup=test_kb3())
            update_data([id, {'счетчик для опроса': number+1, typ[number]: callback.data.split()[-1]}])
        elif number == 11:
            await callback.message.edit_text(qust[number+1], reply_markup=test_kb4())
            update_data([id, {'счетчик для опроса': number+1, typ[number]: callback.data.split()[-1]}])
        else:
            await callback.message.edit_text('КАРАУЛ ТЫ СЛОМАЛ ТЕСТ')


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    # And the run events dispatchingя
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
