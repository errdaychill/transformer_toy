import torch
import torch.nn as nn
import torch.nn.functional as F

import matplotlib.pyplot as plt
import numpy as np
import os
# We
# use SGD with a mini-batch size of 256. The learning rate
# starts from 0.1 and is divided by 10 when the error plateaus,
# and the models are trained for up to 60 × 104
# iterations. We
# use a weight decay of 0.0001 and a momentum of 0.9

# In testing, for comparison studies we adopt the standard
# 10-crop testing [21]. For best results, we adopt the fullyconvolutional form as in [40, 12], and average the scores
# at multiple scales (images are resized such that the shorter
# side is in {224, 256, 384, 480, 640})

kkkk
class BasicBlock(nn.Module):
    # initailize layers
    def __init__(self,in_channel,channel_1,stride=1):
        # get mother class 생성자
        super().__init__()
        self.conv1 = nn.Conv2d(in_channel, channel_1, 3, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm2d(channel_1)        
        self.conv2 = nn.Conv2d(channel_1, channel_1, 3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(channel_1)
        self.shortcut = nn.Sequential()
        # if in_channel != channel_1:
        #    self.shortcut = nn.Sequential(nn.Conv2d(in_channel, channel_1, 1), nn.BatchNorm2d(channe_1))

    #link all layers through activate f 
    def forward(self, x):
        h1_relu = F.relu(self.bn1(self.conv1(x)))
        h2_relu = self.conv2(h1_relu)
        # 왜 배치놂한 거 위에 더하지 === 논문에 나와있다
        return F.relu(self.bn2(h2_relu) + self.identity)
    
class ResNet34(nn.Module):
    def __init__(self,x,classes=10):
        super().__init__()
        # layer  = Values
        self.conv1 = nn.Conv2d(in_channel, 64, 7, stride=2, padding=3)
        # self.maxpool = nn.MaxPool2d(self.conv0
        self.seq_64 = nn.Sequential(BasicBlock(64,64), BasicBlock(64,64), BasicBlock(64,64)
        self.seq_128 = nn.Sequential(BasicBlock(64,128,2),BasicBlock(128,128),BasicBlock(128,128),BasicBlock(128,128))
        self.seq_256 = nn.Sequential(BasicBlock(128,256,2),BasicBlock(256,256),BasicBlock(256,256),
        BasicBlock(256,256),BasicBlock(256,256),BasicBlock(256,256))
        self.seq_512 = nn.Sequential(BasicBlock(256,512,2), BasicBlock(512,512), BasicBlock(512,512)) 
        self.avgpool = nn.AvgPool2d(512,512)
        self.fc_layer = nn.Linear(self.avgpool.shape[0], classes)
            
        dddd
    def forward(self ,x):
        conv1 = self.conv1(x)
        conv2_input =F.MaxPool2d(conv1)
        conv2_x = self.seq_64(conv2_input)
        conv3_x = self.seq_128(conv2_x)
        conv4_x = self.seq_256(conv3_x)
        conv5_x = self.seq_512(conv4_x)

        # global averagepool
        #FC dimension depends on CIFAR - X
        avgpool = F.AvgPool2d(conv5_x)
        scores = self.fc_layer(avgpool)
        
        loss = nn.CrossEntropyLoss
    

if __name__ == "__name__":
    ResNet34()

