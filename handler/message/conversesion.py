from telegram import Update
from telegram.ext import ContextTypes


async def start_conv(update:Update,context:ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🎫 Biletlar":
        await update.message.reply_text("Ishlamoqchi bo'lgan bilet raqamini yozing:")
    elif text == "🎫 Билеты":
        await update.message.reply_text("Введите номер билета, который хотите пройти:")
