from configs.config import TILE_SIZE
from system.collisions.TankCollisions import TankCollisions

class TankMovement:
    def __init__(self):
        self.collisions = TankCollisions()


    def move(self, tank, context):
        old_coordinates = tank.coordinates
        _, _, (dx, dy) = next(
            (v for v in tank.key_to_direction.values() if v[0] == tank.direction),
            (None, None, (0, 0))
        )

        tank.old_rect = tank.rect.copy()

        if tank.direction != tank.old_direction:
            if tank.direction in ['left', 'right']:
                tank.rect.y = round(tank.rect.y / TILE_SIZE) * TILE_SIZE
            elif tank.direction in ['up', 'down']:
                tank.rect.x = round(tank.rect.x / TILE_SIZE) * TILE_SIZE

        tank.old_direction = tank.direction

        tank.rect.x += dx * tank.speed
        tank.rect.y += dy * tank.speed

        self.collisions.check_collision(tank, context.enemies, context.map, context.player)

        tank.x, tank.y = tank.rect.topleft
        tank.coordinates = (round(tank.rect.x / TILE_SIZE), round(tank.rect.y / TILE_SIZE))

        return tank.coordinates != old_coordinates