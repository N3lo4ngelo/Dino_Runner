from dino_runner.utils.constants import SWORD, SWORD_TYPE
from dino_runner.components.powerups.power_up import PowerUp

class Sword(PowerUp):
    def __init__(self):
        self.image = SWORD
        self.type = SWORD_TYPE
        super().__init__(self.image, self.type)