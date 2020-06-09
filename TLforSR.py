import torch
import torch.nn as nn
import torch.nn.functional as F

import matplotlib.pyplot as plt
import numpy as np
import os

dddd
class BasicBlock(nn.Module):
    # initailize layers
    def __init__(self,in_channel,channel_1,):
        # get mother class 생성자
        super().__init__()
        self.conv1 = nn.Conv2d(in_channel,channel_1,3,padding=1)
        self.bn1 = nn.BatchNorm2d(channel_1)        
        self.conv2 = nn.Conv2d(channel_1,channel_1,3,padding=1)
        self.bn2 = nn.BatchNorm2d(channel_1)
        self.identity = nn.Sequential()
        #if in_channel != channel_1:
        #   self.identity = nn.Sequential(nn.Conv2d(in_channel, channel_1, 1), nn.BatchNorm2d(channe_1))

    #link all layers through activate f 
    def forward(self, x):
        h1_relu = F.relu(self.bn1(self.conv1(x)))
        h2_relu = self.conv2(h1_relu)
        # 왜 배치놂한 거 위에 더하지 === 논문에 나와있다
        return F.relu(self.bn2(h2_relu) + self.identity)

class ResNet34(nn.Module):
    def __init__(self,x):
        super().__init__()
        self.conv0 = F.Conv2d()
        self.res1 = BasicBlock(64,64)
        self.res2 = BasicBlock(64,64)
        self.res3 = BasicBlock(64,64)
        self.res4 = BasicBlock(64,128)
        self.res5 = BasicBlock(128,128)
        self.res6 = BasicBlock(128,128)
        self.res7 = BasicBlock(128,128)
        self.res8 = BasicBlock(128,256)
        self.res9 = BasicBlock(256,256)
        self.res10 = BasicBlock(256,256)
        self.res10 = BasicBlock(256,256)
        self.res10 = BasicBlock(256,256)
        self.res10 = BasicBlock(256,256)
        self.res14 = BasicBlock(256,512)
        self.res15 = BasicBlock(512,512)
        self.res16 = BasicBlock(512,512)
        self.avgpool = nn.AvgPool2d(512,512)

    def forward(self ,x):



if __name__ == "__name__":
    ResNet34()

