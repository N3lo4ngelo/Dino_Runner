import random
import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacles_manager import ObstacleManager
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.utils.text_utils import draw_message_component

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self, game_speed):
        self.x -= game_speed
        if self.x < -self.width:
          self.x = SCREEN_WIDTH + random.randint(2500, 3000)
          self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(ICON)
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()
    self.playing = False
    self.running = False
    self.score = 0
    self.death_count = 0
    self.difficulty = "Dino must escape"
    self.difficulty_speeds = {
            "Dino must fly": 10,  # Velocidade mais baixa para Fácil
            "Dino must escape": 20,  # Velocidade média para Médio
            "Dino must die": 35  # Velocidade mais alta para Difícil
        }
    self.game_speed = self.difficulty_speeds[self.difficulty]
    self.cloud = Cloud()
    self.lives = 3
    self.x_pos_bg = 0
    self.y_pos_bg = 380
    self.higher_score = 0
    self.player = Dinosaur()
    self.obstacle_manager = ObstacleManager(self.player)
    self.power_up_manager = PowerUpManager()

  def execute(self):
    self.running = True
    while self.running:
      if not self.playing:
        self.show_menu()
    
    pygame.display.quit()
    pygame.quit()

  def run(self):
      self.playing = True
      self.obstacle_manager.reset_obstacles()
      self.power_up_manager.reset_power_ups()
      self.game_speed = self.difficulty_speeds[self.difficulty]
      self.score = 0
      while self.playing:
        self.events()
        self.update()
        self.draw()

  def events(self):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.playing = False
          self.running = False

  def update(self):
      user_input = pygame.key.get_pressed()
      self.player.update(user_input)
      self.obstacle_manager.update(self)
      self.update_score()
      self.power_up_manager.update(self.score, self.game_speed, self.player)

  def update_score(self):
    self.score += 1

    if self.score > self.higher_score:
        self.higher_score = self.score

    if self.difficulty == "Dino must fly":
      if (self.score % 150 == 0):
        self.game_speed += 5
    elif self.difficulty == "Dino must escape":
       if (self.score % 100 == 0):
        self.game_speed += 5
    elif self.difficulty == "Dino must die":
      if (self.score % 50 == 0):
        self.game_speed += 7

  def draw(self):
    self.clock.tick(FPS)
    self.screen.fill((255, 255, 255)) 
    self.draw_background()
    self.player.draw(self.screen)
    self.obstacle_manager.draw(self.screen)
    self.draw_lives()
    self.draw_score()
    self.draw_power_up_time()
    self.cloud.draw(self.screen)
    self.cloud.update(self.game_speed)
    self.power_up_manager.draw(self.screen)
    pygame.display.update()
    pygame.display.flip()
    
  def draw_background(self):
    image_width = BG.get_width()
    self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
    self.screen.blit(BG, (image_width + self.x_pos_bg, image_width + self.y_pos_bg))
    if self.x_pos_bg <= -image_width:
        self.screen.blit(BG, (image_width + self.x_pos_bg, image_width + self.y_pos_bg))
        self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

  def draw_score(self):
    draw_message_component(
      f"Score: {self.score}",
      self.screen,
      pos_x_center = 1000,
      pos_y_center = 50
    )

  def draw_lives(self):
     draw_message_component(
        f"Vidas: {self.player.lives}",
          self.screen,
          pos_x_center = 100, 
          pos_y_center = 50
        )

  def draw_power_up_time(self):
    if self.player.has_power_up:
      time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
      if time_to_show >= 0:
        draw_message_component(
          f"{self.player.type.capitalize()} disponivel por {time_to_show} segundos",
          self.screen,
          font_size =  18,
          pos_x_center = 500,
          pos_y_center = 40
        )
      else:
        self.player.has_power_up = False
        self.player.type = DEFAULT_TYPE
  

  def handle_events_on_menu(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.playing = False
        self.running = False
      elif event.type == pygame.KEYDOWN:
        self.show_menu_difficulty()
        
  
  def show_menu_difficulty(self):
        selecting = True
        while selecting:
            self.screen.fill((255, 255, 255)) 

            half_screen_height = SCREEN_HEIGHT // 2
            half_screen_width = SCREEN_WIDTH // 2

            draw_message_component("Escolha a dificuldade:", self.screen, font_size=30, pos_y_center=half_screen_height - 100)
            draw_message_component("1 - Dino must fly", self.screen, font_size=20, pos_y_center=half_screen_height - 50)
            draw_message_component("2 - Dino must escape", self.screen, font_size=20, pos_y_center=half_screen_height)
            draw_message_component("3 - Dino must die", self.screen, font_size=20, pos_y_center=half_screen_height + 50)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.difficulty = "Dino must fly"
                        self.player.lives = 3
                        selecting = False
                    elif event.key == pygame.K_2:
                        self.difficulty = "Dino must escape"
                        self.player.lives = 2
                        selecting = False
                    elif event.key == pygame.K_3:
                        self.difficulty = "Dino must die"
                        self.player.lives = 1
                        selecting = False
                if event.type == pygame.QUIT:
                    pygame.quit()
        self.game_speed = self.difficulty_speeds[self.difficulty]
        self.run()

  def show_menu(self):
    self.screen.fill((255, 255, 255))
    half_screen_height = SCREEN_HEIGHT  // 2
    half_screen_width = SCREEN_WIDTH // 2
    
    if self.death_count == 0:
      draw_message_component("Pressione qualquer tecla para iniciar", self.screen)
    else:
      draw_message_component("Pressione qualquer tecla para reiniciar", self.screen, pos_y_center = half_screen_height + 150)

      draw_message_component(
        f"Melhor Pontuação: {self.higher_score}",
        self.screen,
        pos_y_center = half_screen_height - 75
      )

      draw_message_component(
        f"Sua pontuação: {self.score}",
        self.screen,
        pos_y_center = half_screen_height - 50
      )

      draw_message_component(
        f"Contagem de vidas: {self.death_count}",
        self.screen,
        pos_y_center = half_screen_height - 100
      )
        
      self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 30))

    pygame.display.flip()
    self.handle_events_on_menu()
  
  def sound_player(self, bgm):
    pygame.mixer.music.load(bgm)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume == 40


                      
              
  