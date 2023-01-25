from aiogram import Dispatcher
from aiogram import types

from lexicon.lexicon_ru import LEXICON_RU

# Handler for text messages not handled by other handlers
async def send_answer(message: types.Message):
    await message.answer(text=LEXICON_RU['other_answer'])
    
# The function for regestering handler in dispatcher
def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(send_answer)
    