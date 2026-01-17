import pygame
from configs.brick_confing import parts
from configs.config import TILE_SIZE

class BricksTile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.parts = parts
        self.parts_alive = [True] * 16
        self.image = self.collect_parts()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.sides = {
            'top': [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            'bottom': [[12, 13, 14, 15], [8, 9, 10, 11], [4, 5, 6, 7], [0, 1, 2, 3]],
            'left': [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]],
            'right': [[3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13], [0, 4, 8, 12]],
        }

    def collect_parts(self):
        surface = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        for i, alive in enumerate(self.parts_alive):
            if alive:
                col = i % 4
                row = i // 4
                x = col * (TILE_SIZE // 4)
                y = row * (TILE_SIZE // 4)
                surface.blit(self.parts[i], (x, y))
        return surface

    def destroy_side(self, side):
        if not self.sides[side]:
            return

        current_row = self.sides[side][0]

        if any(self.parts_alive[i] for i in current_row):
            for i in current_row:
                self.parts_alive[i] = False

            del self.sides[side][0]

            self.image = self.collect_parts()
            self.mask = pygame.mask.from_surface(self.image)

            if not any(self.parts_alive):
                self.kill()


