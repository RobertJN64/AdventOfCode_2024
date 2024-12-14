import util

class Robot:
    def __init__(self, line: str):
        pos, v = line.split(' ')
        self.x, self.y = list(map(int, pos.removeprefix('p=').split(',')))
        self.vx, self.vy = list(map(int, v.removeprefix('v=').split(',')))

    def tick(self, max_x, max_y):
        self.x += self.vx
        self.y += self.vy

        if self.x >= max_x:
            self.x -= max_x
        if self.x < 0:
            self.x += max_x

        if self.y >= max_y:
            self.y -= max_y
        if self.y < 0:
            self.y += max_y

    def quadrant(self, max_x, max_y):
        left = self.x < int(max_x / 2)
        right = self.x >= int((max_x + 1) / 2)
        top = self.y < int(max_y / 2)
        bottom = self.y >= int((max_y + 1) / 2)

        if left and top:
            return 1
        if right and top:
            return 2
        if left and bottom:
            return 3
        if right and bottom:
            return 4
        return 0

    def __repr__(self):
        return f"Robot at ({self.x}, {self.y}) with velocity ({self.vx}, {self.vy})"

def main():
    with open("Day14/day14.txt") as f:
        robots = [Robot(line.strip()) for line in f.readlines()]
    print(robots[0:10])

    MAX_X = 101
    MAX_Y = 103

    for i in range(0, 100):
        for robot in robots:
            robot.tick(MAX_X, MAX_Y)

    #print(robots)
    quads = [0, 0, 0, 0, 0]
    for robot in robots:
        #print(robot)
        #print(robot.quadrant(MAX_X, MAX_Y))
        quads[robot.quadrant(MAX_X, MAX_Y)] += 1
    #print(quads[1:])
    print(quads[1] * quads[2] * quads[3] * quads[4])

