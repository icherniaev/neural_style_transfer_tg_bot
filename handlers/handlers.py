from keyboards.keyboards import get_page_keyboard, get_after_keyboard, get_start_keyboard, get_close_keyboard
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, CallbackQuery, InputMedia, InputMediaPhoto
from data.data import styles, styles_callback, examples
import os
from time import sleep
from services.services import stylization
from lexicon.lexicon import LEXICON_EN


model: dict[str: str] = {}

# Handlers for basic messages

async def process_start_command(message: Message):
    keyboard = get_start_keyboard()
    await message.answer(text=LEXICON_EN['/start'], reply_markup=keyboard)
    
async def process_help_command(query: CallbackQuery):
    keyboard = get_close_keyboard()
    await query.message.answer(text=LEXICON_EN['/help'], reply_markup=keyboard)
    
async def author_handler(query: CallbackQuery):
    keyboard = get_close_keyboard()
    await query.message.answer(text=LEXICON_EN['/author'], parse_mode='HTML', reply_markup=keyboard)
    
async def example(query: CallbackQuery):
    keyboard = get_close_keyboard()
    media = types.MediaGroup()
    for i in range(4):
        media.attach_photo(types.InputFile(examples[i]['image']), examples[i]['name'])
    await query.message.answer_media_group(media=media)
    
async def close(query: CallbackQuery):
    await query.message.delete()
    

# Handlers for image processing

async def begin_handler(query: CallbackQuery):
    style = styles[0]
    caption = LEXICON_EN['/begin']
    keyboard = get_page_keyboard(styles_callback=styles_callback)  # Page: 0
    with open(style['image'], 'rb') as file:
        await query.message.answer_photo(
            photo=file,
            caption=caption,
            reply_markup=keyboard
        )


async def page_handler(query: CallbackQuery, callback_data: dict): 
    page = int(callback_data.get("page"))
    style = styles[page]
    caption = style['description']
    keyboard = get_page_keyboard(page, styles_callback=styles_callback)
    with open(style['image'], 'rb') as file:
        photo = InputMedia(type="photo", media=file, caption=caption)
        await query.message.edit_media(photo, keyboard)
            
async def selected_handler(query: CallbackQuery, callback_data: dict):
     page = int(callback_data.get("page"))
     style = styles[page]
     model_selected = style['model']
     image = style['image']
     model[str(query.from_user.id)] = model_selected # create the model path
     sleep(1)
     await query.message.delete()
     await query.message.answer(LEXICON_EN['send'])
     
async def process_photo(message: Message):
    await message.answer(text=LEXICON_EN['processing'])
    path_for_photo = 'data/' + str(message.from_user.id) # create the path for photo
    try:
        os.mkdir(path_for_photo) 
    except:
        pass
    await message.photo[-1].download(path_for_photo + '/recieved.jpg') # save the photo
    model_selected = model[str(message.from_user.id)] # select the model
    processed_photo_path = stylization(photo_path=path_for_photo + '/recieved.jpg', model_path=model_selected, user_id=message.from_user.id) # process photo and save
    with open(processed_photo_path, 'rb') as file:
        await message.answer_photo(file) # send the photo to the user
        #await message.answer(text=LEXICON_EN['add'])
    keyboard = get_after_keyboard()
    await message.answer(text="Options:", reply_markup=keyboard)
 
# Handlers for the last keyboard   

async def send_another_photo(query: CallbackQuery):
    await query.message.delete()
    await query.message.answer(text="Please, upload another photo!")
    
async def select_another_style(query: CallbackQuery):
    await query.message.delete()
    await query.message.answer(text=LEXICON_EN['/begin'])
    
async def return_to_main_menu(query: CallbackQuery):
    await query.message.delete()
    keyboard = get_start_keyboard()
    await query.message.answer(text=LEXICON_EN['/start'], reply_markup=keyboard)
    

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_callback_query_handler(process_help_command, text='help')
    dp.register_callback_query_handler(begin_handler, text='begin')
    dp.register_callback_query_handler(author_handler, text='author')
    dp.register_callback_query_handler(example, text='examples')
    dp.register_callback_query_handler(close, text='close')
    dp.register_callback_query_handler(send_another_photo, text='another photo button')
    dp.register_callback_query_handler(select_another_style, text='begin')
    dp.register_callback_query_handler(return_to_main_menu, text='start')
    dp.register_callback_query_handler(page_handler, styles_callback.filter(selected="False"))
    dp.register_callback_query_handler(selected_handler, styles_callback.filter(selected="True"))
    dp.register_message_handler(process_photo, content_types=['photo'])
    
    