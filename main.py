import re

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    PollAnswerHandler,
    filters,
    ConversationHandler
)

from decouple import config
from handler import start, language, quiz, handle_answer,start_conv


def main():
    app = ApplicationBuilder().token(config("TOKEN")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler(["uz", "ru"], language))

    app.add_handler(
        MessageHandler(
            filters.Regex(re.compile(r'^(📝 Testni boshlash|📝 Начать тест)$')),
            quiz
        )
    )

    conv_handler = ConversationHandler(
        entry_points=[
    MessageHandler(filters.Regex(r"^🎫 (Biletlar|Билеты)$"), start_conv)
        ],
        states={},
        fallbacks=[]
    )

    app.add_handler(conv_handler)
  
    app.add_handler(PollAnswerHandler(handle_answer))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()