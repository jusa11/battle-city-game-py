from configs.sounds import DESTROY_TANK_SOUND

class RocketHit:
    def __init__(self, rect):
        self.rect = rect
        self.destroy_tank_sound = DESTROY_TANK_SOUND


    def hit_target(self, alive, enemies, player, game_score):
        """Попадание снаряда"""
        if enemies:
            for enemy in enemies:
                if self.rect.colliderect(enemy.rect) and alive:
                    alive = False
                    enemy.alive = False
                    game_score['score'] += 150
                    self.destroy_tank_sound.play()
                    break

        if player:
            if self.rect.colliderect(player.rect) and alive:
                alive = False
                player.alive = False
                self.destroy_tank_sound.play()
