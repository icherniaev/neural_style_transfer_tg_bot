from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU

# Create a keyboard for style selection
style_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                    resize_keyboard=True)
button_mal: KeyboardButton = KeyboardButton(LEXICON_RU['mal_button'])
button_kd: KeyboardButton = KeyboardButton(LEXICON_RU['kd_button'])
button_gon: KeyboardButton = KeyboardButton(LEXICON_RU['gon_button'])

style_kb.add(button_mal, button_kd, button_gon)

