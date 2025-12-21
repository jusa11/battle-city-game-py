import pygame
from configs.maps import level_1
from configs.config import TILE_SIZE
from Tile import Tile

class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(level_1):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.tiles.add(Tile(x, y))

    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)

    def destruction_brick(self, rocket, screen, destruct_side):
        if rocket is None or not rocket.alive:
            return

        for brick in self.tiles:
            if pygame.sprite.collide_mask(rocket, brick):
                brick.destroy_side(destruct_side)
                rocket.destroy()
                break

        if not rocket.alive:
            rocket.shell_explosion(screen)
