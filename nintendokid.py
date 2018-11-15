#!/usr/bin/env python
import gym
import random
import retro
import torch
import torch.nn as nn
import torch.nn.functional as F

from environments.games import *
from models import convnet
learning_rate = 1e-3

start_random = 0.8
end_random = 0.1
decay = 0.01


#creates the network for future use
model = convnet.Network()
print(model)

env = build_retro_env(game='1943-Nes', state='Level1')

observation = env.reset()

input = torch.randn(1, 3, 224, 240)
out = model(input)
print(out)

current_random = start_random
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
memory = convnet.Memory(3200)
while True:
        
    env.render()
    #sometimes we want to do a random action.
    if random.random() <= current_random:
        #generate a random tensor
        action = torch.rand(9)
    else:
        observation = torch.from_numpy(observation)
        observation = torch.unsqueeze(observation, 0)
        observation = observation.permute(0, 3, 1, 2)
        observation = observation.float()
        #observation = torch.
        #action = env.action_space.sample()
        action = torch.squeeze(model(observation))

    #Simple way to get binary outputs
    action = torch.round(action)

    print(action)
    observation, reward, done, _ = env.step(action)
    learning_data = (observation, action, reward, done)
    memory.push(learning_data)
    print(learning_data)

    
    

    print(reward)

