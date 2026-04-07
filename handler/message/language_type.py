from telegram import Update
from telegram.ext import ContextTypes

from handler import button_lang

async def language(update:Update,context:ContextTypes.DEFAULT_TYPE):
    text = update.message.text.replace('/','')
    context.user_data['lang'] = text

    if text == "uz":
        await update.message.reply_text("👇 Qani ketdik:start yoki test deb yozing va testni boshlang!",reply_markup=button_lang(text))

    if text == "ru":
        await update.message.reply_text("👇 Поехали:Напишите старт или тест и начните тест!",reply_markup=button_lang(text))