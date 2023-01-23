 import sqlite3

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, \
    ConversationHandler, Filters

import models

bot_token = "5945103866:AAHMIjz3zQtEpMOVs2iYhXZxmpivubYQDOY"
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

conn = sqlite3.connect('phone.db', check_same_thread=False)
cursor = conn.cursor()
add_storage = []


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             f"Привет! Я бот-телефонный справочник\n"
                             f"/all_contact - Показать все контакты\n"
                             f"/find_name - Найти контакты по фамилии\n"
                             f"/add - Добавить контакт\n"
                             f"/delete - Удалить контакт")


# def info(update, context):
#     context.bot.send_message(update.effective_chat.id,
#                              f"Привет! Я бот-телефонный справочник\n"
#                              f"/all_contact - Показать все контакты\n"
#                              f"/find_name - Найти контакты по фамилии\n"
#                              f"/add - Добавить контакт\n"
#                              f"/delete - Удалить контакт")


def all_contact(update, context):
    data = models.get_contacts(cursor)
    context.bot.send_message(
        update.effective_chat.id,
        f"{data}")


def find_name(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите имя или фамилию\n"
        f"Для выхода введите /stop")
    return 1


def find_context(update, context):
    item = update.message.text
    data = models.get_contact(item, cursor)
    context.bot.send_message(
        update.effective_chat.id,
        f"{data}")


def stop(update, context):
    return ConversationHandler.END


def add(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите имя")
    return 1


def add_name(update, context):
    name = update.message.text
    add_storage.append(name)
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите фамилию")
    return 2


def add_surname(update, context):
    surname = update.message.text
    add_storage.append(surname)
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите номер телефона")
    return 3


def add_phone(update, context):
    phone = update.message.text
    add_storage.append(phone)
    models.add_contact(add_storage, conn, cursor)
    context.bot.send_message(
        update.effective_chat.id,
        f"Запись добавлена\n Для выхода введите /stop")
    add_storage.clear()


def delete_contact(update, context):
    id_contact = update.message.text
    msg = models.delete(id_contact, conn, cursor)
    context.bot.send_message(
        update.effective_chat.id,
        msg)


def delete(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите ID")
    return 1


def get_handler(command, func, func1):
    hand = ConversationHandler(
        entry_points=[CommandHandler(command, func)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, func1)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    return hand


add_handler = ConversationHandler(
    entry_points=[CommandHandler('add', add)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, add_name)],
        2: [MessageHandler(Filters.text & ~Filters.command, add_surname)],
        3: [MessageHandler(Filters.text & ~Filters.command, add_phone)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)

find_handler = get_handler('find_name', find_name, find_context)
delete_handler = get_handler('delete', delete, delete_contact)

start_handler = CommandHandler('start', start)
back_handler = CommandHandler('back', start)
all_handler = CommandHandler('all_contact', all_contact)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(all_handler)
dispatcher.add_handler(find_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(delete_handler)
updater.start_polling()
updater.idle()
conn.close()