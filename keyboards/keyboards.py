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

def get_after_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton(text="Select anlother style",
                                    callback_data="begin")
    button_2 = InlineKeyboardButton(text="Process another photo",
                                    callback_data="another photo button")
    button_3 = InlineKeyboardButton(text="Main menu",
                                    callback_data="start")
    
    keyboard.add(button_1)
    keyboard.add(button_2)
    keyboard.add(button_3)
    
    return keyboard


def get_start_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton(text="Begin style transfer",
                                    callback_data="begin")
    button_2 = InlineKeyboardButton(text="Author of the bot",
                                    callback_data="author")
    button_3 = InlineKeyboardButton(text="Info",
                                    callback_data="help")
    button_4 = InlineKeyboardButton(text="Examples of style transfer",
                                    callback_data='examples')
    
    keyboard.add(button_1)
    keyboard.add(button_2)
    keyboard.add(button_3)
    keyboard.add(button_4)
    
    return keyboard

def get_close_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton(text="Close",
                                    callback_data="close")
    keyboard.add(button_1)
    return keyboard
    
    