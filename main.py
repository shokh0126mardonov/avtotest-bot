import re

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    PollAnswerHandler,
    filters,
)

from decouple import config
from handler import start, language, quiz, handle_answer


def main():
    app = ApplicationBuilder().token(config("TOKEN")).build()

    # basic handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler(["uz", "ru"], language))

    # quiz start button
    app.add_handler(
        MessageHandler(
            filters.Regex(re.compile(r'^(📝 Testni boshlash|📝 Начать тест)$')),
            quiz
        )
    )

  
    app.add_handler(PollAnswerHandler(handle_answer))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()