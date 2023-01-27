from aiogram.utils.callback_data import CallbackData


styles = [
    {   
        "name": "day",
        "image": "data/styles/day.jpeg",
        "model": "style_transfer/models/day.pth",
    },
    {
        "name": "night",
        "image": "data/styles/night.jpeg",
        "model": "style_transfer/models/night.pth"  
    },
    {
        "name": "kan",
        "image": "data/styles/kan.jpeg",
        "model": "style_transfer/models/kd.pth"
    },
    {
        "name": "mal",
        "image": "data/styles/ma.jpeg",
        "model": "style_transfer/models/mal.pth"
    }
]

styles_callback = CallbackData("style", "page", "selected")
