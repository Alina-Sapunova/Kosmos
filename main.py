import telebot
from telebot import types

bot = telebot.TeleBot('7133490418:AAHK3YC7gWu-uLxJygNinVp5Fk1yz33_qDY')

SPISOK_COMAND = ['/inline', '/help', '/start', '/begin', '/Go', '2', '3', '4', '5', '/end']


@bot.message_handler(commands=['start'])
def start(message):
    klava_begin = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='/begin')
    klava_begin.add(button)
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Привет, я SpaceBot! Знаю много фактов, связанных с космосом. '
                                          'А знаешь ли ты? Отправь команду /begin и начнём.', reply_markup=klava_begin)


@bot.message_handler(commands=['begin'])
def begin_comand(message):
    klava_go = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='/Go')
    klava_go.add(button)
    bot.send_message(message.chat.id, 'Я задам 5 вопросов про различные факты о космосе, '
                                      'а ты отвечай из предложенных вариантов. Если появятся вопросы отправляй команду /help,',
                     reply_markup=klava_go)


@bot.message_handler(commands=['Go'])
def go_comand(message):
    klava_one = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(text='С.П. Королев', callback_data='button')
    button2 = types.InlineKeyboardButton(text='Ю.А. Гагарин', callback_data='button2')
    button3 = types.InlineKeyboardButton(text='Г.С. Титов', callback_data='button3')
    klava_one.add(button, button2, button3)
    bot.send_message(message.chat.id, 'Вопрос 1: Первый космонавт Земли?', reply_markup=klava_one)


@bot.callback_query_handler(func=lambda call: call.data)
def check(call):
    klava_two = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='/2')
    klava_two.add(button)

    klava_three = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='/3')
    klava_three.add(button)

    klava_four = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='/4')
    klava_four.add(button)

    klava_five = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='/5')
    klava_five.add(button)

    klava_six = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='/end')
    klava_six.add(button)

    if call.data == 'button2':
        file = open('C:\Kosmos\img\gagarin.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Верно! Ю.А. Гагарин был первым кто полетел в космос. '
                                                   'Нажми на команду /2 для следующего вопроса', reply_markup=klava_two)
    elif call.data == 'button':
        bot.send_message(call.message.chat.id, 'Неверно:( С.П. Королев — выдающийся конструктор и учёный, '
                                               'работавший в области ракетной и ракетно-космической техники.Попробуй ёщё!')
    elif call.data == 'button3':
        bot.send_message(call.message.chat.id, 'Неверно:( Г.С. Титов — второй советский космонавт, '
                                               'второй человек в мире, совершивший орбитальный космический полёт.'
                                               'Попробуй ёщё!')

    elif call.data == 'btn2' or call.data == 'btn3':
        bot.send_message(call.message.chat.id, 'Неверно:( Попробуй ёщё!')
    elif call.data == 'btn':
        bot.send_message(call.message.chat.id,
                         'Верно! 12 апреля-День космонавтики. Нажми на команду /3 для следующего вопроса',
                         reply_markup=klava_three)
    elif call.data == 'bt':
        bot.send_message(call.message.chat.id, 'Неверно:( С.Е. Савицкая-вторая в мире женщина-космонавт после '
                                               'Валентины Терешковой. Совершила два полёта в космос. Попробуй ёщё!')
    elif call.data == 'bt3':
        bot.send_message(call.message.chat.id,
                         'Неверно:( Е.В. Кондакова-Герой Российской Федерации.Лётчик-космонавт '
                         'Российской Федерации.Стала третьей женщиной-космонавтом в истории после Валентины Терешковой '
                         'и Светланы Савицкой. Попробуй ёщё!')
    elif call.data == 'bt2':
        file2 = open('C:\Kosmos\img\chereshkova.jpeg', 'rb')
        bot.send_photo(call.message.chat.id, file2,
                       'Верно! В.В. Терешкова вошла в историю как первая женщина-космонавт '
                       'и единственная женщина, совершившая одиночный космический полет.'
                       'После полета продолжила заниматься космической подготовкой.'
                       ' Нажми на команду /4 для следующего вопроса', reply_markup=klava_four)
    elif call.data == 'kn':
        bot.send_message(call.message.chat.id, 'Неверно:( Попробуй ёщё!')
    elif call.data == 'kn2':
        bot.send_message(call.message.chat.id, 'Неверно:( Попробуй ёщё!')
    elif call.data == 'kn3':
        bot.send_message(call.message.chat.id, 'Верно! 1957 год считается началом космической эры человечества. '
                                               'Нажми на команду /5 для следующего вопроса', reply_markup=klava_five)
    elif call.data == 'knop3':
        bot.send_message(call.message.chat.id, 'Неверно:( Попробуй ёщё!')
    elif call.data == 'knop2':
        bot.send_message(call.message.chat.id, 'Неверно:( Попробуй ёщё!')
    elif call.data == 'knop':
        bot.send_message(call.message.chat.id, 'Молодец!')
        bot.send_message(call.message.chat.id, 'Название Млечный Путь произошло от латинского via lactea, '
                                               'что переводится как — молочная дорога. Млечный Путь — '
                                               'наша родная галактика.Она состоит примерно из 100-400 '
                                               'миллиардов звезд! А ещё наша галактика существует уже порядка '
                                               '13,6 миллиардов лет!', reply_markup=klava_six)
        bot.send_message(call.message.chat.id, 'Класс! Теперь напиши команду /end для завершения диалога.')


@bot.message_handler(commands=['2'])
def two_comand(message):
    klava = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(text='12 апреля', callback_data='btn')
    button2 = types.InlineKeyboardButton(text='7 апреля', callback_data='btn2')
    button3 = types.InlineKeyboardButton(text='1 мая', callback_data='btn3')
    klava.add(button, button2, button3)
    bot.send_message(message.chat.id, 'Вопрос 2: День космонавтики?', reply_markup=klava)


@bot.message_handler(commands=['3'])
def three_comand(message):
    klava3 = types.InlineKeyboardMarkup(row_width=1)
    bt = types.InlineKeyboardButton(text='С.Е. Савицкая', callback_data='bt')
    bt2 = types.InlineKeyboardButton(text='В.В. Терешкова', callback_data='bt2')
    bt3 = types.InlineKeyboardButton(text='Е.В. Кондакова', callback_data='bt3')
    klava3.add(bt, bt2, bt3)
    bot.send_message(message.chat.id, 'Вопрос 3: Первая женщина – космонавт?', reply_markup=klava3)


@bot.message_handler(commands=['4'])
def four_comand(message):
    klava4 = types.InlineKeyboardMarkup(row_width=1)
    kn = types.InlineKeyboardButton(text='1961', callback_data='kn')
    kn2 = types.InlineKeyboardButton(text='1962', callback_data='kn2')
    kn3 = types.InlineKeyboardButton(text=' 1957', callback_data='kn3')
    klava4.add(kn, kn2, kn3)
    bot.send_message(message.chat.id, 'Вопрос 4: Какой год считают началом эры космонавтики?', reply_markup=klava4)


@bot.message_handler(commands=['5'])
def four_comand(message):
    klava5 = types.InlineKeyboardMarkup(row_width=1)
    knop = types.InlineKeyboardButton(text='Млечный путь', callback_data='knop')
    knop2 = types.InlineKeyboardButton(text='Галактика Андромеды', callback_data='knop2')
    knop3 = types.InlineKeyboardButton(text='Земная галактика', callback_data='knop3')
    klava5.add(knop, knop2, knop3)
    bot.send_message(message.chat.id, 'Вопрос 5: Как называется наша галактика?', reply_markup=klava5)


@bot.message_handler(commands=['inline'])
def inline_comand(message):
    klava = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(text='Первая женщина космонавт',
                                        url='https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%80%D0%B5%D1%88%D0%BA%D0%BE%D0%B2%D0%B0,_%D0%92%D0%B0%D0%BB%D0%B5%D0%BD%D1%82%D0%B8%D0%BD%D0%B0_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%BD%D0%B0')
    button2 = types.InlineKeyboardButton(text='Ю.А. Гагарин',
                                         url='https://ru.wikipedia.org/wiki/%D0%93%D0%B0%D0%B3%D0%B0%D1%80%D0%B8%D0%BD,_%D0%AE%D1%80%D0%B8%D0%B9_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B5%D0%B2%D0%B8%D1%87')
    button3 = types.InlineKeyboardButton(text='Млечный путь',
                                         url='https://pikabu.ru/story/10_interesnyikh_faktov_o_mlechnom_puti_4349014')
    klava.add(button, button2, button3)
    bot.send_message(message.chat.id, 'Полезные ссылки', reply_markup=klava)


@bot.message_handler(commands=['help'])
def help_comand(message):
    bot.send_message(message.chat.id, """Вот список всех команд для общения с SpaceBot:
    /inline - полезные ссылки
    /help - помощь пользователю
    /start - запустить бота
    /begin - введение в суть диалога с ботом
    /Go - начать диалог с ботом
    /2, /3, /4, /5, - бот задаст следующий
     по счёту вопрос
     /end - завершить диалог""")


@bot.message_handler(commands=['end'])
def end_comand(message):
    klava_seven = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='/inline')
    klava_seven.add(button)
    file = open('C:\Kosmos\img\stik.jpg', 'rb')
    bot.send_message(message.chat.id, 'На этом всё! Лови подарочек от SpaceBot.')
    bot.send_photo(message.chat.id, file,
                   'Теперь ты больше знаешь о космосе. Если что-то заинтересовало отправвь команду '
                   '/inline, там есть полезные ссылочки. Пока-пока', reply_markup=klava_seven)


@bot.message_handler(func=lambda message: True)
def eho(message):
    if message.text not in SPISOK_COMAND:
        bot.send_message(message.chat.id, 'Ваша команда не понятна. Если возникли трудности отправь команду /help')


bot.polling()
