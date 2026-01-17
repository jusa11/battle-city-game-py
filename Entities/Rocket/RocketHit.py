class Targe:
    def __init__(self):
        pass

    def hit_target(self, enemies=None, player=None, game_score=None):
        """Попадание снаряда"""
        if enemies:
            for enemy in enemies:
                if self.rect.colliderect(enemy.rect) and self.alive:
                    self.alive = False
                    enemy.alive = False
                    game_score['score'] += 150
                    self.destroy_tank_sound.play()
                    break
                if self.explosion_anim.finished:
                    self.kill()

        if player:
            if self.rect.colliderect(player.rect) and self.alive:
                self.alive = False
                player.alive = False
                self.destroy_tank_sound.play()
            if self.explosion_anim.finished:
                self.kill()