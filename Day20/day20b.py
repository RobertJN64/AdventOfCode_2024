import util

def fast_costs(grid, pos, goal):
    maze_costs = [[0] * len(grid[0]) for _ in grid]  # init maze to 0
    x, y = pos
    counter = 1
    while (x, y) != goal:
        maze_costs[y][x] = counter
        for dx, dy in util.cardinal:
            n_x = x + dx
            n_y = y + dy
            if not util.out_of_bounds(maze_costs, n_x, n_y) and maze_costs[n_y][n_x] == 0 and grid[n_y][n_x] != '#':
                x = n_x
                y = n_y
                counter += 1
                break
    maze_costs[y][x] = counter
    return maze_costs

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

    costs = fast_costs(grid, start, goal)

    SEARCH_SIZE = 20
    GRID_SIZE = len(grid)

    count = 0
    for y_one, row_one in enumerate(costs):
        for x_one, cost_one in enumerate(row_one):
            if cost_one == 0:
                continue

            for y_two in range(max(0, y_one - SEARCH_SIZE), min(GRID_SIZE, y_one + SEARCH_SIZE + 1)):
                y_del = abs(y_one - y_two)
                x_del_avail = SEARCH_SIZE - y_del
                for x_two in range(max(0, x_one - x_del_avail), min(GRID_SIZE, x_one + x_del_avail + 1)):
                    cost_two = costs[y_two][x_two]
                    if cost_two == 0:
                        continue
                    x_del = abs(x_one - x_two)

                    delta = x_del + y_del

                    if cost_one - cost_two - delta >= 100:
                        #print("Found shortcut that saves", cost_one - cost_two - delta)
                        #print((x_one, y_one), (x_two, y_two))
                        count += 1

    print(count)