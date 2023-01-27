from style_transfer.processing import stylize

# Get the style choice and load the respective model
def stylization(photo_path: 'str', model_path: 'str', user_id: str):
    output_image_path='data/' + str(user_id) + '/processed.jpg'
    stylize(model_path=model_path,
            content_image_path=photo_path,
            output_image_path=output_image_path)
    return output_image_path
    

# Get the image, do the processing and return the model
