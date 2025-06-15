import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from django.conf import settings

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    username = user.username
    # Store username in database (implement your storage logic here)
    update.message.reply_text(f'Hello, {username}! Your username has been stored.')

def main():
    updater = Updater(settings.TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main() 