import logging
import os
import datetime
import signal

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


TOKEN = os.environ.get('BOT_TOKEN')
NAME = os.environ.get('BOT_NAME')
PORT = os.environ.get('BOT_PORT')


def get_birth_days():
    curr_date = datetime.datetime.now()
    persons = {}
    with open('dates.csv', 'r') as f:
        for s in f:
            arr = s.split(',')
            birth_date = arr[-1].split(';')[0].split('.')
            if int(birth_date[0]) == int(curr_date.day) and int(birth_date[1]) == int(curr_date.month):
                if len(birth_date) == 3:
                    persons[' '.join(
                        arr[0:3])] = f'{int(curr_date.year) - int(birth_date[-1])} летие.'
                else:
                    persons[' '.join(arr[0:3])] = '.'.join(birth_date)

    message = 'Сегодня никаких дней рождений.'
    if len(persons) != 0:
        message = f'На {curr_date.day}.{curr_date.month}.{curr_date.year} дни рождения празднуют:\n' + \
            f'\n'.join([f'{key}: {value}' for key, value in persons.items()])

    return message


def callback_alarm(context: CallbackContext):
    context.bot.send_message(
        chat_id=context.job.context, text=get_birth_days())


def start(update: telegram.Update, context: CallbackContext):
    msg = 'Привет! Я буду каждый день присылать тебе напоминания о днях \
        рождения. Главное вовремя обновлять список.'
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)
    print('Message on -', update.message.chat_id)
    context.job_queue.run_daily(callback_alarm, datetime.time(
        hour=23, minute=30), context=update.message.chat_id)


def day(update: telegram.Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.message.chat_id, text=get_birth_days())


if __name__ == "__main__":
    print(f"Bot {NAME}({TOKEN[:3]}..{TOKEN[-3:]}) started on {PORT} port")
    u = Updater(TOKEN, use_context=True)
    j = u.job_queue

    timer_handler = CommandHandler('start', start)
    u.dispatcher.add_handler(timer_handler)

    day_handler = CommandHandler('day', day)
    u.dispatcher.add_handler(day_handler)

    u.start_polling()
    u.idle(stop_signals=(signal.SIGABRT,))
