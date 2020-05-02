import datetime
import logging
import os
import signal

import telegram
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)

from birth_day import BirthDay as birth_d
from user_manager import UserManager as u_man

import persistent as pers
from admin import restricted as is_admin

TOKEN = os.environ.get('BOT_TOKEN')
NAME = os.environ.get('BOT_NAME')
PORT = os.environ.get('BOT_PORT')
# REQUEST_KWARGS = {
#     # "USERNAME:PASSWORD@" is optional, if you need authentication:
#     # 'proxy_url': 'HTTPS://185.198.184.14:48122/',
# }


def callback_alarm(context: CallbackContext):
    logging.getLogger().info(f'{context.job.context} call /day or alarm.')
    context.bot.send_message(
        chat_id=context.job.context, text=birth_d.get_birth_days())


def start(update: telegram.Update, context: CallbackContext):
    msg = """Привет! 
Я буду каждый день присылать тебе напоминания о важных событиях. 
Главное вовремя обновлять список."""
    if not u_man.is_user_in_list(update.message.chat_id):

        logging.getLogger().info(
            f'Message /start on - {update.message.chat_id}')
        u_man.add_user_in_list(update.message.chat_id)

        context.bot.send_message(chat_id=update.message.chat_id, text=msg)
        context.job_queue.run_daily(callback_alarm,
                                    datetime.time(hour=7, minute=1),
                                    context=update.message.chat_id)
    else:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text='Вы уже подписаны.')


def day(update: telegram.Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=birth_d.get_birth_days())


# @is_admin
def save_jobs(update: telegram.Update, context: CallbackContext):
    pers.save_jobs_job(context)


# @is_admin
def load_jobs(update: telegram.Update, context: CallbackContext):
    pers.load_jobs_job(update, context)


if __name__ == "__main__":

    logging.basicConfig(filename='./logs/debug.log',
                        filemode='a',
                        format='%(asctime)s - %(name)s - %(levelname)s -' +
                        '%(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -' +
                        '%(message)s', level=logging.INFO)

    logging.getLogger().info(f"Bot {NAME}({TOKEN[:3]}..{TOKEN[-3:]}) \
        started on {PORT} port")

    u = Updater(TOKEN, use_context=True)
    j = u.job_queue

    timer_handler = CommandHandler('start', start)
    u.dispatcher.add_handler(timer_handler)

    day_handler = CommandHandler('day', day)
    u.dispatcher.add_handler(day_handler)

    save_jobs_handler = CommandHandler('save_jobs', save_jobs)
    u.dispatcher.add_handler(save_jobs_handler)

    load_jobs_handler = CommandHandler('load_jobs', load_jobs)
    u.dispatcher.add_handler(load_jobs_handler)

    u.start_polling()
    u.idle(stop_signals=(signal.SIGABRT,))
