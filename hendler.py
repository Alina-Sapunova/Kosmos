import telebot
from telebot import types

bot = telebot.TeleBot('7133490418:AAHK3YC7gWu-uLxJygNinVp5Fk1yz33_qDY')
SPISOK_COMAND = ['/inline', '/help', '/start', '/begin', '/Go', '/next']


def sms(message):
    sms = message.text
    if sms not in SPISOK_COMAND:
        bot.send_message(message.chat.id, f'Команда {sms} не понятна. Если возникли трудности отправь команду /help')


