from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, InputMedia
from aiogram.utils.callback_data import CallbackData

from data.data import styles
from lexicon.lexicon import LEXICON_EN

def get_page_keyboard(page: int = 0, styles_callback: CallbackData = None) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)
    has_next_page = len(styles) > page + 1

    if page != 0:
        keyboard.insert(
            InlineKeyboardButton(
                text=LEXICON_EN['backward'],
                callback_data=styles_callback.new(page=page - 1, selected=False)
            )
        )

    keyboard.insert(
        InlineKeyboardButton(
            text=LEXICON_EN['select'],
            callback_data=styles_callback.new(page=page, selected=True)
        )
    )

    if has_next_page:
        keyboard.insert(
            InlineKeyboardButton(
                text=LEXICON_EN['forward'],
                callback_data=styles_callback.new(page=page + 1, selected=False)
            )
        )

    return keyboard