import torchvision.models as models
import torch.nn as nn


class CILRS(nn.Module):
    """An imitation learning agent with a resnet backbone."""
    def __init__(self):
      super(CILRS,self).__init__()
      is_model_pretrained = True
      my_resnet_model = models.resnet18(pretrained=is_model_pretrained)
      
        

    def forward(self, img, command):
      pass
        

