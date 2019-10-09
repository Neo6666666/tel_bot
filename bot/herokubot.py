import logging
import os
import datetime
import signal
import logging

import telegram
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          CallbackContext)

from birth_day import BirthDay as birth_d
from user_manager import UserManager as u_man

TOKEN = os.environ.get('BOT_TOKEN')
NAME = os.environ.get('BOT_NAME')
PORT = os.environ.get('BOT_PORT')


def callback_alarm(context: CallbackContext):
    logging.getLogger().info(context.job.context, 'call /day or alarm.')
    context.bot.send_message(
        chat_id=context.job.context, text=birth_d.get_birth_days())


def start(update: telegram.Update, context: CallbackContext):
    msg = 'Привет! Я буду каждый день присылать тебе напоминания о днях \
        рождения. Главное вовремя обновлять список.'
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)

    logging.getLogger().info('Message /start on -', update.message.chat_id)
    if not u_man.is_user_in_list(update.message.chat_id):
        u_man.add_user_in_list(update.message.chat_id)
        context.job_queue.run_daily(callback_alarm, 
                                    datetime.time(hour=23, minute=30), 
                                    context=update.message.chat_id)


def day(update: telegram.Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, 
                             text=birth_d.get_birth_days())


if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
        %(message)s', level=logging.INFO)

    logging.getLogger().info(f"Bot {NAME}({TOKEN[:3]}..{TOKEN[-3:]}) \
        started on {PORT} port")

    u = Updater(TOKEN, use_context=True)
    j = u.job_queue

    timer_handler = CommandHandler('start', start)
    u.dispatcher.add_handler(timer_handler)

    day_handler = CommandHandler('day', day)
    u.dispatcher.add_handler(day_handler)

    u.start_polling()
    u.idle(stop_signals=(signal.SIGABRT,))
