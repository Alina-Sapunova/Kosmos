import logging
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from config import TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    reply_keyboard = [['/begin', '/finish']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        "Привет, я SpaceBot! Знаю много фактов, связанных с космосом. "
        "А знаешь ли ты? Отправь команду </begin> и начнём.",
        reply_markup=markup
    )


async def begin_command(update, context):
    if 'begin' in update.message.text:
        reply_keyboard = [['/Go']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        await update.message.reply_text('Я буду задавать вопросы про различные факты о космосе, '
                                        'а ты отвечай из предложенных вариантов.'
                                        'Если появятся вопросы отправляй команду </help>',
                                        reply_markup=markup
                                        )


def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


async def fact_one(update, context):
    buttons = ['/1', '/two', '/3']
    keyboard = [
        [button] for button in buttons
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text(
        text="""Первый космонавт Земли?
             Варианты ответа:
             1.С.П. Королев
             2.Ю.А. Гагарин
             3.Г.С. Титов""",
        reply_markup=reply_markup
    )


async def eee(update, context):
    if 'Фил' in update.message.text:
        await update.message.reply_text("ееееее")

async def otvet_command(update, context):
    if 'two' in update.message.text:
        chat_id = update.message.chat.id
        await context.bot.send_photo(chat_id=chat_id, photo="C:\Kosmos\img\gagarin.jpg")


async def f_command(update, context):
    await update.message.reply_text("ffffffff")


async def finish_command(update, context):
    await update.message.reply_text("Пока-пока")


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CommandHandler("help", help_command))
    # application.add_handler(CommandHandler("inline", inline))
    application.add_handler(CommandHandler("begin", begin_command))
    application.add_handler(CommandHandler("finish", finish_command))
    application.add_handler(CommandHandler("Go", fact_one))
    application.add_handler(CommandHandler("two", otvet_command))
    # application.add_handler(MessageHandler("Фил", eee))
    application.run_polling()



if __name__ == '__main__':
    main()

