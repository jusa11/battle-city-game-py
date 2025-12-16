import pygame
from configs.maps import level_1, level_2
from configs.config import TILE_SIZE
from Tile import Tile


class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tiles = pygame.sprite.Group()
        self.bricks = pygame.image.load('images/tile_bricks.png')

        for row_index, row in enumerate(level_1):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.tiles.add(Tile(self.bricks, x, y))


    def draw_map(self, screen):
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)


    def destruction_brick(self, rocket):
        if rocket:
            for brick in self.tiles:
                if rocket.rect.colliderect(brick.rect):
                    # rocket.shell_explosion(self.screen)
                    rocket.destroy()
                    brick.kill()
                    break

