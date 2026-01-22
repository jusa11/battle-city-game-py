from configs.sounds import DESTROY_TANK_SOUND

class ProjectileHit:
    def __init__(self, rect):
        self.rect = rect
        self.destroy_tank_sound = DESTROY_TANK_SOUND


    def hit_target(self, enemies, player):
        """Попадание снаряда"""
        if enemies:
            for enemy in enemies:
                if self.rect.colliderect(enemy.rect):
                    enemy.alive = False
                    self.destroy_tank_sound.play()
                    return True

        if player:
            if self.rect.colliderect(player.rect):
                player.alive = False
                self.destroy_tank_sound.play()

        return False
