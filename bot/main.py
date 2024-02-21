import asyncio
import json

from aiogram import Bot, Dispatcher, types
import aiogram
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold


from config import token as TOKEN
from config import start_message as START
from config import bot_message
from config import incorrect_messages
from random import choice
import logging
import sys

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(START)
    await message.answer(bot_message)


@dp.message()
async def text_handler(message: types.Message) -> None:
    try:
        if message.text.lower() == 'кодировка подошла':
            text = '''отлично, держи код '5JzxOEmn6e' тебе это понадобится при регистрации на сайте.

если ты проходишь соревнования очно, то тебе на сайт https://offline.vsuet-ctf.ru
в ином случае, https://online.vsuet-ctf.ru
            
регистрация откроется в понедельник. удачи, молодой боец!'''
            with open('./data/users.json', 'r') as file:
                data = json.load(file)
                data.append(message.from_user.id)
                
            with open('./data/users.json', 'w') as file:
                json.dump(data, file)
        else:
            text = choice(incorrect_messages)
    except TypeError:
        text = 'nice try!'
    await message.answer(text)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
