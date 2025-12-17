import sys
import pygame
from Tank import Tank
from configs.sounds import DRIVING_TANK_SOUND
from configs.main_tank_config import MAIN_TANK_IMAGE, MAIN_TANK_X, MAIN_TANK_Y, MAIN_TANK_FRAMES


class MainTank(Tank):
    def __init__(self):
        super().__init__(MAIN_TANK_IMAGE, MAIN_TANK_X, MAIN_TANK_Y, MAIN_TANK_FRAMES)
        self.driving_tank_sound = DRIVING_TANK_SOUND

    def handle_user_input(self):
        """Обработка ввода"""
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


