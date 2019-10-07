import logging
import os
import datetime
import signal

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


TOKEN = "780204015:AAGkIDmwlnjngHyeXmSArTe_dqvsBUu6IQk"
NAME = "lfnotifybot"
PORT = os.environ.get('PORT')
"""
CHAT_ID = ''

def start(update: Update, context: CallbackContext):
    # CHAT_ID = str(update.message.chat_id)
    # print(update.message.chat_id)
    update.effective_message.reply_text(chat_id=update.message.chat_id, text="")
    context.job_queue.run_repeating(remind, datetime.time(hour=23, minute=30),context=update.message.chat_id)

def echo(update: Update, context: CallbackContext):
    update.effective_message.reply_text(update.effective_message.text)

def who(update: Update, context: CallbackContext):
    remind(update.message.chat_id)

def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)



def remind(context):
    context.bot.send_message(chat_id=context.job.context, text=get_birth_days())




    # Set these variable to the appropriate values
    
    

    # Port is given by Heroku
    

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('day', who))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    # queue = updater.job_queue
    # birthdays1 = queue.run_repeating(remind, interval=30, first=0)
    
    # birthdays = queue.run_daily(remind, datetime.time(hour=23, minute=30))
    # updater.start_polling(timeout=10000.0)
    # Start the webhook
    
"""

def get_birth_days():
    curr_date = datetime.datetime.now()
    persons = {}
    with open('dates.csv', 'r') as f:
        for s in f:
            arr = s.split(',')
            birth_date = arr[-1].split(';')[0].split('.')
            if int(birth_date[0]) == int(curr_date.day) and int(birth_date[1]) == int(curr_date.month):
                if len(birth_date) == 3:
                    persons[' '.join(arr[0:3])] = f'{int(curr_date.year) - int(birth_date[-1])} летие.'
                else:
                    persons[' '.join(arr[0:3])] = '.'.join(birth_date)

    message = 'Сегодня никаких дней рождений.'
    if len(persons) != 0:
        message = f'На {curr_date.day}.{curr_date.month}.{curr_date.year} дни рождения празднуют:\n' + \
              f'\n'.join([f'{key}: {value}' for key, value in persons.items()])

    return message



def callback_alarm(context: CallbackContext):
    context.bot.send_message(chat_id=context.job.context, text=get_birth_days())

def start(update: telegram.Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Привет! Я буду каждый день присылать тебе напоминания о днях рождения. Главное вовремя обновлять список.')

    context.job_queue.run_daily(callback_alarm, datetime.time(hour=23, minute=30), context=update.message.chat_id)
    # context.job_queue.run_repeating(callback_alarm, interval=30, context=update.message.chat_id)
    # gel_live(context)

def day(update: telegram.Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, text=get_birth_days())

# def callback_alarm(context: telegram.ext.CallbackContext):
#     context.bot.get_chat(chat_id=context.job.context)

# def gel_live(context: CallbackContext):
#     context.job_queue.run_repeating(callback_alarm, interval=60, first=0)


if __name__ == "__main__":
    u = Updater(TOKEN, use_context=True)
    j = u.job_queue

    timer_handler = CommandHandler('start', start)
    u.dispatcher.add_handler(timer_handler)

    day_handler = CommandHandler('day', day)
    u.dispatcher.add_handler(day_handler)

    # u.start_webhook(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path=TOKEN,
    #                       bootstrap_retries=-1)
    # u.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    u.start_polling()
    u.idle(stop_signals=(signal.SIGABRT,))
