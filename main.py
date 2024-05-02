import telebot
from telebot import types

bot = telebot.TeleBot('7133490418:AAHK3YC7gWu-uLxJygNinVp5Fk1yz33_qDY')


@bot.message_handler(commands=['start'])
def start(message):
    klava = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='/begin')
    klava.add(button)
    bot.send_message(message.chat.id, 'Привет, я SpaceBot! Знаю много фактов, связанных с космосом. '
                                      'А знаешь ли ты? Отправь команду </begin> и начнём.', reply_markup=klava)


@bot.message_handler(commands=['begin'])
def begin_comand(message):
    klava = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='/Go')
    klava.add(button)
    bot.send_message(message.chat.id, 'Я буду задавать вопросы про различные факты о космосе, '
                                      'а ты отвечай из предложенных вариантов.Если появятся вопросы отправляй команду </help>',
                     reply_markup=klava)


@bot.message_handler(commands=['Go'])
def go_comand(message):
    klava = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(text='С.П. Королев', callback_data='button')
    button2 = types.InlineKeyboardButton(text='Ю.А. Гагарин', callback_data='button2')
    button3 = types.InlineKeyboardButton(text='Г.С. Титов', callback_data='button3')
    klava.add(button, button2, button3)
    bot.send_message(message.chat.id, 'Первый космонавт Земли?', reply_markup=klava)


@bot.callback_query_handler(func=lambda call: call.data)
def check_one(call):
    if call.data == 'button2':
        file = open('C:\Kosmos\img\gagarin.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Верно! Ю.А. Гагарин был первым кто полетел в космос.')
    elif call.data == 'button':
        bot.send_message(call.message.chat.id, 'Неверно:( С.П. Королев — выдающийся конструктор и учёный, '
                                               'работавший в области ракетной и ракетно-космической техники.Попробуй ёщё!')
    else:
        bot.send_message(call.message.chat.id, 'Неверно:( Г.С. Титов — второй советский космонавт, '
                                               'второй человек в мире, совершивший орбитальный космический полёт.'
                                               'Попробуй ёщё!')


bot.polling()
