class GameContext:
    def __init__(self, player, enemies, map, timer, score, phase):
        self.player = player
        self.enemies = enemies
        self.map = map
        self.timer = timer
        self.score = score
        self.phase = phase