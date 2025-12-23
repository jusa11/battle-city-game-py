import pygame
from configs.maps import level_1
from configs.config import TILE_SIZE
from BricksTile import BricksTile

class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(level_1):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.tiles.add(BricksTile(x, y))

    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)

    def destruction_brick(self, rocket, destruct_side):
          for brick in self.tiles:
            if rocket.rect.colliderect(brick.rect):
                print(f"Столкновение с кирпичом, side={destruct_side}, parts_alive={brick.parts_alive}")
                brick.destroy_side(destruct_side)
                rocket.destroy()
                break

