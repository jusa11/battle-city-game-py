from system.animations.Animation import Animation
from configs.config import TANK_SPAWN_FRAMES


class TankSpawn:
    def __init__(self):
        self.anim = Animation(TANK_SPAWN_FRAMES, duration=150, loop=False, repeat=3)

    def start_anim(self, screen, x, y):
        if not self.anim.finished:
            self.anim.update()
            screen.blit(self.anim.get_image(), (x, y))
