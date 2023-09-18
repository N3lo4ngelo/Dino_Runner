import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.pumpkin import Pumpkin
from dino_runner.components.obstacles.slash import Slash
from dino_runner.utils.constants import SWORD_TYPE, HEART_TYPE, SHIELD_TYPE, SLASH_SOUND, GAME_OVER_SOUND, SHIELD_BLOCK_SOUND, DAMAGE


class ObstacleManager:
  def __init__(self, player):
    self.obstacles = []
    self.player = player

  def update(self, game):
    obstacle_type = [
      Cactus(),
      Bird(),
      Pumpkin()
    ]

    if len(self.obstacles) == 0:
      self.obstacles.append(obstacle_type[random.randint(0, 2)])

    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles)
      if game.player.dino_rect.colliderect(obstacle.rect):
          if self.player.lives > 1:
            if game.player.type == SHIELD_TYPE:
              pygame.time.delay(50)
              game.sound_player(SHIELD_BLOCK_SOUND)
              #game.game_speed += 1
              #game.score += 50
              self.obstacles.pop()
            elif game.player.type == SWORD_TYPE:
              rect_x = obstacle.rect.x
              rect_y = obstacle.rect.y
              slash = Slash(rect_x, rect_y)
              self.obstacles.append(slash)
              game.sound_player(SLASH_SOUND)
              pygame.time.delay(50)
              self.obstacles.remove(obstacle)
            else:
              game.sound_player(DAMAGE)
              pygame.time.delay(50)
              self.player.lives -= 1
              self.obstacles.pop()
          else:
            game.sound_player(GAME_OVER_SOUND)
            pygame.time.delay(1000)
            game.playing = False
            game.death_count += 1
            break
      

      

        

    
  def reset_obstacles(self):
    self.obstacles = []

  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)