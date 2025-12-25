import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, type, x, y):
        super().__init__()
        self.image = image
        self.type = type
        self.rect = self.image.get_rect(topleft=(x, y))
