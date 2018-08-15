#!/usr/bin/env python3

import gym
import retro


#builds a retro game environment for use with the gameplay and training loops
def build_retro_env(game, state=''):
    env = retro.make(game=game, state=state)
    return env

#builds a regular gym environment for use with the gameplay and training loops
def build_env(environment):
    env = gym.make(environment)
    return env

