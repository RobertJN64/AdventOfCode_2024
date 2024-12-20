import copy

import util

def main():
    with open("day20.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    goal = (0, 0)
    start = (0, 0)
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'E':
                goal = (x,y)
            if c == 'S':
                start = (x,y)

    def constraint(n_x, n_y, _, __):
        return grid[n_y][n_x] != '#'

    baseline = util.wavefront(grid, start, goal, constraint)[start[1]][start[0]] - 1

    count = 0

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '#':
                new_grid = copy.deepcopy(grid)
                new_grid[y][x] = '.'

                def constraint(n_x, n_y, _, __):
                    return new_grid[n_y][n_x] != '#'

                new_time = util.wavefront(new_grid, start, goal, constraint)[start[1]][start[0]] - 1
                print(x, y, new_time)
                if new_time < baseline:
                    print(f"Shortcut saves {baseline - new_time}")
                # if baseline - new_time >= 100:
                #     count += 1

    print("done")
    print(count)


main()