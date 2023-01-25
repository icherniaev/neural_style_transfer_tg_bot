from style_transfer.processing import stylize
from lexicon.lexicon_ru import LEXICON_RU


def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key

# Get the style choice and load the respective model
def sylization(photo_path: 'str', model: 'str', user_id: str):
    model: str = _normalize_user_answer(model) # name of the model
    output_image_path='data/' + str(user_id) + '/processed.jpg'
    stylize(model="style_transfer/models/" + model + '.pth',
            content_image_path=photo_path,
            output_image_path=output_image_path)
    return output_image_path
    

# Get the image, do the processing and return the model
