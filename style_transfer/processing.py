import torch
import style_transfer.utils as utils
from torchvision import transforms
from style_transfer.transformer_net import TransformerNet
import re

def stylize(model_path: str, content_image_path: str = None, output_image_path: str = None):
    """
    path to content image and path to model.pth
    """
    device = torch.device("cpu")
    content_image = utils.load_image(content_image_path) #load image form db
    content_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])
    content_image = content_transform(content_image) # problem here
    content_image = content_image.unsqueeze(0).to(device)
    
    with torch.no_grad():
        style_model = TransformerNet()
        state_dict = torch.load(model_path)
        # remove saved deprecated running_* keys in InstanceNorm from the checkpoint
        for k in list(state_dict.keys()):
            if re.search(r'in\d+\.running_(mean|var)$', k):
                del state_dict[k]
        style_model.load_state_dict(state_dict)
        style_model.to(device)
        style_model.eval()
        output = style_model(content_image).cpu()
        return utils.save_image(output_image_path, output[0])
            
    
    