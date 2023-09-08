"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import logging

from environs import Env
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem


logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def get_constellation(update, context):
    planet_name = update.message.text.split()[1]
    planet = getattr(ephem, planet_name)()
    planet.compute()
    constellation = ephem.constellation(planet)
    update.message.reply_text(
        f'{planet_name} is currently in the constellation of '
        f'{constellation[1]}'
    )


def main():
    env = Env()
    env.read_env()

    bot = Updater(env('TG_BOT_TOKEN'), use_context=True)

    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
