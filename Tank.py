import  pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, tank_img, tank_x, tank_y, tank_rect, tank_angle=0,):
        super().__init__()
        self.img = tank_img
        self.width, self.height = self.img.get_size()
        self.x = tank_x
        self.y = tank_y
        self.rect = tank_rect   # координаты
        self.rect.topleft = (int(self.x), int(self.y))
        self.mask = pygame.mask.from_surface(self.img)
        self.angle = tank_angle