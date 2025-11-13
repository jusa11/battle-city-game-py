import time
from random import randint


class Bot:
    def __init__(self, light_tank):
        self.light_tank = light_tank

    def shoot(self, shot_fn):
        while True:
            delay = randint(1, 3)
            time.sleep(delay)
            shot_fn()
