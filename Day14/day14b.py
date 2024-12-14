from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import util

robots = []
MAX_X = 101
MAX_Y = 103
TIMER = 0

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

MIN_SCORE = float('inf')
def animate(_):
    global TIMER
    global MIN_SCORE

    while True:
        quads = [0, 0, 0, 0, 0]
        for robot in robots:
            robot.tick(MAX_X, MAX_Y)
            quads[robot.quadrant(MAX_X, MAX_Y)] += 1
        score = quads[1] * quads[2] * quads[3] * quads[4]
        TIMER += 1
        if score < MIN_SCORE:
            break

    MIN_SCORE = score

    grid = np.zeros((103,101))
    for robot in robots:
        grid[robot.y][robot.x] = 1

    plt.cla()
    plt.gca().set_title(f'seconds = {TIMER}, score = {score}')
    plt.gca().imshow(grid)  # redraw the image

def main():
    global robots
    with open("Day14/day14.txt") as f:
        robots = [Robot(line.strip()) for line in f.readlines()]
    print(robots[0:10])

    JUMP_TO_FINAL = False

    if JUMP_TO_FINAL:
        for i in range(0, 7286):
            for robot in robots:
                robot.tick(MAX_X, MAX_Y)
        grid = np.zeros((101, 103))
        for robot in robots:
            grid[robot.x][robot.y] = 1
        plt.cla()
        plt.gca().set_title(f'seconds = {7286}')
        plt.gca().imshow(grid)  # redraw the image
        plt.show()

    else:
        fig = plt.figure()
        _ = FuncAnimation(fig, animate, interval=1000)
        plt.show()
