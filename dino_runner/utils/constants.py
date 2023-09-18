import pygame
import os

TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SWORD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Sword.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Sword.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_SWORD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpSword.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SWORD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Sword.png")), #Inserir diretorio
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Sword.png"))
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

PUMPKIN = [
    pygame.image.load(os.path.join(IMG_DIR, "Pumpkin/Pumpkin1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Pumpkin/Pumpkin2.png")),
]



CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))
SWORD = pygame.image.load(os.path.join(IMG_DIR, 'Other/sword.png'))
SWORD_SLASH = [pygame.image.load(os.path.join(IMG_DIR, 'Other/sword_slash.png'))]

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

SLASH_SOUND = os.path.join(IMG_DIR, 'Sounds/sword_effect.mp3')
GAME_OVER_SOUND = os.path.join(IMG_DIR, 'Sounds/game_over.mp3')
SHIELD_BLOCK_SOUND = os.path.join(IMG_DIR, 'Sounds/shield_block.mp3')
HEART_INCREASE_SOUND = os.path.join(IMG_DIR, 'Sounds/life_increase.mp3')
DAMAGE = os.path.join(IMG_DIR, 'Sounds/hit.mp3')

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
SWORD_TYPE = "sword"
HEART_TYPE = "heart"
