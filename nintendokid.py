#!/usr/bin/env python
import gym
import retro
import torch
import torch.nn as nn
import torch.nn.functional as F

from environments.games import *

env = build_retro_env(game='1943-Nes')


observation = env.reset()
while True:
    action = env.action_space.sample()
    env.step(action)
    env.render()




