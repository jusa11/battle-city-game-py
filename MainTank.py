import sys
import pygame
from Tank import Tank
from Animation import Animation
from configs.main_tank_config import MAIN_TANK_IMAGE, MAIN_TANK_X, MAIN_TANK_Y, MAIN_TANK_FRAMES


class MainTank(Tank):
    def __init__(self):
        super().__init__(MAIN_TANK_IMAGE, MAIN_TANK_X, MAIN_TANK_Y)
        self.driving_tank_sound = pygame.mixer.Sound(
            file='./sounds/ride-tank.mp3')
        self.tracks = MAIN_TANK_FRAMES
        self.tracks_anim = Animation(self.tracks, 1)

    def handle_user_input(self):
        """Обработка событий нажатия на клавиши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.set_action('fire')
                else:
                    self.set_action(event.key)
                    self.driving_tank_sound.play()

            if event.type == pygame.KEYUP:
                self.driving_tank_sound.stop()
                if event.key in self.key_to_direction:
                    direction, _, _ = self.key_to_direction[event.key]
                    if self.direction == direction:
                        self.direction = None


