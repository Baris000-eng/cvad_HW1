import torchvision.models as models
import torch.nn as nn


class AffordancePredictor(nn.Module):
    """Afforance prediction network that takes images as input"""
    def __init__(self):
        super(AffordancePredictor,self).__init__()
        is_Pretrained=True
        my_resnet_model = models.resnet18(pretrained=is_Pretrained)
       
        

    def forward(self, img):
        
        pass
