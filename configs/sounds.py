import pygame

START_GAME = None
DESTROY_TANK_SOUND = None
DRIVING_TANK_SOUND = None
SHOT = None

def load_sounds():
    global START_GAME, DESTROY_TANK_SOUND, DRIVING_TANK_SOUND, SHOT

    START_GAME = pygame.mixer.Sound(file='./sounds/start-game.mp3')
    DESTROY_TANK_SOUND = pygame.mixer.Sound('./sounds/explosion-tank.mp3')
    DRIVING_TANK_SOUND = pygame.mixer.Sound('./sounds/ride-tank.mp3')
    SHOT = pygame.mixer.Sound('./sounds/shot-gun.mp3')
