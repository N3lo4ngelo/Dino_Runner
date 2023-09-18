import random
import pygame
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.heart import Heart
from dino_runner.components.powerups.sword import Sword
from dino_runner.utils.constants import HEART_TYPE, SHIELD_TYPE, SWORD_TYPE, DEFAULT_TYPE

class PowerUpManager:
  def __init__(self):
    self.power_ups = []
    self.when_appars = 0
    self.POWER_UPS = [Sword(), Heart(), Shield()]
  
  def generate_power_up(self, score):
    if len(self.power_ups) == 0 and self.when_appars == score:
      self.when_appars += random.randint(200, 300)
      self.power_ups.append(self.POWER_UPS[random.randint(0,2)])

  def update(self, score, game_speed, player):
    self.generate_power_up(score)
    for power_up in self.power_ups:
      power_up.update(game_speed, self.power_ups)
      if player.dino_rect.colliderect(power_up.rect):
        player.type = power_up.type
        if player.type == HEART_TYPE:
          player.lives += 1
          self.power_ups.pop()
        elif player.type == SHIELD_TYPE:
            power_up.start_time = pygame.time.get_ticks()
            player.shield = True
            player.has_power_up = True
            player.type = power_up.type
            player.power_up_time = power_up.start_time + (power_up.duration * 1000)
            self.power_ups.pop()
        else:
            power_up.start_time = pygame.time.get_ticks()
            player.shield = True
            player.has_power_up = True
            player.type = power_up.type
            player.power_up_time = power_up.start_time + (power_up.duration * 1500)
            self.power_ups.pop()
        
  
  def reset_power_ups(self):
    self.power_ups = []
    self.when_appars = random.randint(200, 300)

  def draw(self, screen):
    for power_up in self.power_ups:
      power_up.draw(screen)