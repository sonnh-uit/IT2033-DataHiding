import numpy as np​

import torch​

from torchsummary import summary​

import steganogan​

model = torch.load("D:/python37/Lib/site-packages/steganogan/pretrained/basic.steg", map_location='cpu')​

#sumary = torch.nn.Module.load_state_dict(model)​

#print(sumary)​

attrs = vars(model)​

#print(', '.join("{}: {}".format(item[0], item[1]) for item in attrs.items()))​

print(dir(model))​

print("########################################")​

print(attrs.items())​