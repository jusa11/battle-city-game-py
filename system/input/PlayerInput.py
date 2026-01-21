import sys
import pygame

class PlayerInput:
    def tank_driving(self, tank):
        """Обработка ввода"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tank.set_action('fire')
                else:
                    tank.set_action(event.key)
                    tank.driving_tank_sound.play()

            if event.type == pygame.KEYUP:
                tank.driving_tank_sound.stop()
                if event.key in tank.key_to_direction:
                    direction, _, _ = tank.key_to_direction[event.key]
                    if tank.direction == direction:
                        tank.direction = None
