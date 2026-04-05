from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import ContextTypes



def button_lang(lang:str)->ReplyKeyboardMarkup:
    if lang == 'uz':
        buttons = [
            [
                KeyboardButton('📝 Testni boshlash'),
                KeyboardButton('🎫 Biletlar')
            ]
        ]

    elif lang == 'ru':
        buttons = [
            [
                KeyboardButton('📝 Начать тест'),
                KeyboardButton('🎫 Билеты')
            ]
        ]

    return ReplyKeyboardMarkup(buttons,one_time_keyboard=True,resize_keyboard=True)