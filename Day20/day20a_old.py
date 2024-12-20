import copy
import util

def quick_search(grid, start, goal):
    visited = set()
    queue = [(start[0], start[1], 0)]
    best_cost = float('inf')
    while queue:
        x, y, cost = queue.pop(0)
        if (x, y) == goal and cost < best_cost:
            best_cost = cost
            continue
        visited.add((x, y))
        for dx, dy in util.cardinal:
            n_x = x + dx
            n_y = y + dy
            if not util.out_of_bounds(grid, n_x, n_y) and grid[n_y][n_x] != '#' and (n_x, n_y) not in visited:
                queue.append((n_x, n_y, cost+1))
    return best_cost

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

    baseline = quick_search(grid, start, goal)

    count = 0

    for y, row in enumerate(grid):
        print(y, len(grid))
        for x, c in enumerate(row):
            if c == '#':
                new_grid = copy.deepcopy(grid)
                new_grid[y][x] = '.'
                new_time = quick_search(new_grid, start, goal)
                # if new_time < baseline:
                #     print(f"Shortcut saves {baseline - new_time}")
                # if baseline - new_time == 2:
                #     count += 1
                if baseline - new_time >= 100:
                    count += 1

    print("done")
    print(count)

