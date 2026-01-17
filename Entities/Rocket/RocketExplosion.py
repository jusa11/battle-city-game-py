from Animation import Animation
from configs.config import ROCKET_EXPLOSION_FRAMES


class RocketExplosion:
    def __init__(self):
        self.explosion_frames = ROCKET_EXPLOSION_FRAMES
        self.explosion_anim = Animation(self.explosion_frames, 30, False)


    def rocket_explosion(self, screen, rocket_x, rocket_y):
        if self.explosion_anim and not self.explosion_anim.finished:
            self.explosion_anim.update()
            screen.blit(self.explosion_anim.get_image(),
                    (rocket_x -22, rocket_y - 22))