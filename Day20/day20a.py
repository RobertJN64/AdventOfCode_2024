import util

def main():
    with open("Day20/day20.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    goal = (0, 0)
    start = (0, 0)
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'E':
                goal = (x,y)
            if c == 'S':
                start = (x,y)

    def constraint(new_x, new_y, _, __):
        return grid[new_y][new_x] != '#'

    costs = util.wavefront(grid, start, goal, constraint)

    count = 0
    for y, row in enumerate(costs):
        for x, cost_one in enumerate(row):
            if cost_one == 0:
                continue
            for dx, dy in util.cardinal:
                n_x = x + dx * 2
                n_y = y + dy * 2
                if not util.out_of_bounds(grid, n_x, n_y) and costs[n_y][n_x] != 0:
                    cost_two = costs[n_y][n_x]
                    if cost_one - cost_two > 2:
                        #print("Found shortcut that saves", cost_one - cost_two - 2)
                        if cost_one - cost_two - 2 >= 100:
                            count += 1

    print("done")
    print(count)
