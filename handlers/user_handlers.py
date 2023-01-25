from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text 
import os

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import style_kb
from services.services import sylization

# dictionary for models for each user
model: dict[str, str] = {}

# Handlers for basic messages
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=style_kb)
    
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
    
# Handlers for styles
async def process_style_choice_mal(message: Message):
    await message.answer(text=LEXICON_RU['send'])
    model[message.from_user.id] = message.text

async def process_style_choice_kd(message: Message):
    await message.answer(text=LEXICON_RU['send'])
    model[message.from_user.id] = message.text
    
async def process_style_choice_gon(message: Message):
    await message.answer(text=LEXICON_RU['send'])
    model[message.from_user.id] = message.text
    
async def process_photo(message: Message):
    await message.answer(text=LEXICON_RU['processing'])
    path_for_photo = 'data/' + str(message.from_user.id) # create the path for photo
    try:
        os.mkdir(path_for_photo) 
    except:
        pass
    await message.photo[-1].download(path_for_photo + '/recieved.jpg') # save the photo
    model_selected = model[message.from_user.id] # select the model
    processed_photo_path = sylization(photo_path=path_for_photo + '/recieved.jpg', model=model_selected, user_id=message.from_user.id) # process photo and save
    with open(processed_photo_path, 'rb') as file:
        await message.answer_photo(file) # send the photo to the user

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_style_choice_mal,
                                text=LEXICON_RU['mal_button'])
    dp.register_message_handler(process_style_choice_kd,
                                text=LEXICON_RU['kd_button'])
    dp.register_message_handler(process_style_choice_gon,
                                text=LEXICON_RU['gon_button'])
    dp.register_message_handler(process_photo, content_types=['photo'])


    
   

