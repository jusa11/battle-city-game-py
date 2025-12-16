import pygame
from configs.maps import level_1, level_2
from configs.config import TILE_SIZE
from Tile import Tile
from MainTank import MainTank


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


    def destruction_brick(self, rocket, game):
        if rocket:
            for brick in self.tiles:
                if rocket.rect.colliderect(brick.rect) and rocket.alive:
                    rocket.destroy()
                    brick.kill()
                    break

        if rocket and not rocket.alive:
            rocket.shell_explosion(game)
            if rocket.explosion_anim.finished:
                MainTank.rocket = None

