from aiogram.utils.callback_data import CallbackData


styles = [
    {   
        "name": "iris",
        "image": "data/styles/iris.jpeg",
        "model": "style_transfer/models/iris.pth",
        "description": "Irises"
    },
    {
        "name": "night",
        "image": "data/styles/night.jpeg",
        "model": "style_transfer/models/night.pth",
        "description": "Starry Night Over the Rhône"  
    },
    {
        "name": "red",
        "image": "data/styles/red.jpeg",
        "model": "style_transfer/models/red.pth",
        "description": "The Red Vineyard"
    },
    {
        "name": "green",
        "image": "data/styles/green.jpeg",
        "model": "style_transfer/models/green.pth",
        "description": "Landscape with a Carriage and a Train"
    }
]

examples = [
    {
        'name': 'Starry Night Over the Rhône',
        'image': 'data/examples/night.jpeg'
    },
    {
        'name': 'The Red Vineyard',
        'image': 'data/examples/red.jpeg'
    },
    {
        'name': 'Landscape with a Carriage and a Train',
        'image': 'data/examples/green.jpeg'
    },
    {
      'name': 'Irises',
      'image': 'data/examples/iris.jpeg'  
    }
    
]

styles_callback = CallbackData("style", "page", "selected")
