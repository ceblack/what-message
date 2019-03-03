#!/usr/bin/env python3
import time
import random

def random_wait(seconds):
    return(seconds * random.random())

def sleep_random(seconds):
    time.sleep(random_wait(seconds))
