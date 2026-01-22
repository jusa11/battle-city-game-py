from random import choice
from entities.EnemyTank import EnemyTank
from configs.config import TILE_SIZE
from system.animations.TankSpawn import TankSpawn


class EnemySpawner:
    def __init__(self):
        self.spawn_anim = None
        self.spawn_place = None

    def spawn(self, enemies, player):
        if self.spawn_anim is not None:
            return

        places = [
            (0, (0, 64)),
            (6, (384, 448)),
            (12, (768, 832))
        ]

        free_places = []

        for tile, spawn_range in places:
            occupied = False

            for enemy in enemies:
                ex, ey = enemy.x, enemy.y
                if spawn_range[0] <= ex <= spawn_range[1] and ey <= 64:
                    occupied = True
                    break

            px, py = player.x, player.y
            if spawn_range[0] <= px <= spawn_range[1] and py <= 64:
                occupied = True

            if not occupied:
                free_places.append((tile, spawn_range))

        if not free_places:
            return

        self.spawn_place = choice(free_places)
        self.spawn_anim = TankSpawn()

    def update(self, screen, enemies):
        if not self.spawn_anim or not self.spawn_place:
            return

        tile, spawn_range = self.spawn_place
        spawn_x = tile * TILE_SIZE
        spawn_y = 0

        self.spawn_anim.start_anim(screen, spawn_x, spawn_y)

        if self.spawn_anim.anim.finished:
            enemies.add(EnemyTank(spawn_x))
            self.spawn_anim = None
            self.spawn_place = None
