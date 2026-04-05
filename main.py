from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler
from decouple import config

from handler import start,language



def main():
    app = ApplicationBuilder().token(config("TOKEN")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler(["uz", "ru"], language)) 

    app.run_polling()


if __name__ == '__main__':
    main()