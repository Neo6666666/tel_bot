from functools import wraps


LIST_OF_ADMINS = []


def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Вы не являетесь админом.')
            return
        return func(update, context, *args, **kwargs)
    return wrapped
