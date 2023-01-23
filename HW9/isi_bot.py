from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from random import randint

bot_token ="5945103866:AAHMIjz3zQtEpMOVs2iYhXZxmpivubYQDOY"
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, f"Привет я бот калькулятор. Список команд:"
    "/calc- решить пример,/convert-перевести кг в г,/exit-выход")

def exit(update, context):
    context.bot.send_message(update.effective_chat.id,"Пока,пока!")

def calc(update, context):
    context.bot.send_message(update.effective_chat.id,"Введите выражение.")
    return 1


def convert(update, context):
    context.bot.send_message(update.effective_chat.id,"Введите массу.")
    return 1

def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def calculet(update, context):
    primer = update.message.text
    update.message.reply_text(
        f"Ответ: {eval(primer)} введите новое выражение или введите /stop")


def converter(update, context):
    massa = update.message.text
    update.message.reply_text(
        f"Ответ: {(int(massa)*1000)} введите новую массу или введите /stop")




conv_handler = ConversationHandler(
entry_points=[CommandHandler('calc', calc)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, calculet)],
        },
       fallbacks=[CommandHandler('stop', stop)]
    )

convert_handler = ConversationHandler(
entry_points=[CommandHandler('convert', convert)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, converter)],
        },
       fallbacks=[CommandHandler('stop', stop)]
    )

exit_handler = CommandHandler('exit', exit)
dispatcher.add_handler(exit_handler)

dispatcher.add_handler(conv_handler)

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(convert_handler)
updater.start_polling()
updater.idle()