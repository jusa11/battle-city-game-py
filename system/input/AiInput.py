import pygame


class AiInput:
    def ai_driving(self, tank):
        """Обработка событий от ИИ"""
        if tank.angle == 0:
            tank.set_action(pygame.K_w)
        elif tank.angle == 180:
            tank.set_action(pygame.K_s)
        elif tank.angle == -90:
            tank.set_action(pygame.K_d)
        elif tank.angle == 90:
            tank.set_action(pygame.K_a)
        if tank.is_shot:
            tank.set_action('fire')