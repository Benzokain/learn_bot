import logging
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    print(update)
    update.message.reply_text('Привет пользователь! ТЫ вызвал команду /start')

def test_def(update, context):
    print('Вызван /test')
    update.message.reply_text('Привет пользователь! ТЫ вызвал команду /test')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot=Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('test', test_def))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('BOT is starting')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__name__':
    main()