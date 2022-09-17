import logging
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    # print(update)
    update.message.reply_text('Привет пользователь! ТЫ вызвал команду /start')

def test_def(update, context):
    print('Вызван /test')
    update.message.reply_text('Привет пользователь! ТЫ вызвал команду /test')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def wordcount_def(update, context):
    print('Вызван /wordcount')
    # print(update.message.text)
    # text = update.message.text
    print(update.message.text.isdigit())
    if len(update.message.text.split()) > 1 and update.message.text.strip() and not any(char.isdigit() for char in update.message.text):
        count_list = update.message.text.split()
        update.message.reply_text(f'Введенный текст состоит из {len(count_list)-1} слов(а)')
    else:
        update.message.reply_text('После команды "/wordcount" нужно указать слово и фразу')



def main():
    mybot=Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('test', test_def))
    dp.add_handler(CommandHandler('wordcount', wordcount_def))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('BOT is starting')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()