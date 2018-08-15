import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class Network(nn.Module):

def __init__(self):
    super(Network, self).__init__()
    #Starts with some convolutional layers
    self.conv1 = nn.Conv2d(3, 6, 5)
    self.conv2 = nn.Conv2d(6, 24, 5)
    self.conv3 = nn.Conv2d(24, 48, 5)
    self.conv4 = nn.Conv2d(48, 96, 5)
    #
    self.fc1 = nn.Linear(96 * 5 * 5, 720)
    self.fc2 = nn.Linear(720, 300)
    self.fc3 = nn.Linear(720, 14)





        
