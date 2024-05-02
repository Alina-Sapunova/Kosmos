import telebot
from telebot import types

bot = telebot.TeleBot('7133490418:AAHK3YC7gWu-uLxJygNinVp5Fk1yz33_qDY')


@bot.message_handler(commands=['start'])
def start(message):
    klava = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(text='С.П. Королев', callback_data='button')
    button2 = types.InlineKeyboardButton(text='Ю.А. Гагарин', callback_data='button2')
    klava.add(button, button2)
    bot.send_message(message.chat.id, '1', reply_markup=klava)



bot.polling()
