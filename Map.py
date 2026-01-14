import pygame
from configs.maps import level_1, level_3, level_4, level_5
from configs.config import TILE_SIZE
from configs.brick_confing import concrete_tile, forest_tile
from BricksTile import BricksTile
from Tile import Tile

class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tiles = pygame.sprite.Group()
        self.not_tile = pygame.sprite.Group()
        for row_index, row in enumerate(level_4):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.tiles.add(BricksTile(x, y))
                if tile == 2:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.tiles.add(Tile(concrete_tile, tile, x, y))
                if tile == 3:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.not_tile.add(Tile(forest_tile, tile, x, y))


    def destruction_brick(self, rocket, destruct_side):
          for brick in self.tiles:
            if rocket.rect.colliderect(brick.rect):
                if isinstance(brick, BricksTile):
                    brick.destroy_side(destruct_side)
                    rocket.destroy()
                    break
                if brick.type == 2:
                    rocket.destroy()
                if brick.type == 3:
                    return


    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)
        for not_tile in self.not_tile:
            surface = pygame.Surface(not_tile.image.get_size(), pygame.SRCALPHA)
            surface.blit(not_tile.image, (0, 0))
            surface.set_alpha(180)  # 0-255, чем меньше, тем прозрачнее
            screen.blit(surface, not_tile.rect.topleft)


