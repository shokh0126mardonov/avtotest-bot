from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode


async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    full_name = update.effective_user.full_name
    text = f"""
    <b>Salom {full_name}</b> 👋

    Tilni tanlang:

    /uz - O'zbek tili 🇺🇿
    /ru - Русский язык 🇷🇺
    """

    await update.message.reply_text(
            text,
            parse_mode=ParseMode.HTML
        )
 