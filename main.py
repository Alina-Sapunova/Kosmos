import logging
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
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
        reply_keyboard = [['/Go', '/No']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        await update.message.reply_text('Я буду задавать вопросы про различные факты о космосе,'
                                        'а ты отвечай из предложенных вариантов.'
                                        'Если появятся вопросы отправляй команду </help>')


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CommandHandler("help", help_command))
    # application.add_handler(CommandHandler("inline", inline))
    application.add_handler(CommandHandler("begin", begin_command))
    # application.add_handler(CommandHandler("8march", photo_eighth_march))
    # application.add_handler(CommandHandler("9may", photo_nine_may))
    # application.add_handler(CommandHandler("23february", photo_february))
    # application.add_handler(CommandHandler("new_year", photo_new_year))
    # application.add_handler(CommandHandler("birthday", photo_birthday))
    # application.add_handler(CommandHandler("easter", photo_easter))
    # application.add_handler(CommandHandler("No", no_command))
    application.run_polling()


if __name__ == '__main__':
    main()
