import random

from dino_runner.utils.constants import PUMPKIN
from dino_runner.components.obstacles.obstacle import Obstacle

class Pumpkin(Obstacle):
    def __init__(self):
        img, pumpkin_pos = (PUMPKIN, 325)
        self.type = 0
        super().__init__(img, self.type)
        self.rect.y = pumpkin_pos
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0