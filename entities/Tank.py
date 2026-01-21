import  pygame
from system.animations.Animation import Animation
from system.TankWeapon import TankWeapon
from system.animations.TankExplosion import TankExplosion
from configs.config import KEY_TO_DIRECTION


class Tank(pygame.sprite.Sprite):
    def __init__(self, tank_img, tank_x, tank_y, tracks, tank_angle=0):
        super().__init__()
        self.img = tank_img
        self.width, self.height = self.img.get_size()
        self.x = tank_x
        self.y = tank_y
        self.rect = self.img.get_rect(topleft=(int(self.x), int(self.y)))
        self.mask = pygame.mask.from_surface(self.img)
        self.angle = tank_angle
        self.alive = True
        self.direction = None
        self.is_collision = None
        self.key_to_direction = KEY_TO_DIRECTION
        self.tracks = tracks
        self.tracks_anim = Animation(self.tracks, 10)
        self.explosion = TankExplosion()
        self.old_direction = None
        self.coordinates = None
        self.old_rect = None
        self.weapon = TankWeapon()


    def set_action(self, action, is_key_up=False):
        if action == 'fire':
            data = {
                'angle': self.angle,
                'tank_x': self.x,
                'tank_y': self.y,
                'tank_width': self.width,
                'tank_height': self.height,
            }
            self.weapon.shot_gun(data)

        if action in self.key_to_direction:
            direction, angle, _ = self.key_to_direction[action]
            self.direction = direction
            self.angle = angle

        if is_key_up and action in self.key_to_direction:
            direction, _, _ = self.key_to_direction[action]
            if self.direction == direction:
                self.direction = None


    def draw(self, screen):
        if self.alive:
            rotated = pygame.transform.rotate(self.img, self.angle)
            screen.blit(rotated, self.rect)

            if self.tracks_anim and self.direction:
                self.tracks_anim.update()
                img = self.tracks_anim.get_image()
                rotated = pygame.transform.rotate(img, self.angle)
                screen.blit(rotated,
                            (self.x, self.y))
        else:
            self.explosion.tank_explosion(screen, self.x, self.y)
            if self.explosion.explosion_anim.finished:
                self.kill()

