import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class Network(nn.Module):

    def __init__(self):
        super(Network, self).__init__()
        #Starts with some convolutional layers
        self.conv1 = nn.Conv2d(3, 6, 5)
        #self.bn1   = nn.BatchNorm2d(6)
        self.conv2 = nn.Conv2d(6, 24, 5)
        #self.bn2   = nn.BatchNorm2d(24)
        self.conv3 = nn.Conv2d(24, 48, 5)
        #self.bn3   = nn.BatchNorm2d(48)
        self.conv4 = nn.Conv2d(48, 96, 5)
        #some fully connected layers after
        self.fc1 = nn.Linear(259200, 720)
        self.fc2 = nn.Linear(720, 300)
        self.fc3 = nn.Linear(300, 9)
    

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(F.relu(self.conv4(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        #gym does not like negative inputs, so taking a relu of the last layer
        #removes those negative values
        x = F.relu(self.fc3(x))
        return x
    #Coppied from the tutorial, because honestly it gets the job done
    #https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html#define-the-network
    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features
    
    def calculate_loss(self, actual, expected):
        loss = F.smooth_l1_loss(actual, expected)
        return loss
        
 #   def optimize():


#based upon this ring buffer idea and some other code from pytroch docs
#https://gist.github.com/AdrienLE/4b7e59d1143fd42b640dda148b763e7a#file-ring_buf-py
class Memory(object):

    def __init__(self, size):
        #Could also use a python deque here, but I have heard it is slower to 
        #get random data from, so I'm just going with this.
        self.memory = [] 
        self.size = size
    #There are better ways of doing this, but this was easy to read, so I'm
    #leaving it for now.
    def push(self, element):
        if len(self.memory) < self.size:
            self.memory.append(element)
        elif len(self.memory) == slef.size:
            self.memory.pop(0)
            self.memory.append(element)

    
    def random(self, grab_size):
        output = random.sample(self.memory, grab_size)
        return output

