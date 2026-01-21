from random import choice

class EnemyAI:
    def __init__(self):
        pass

    def shooting(self, tank):
        possible = [50, 100, 200]
        if tank.frame % choice(possible) == 0:
            if not tank.weapon.rocket:
                tank.is_shot = True
        else:
            tank.is_shot = False


    def random_moving(self, tank):
        possible = [0, -90, 90, 180]
        possible.remove(tank.angle)
        tank.angle = choice(possible)


    def attack_moving(self, tank, goal_coordinates, map):
        current_goal_x, current_goal_y = goal_coordinates
        current_self_x, current_self_y = tank.coordinates

        directions = []

        if current_self_x < current_goal_x:
            directions.append(('right', -90))

        if current_self_x > current_goal_x:
            directions.append(('left', 90))

        if current_self_y > current_goal_y:
            directions.append(('up', 0))

        if current_self_y < current_goal_y:
            directions.append(('down', 180))

        possible_directions = []

        for direction, angle in directions:
            dx, dy = tank.possible_directions[direction]
            next_x, next_y = dx + current_self_x, dy + current_self_y
            if map.check_is_free_tile((next_x, next_y)):
                possible_directions.append(angle)

        if possible_directions:
            tank.angle = choice(possible_directions)
        else:
            tank.angle = tank.last_good_angle

        tank.old_coordinates = tank.coordinates

