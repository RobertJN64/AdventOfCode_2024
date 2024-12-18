import util

def cust_wavefront(grid: list[list], start: tuple[int, int], end: tuple[int, int]):
    """
    Returns cost grid after running wavefront on grid
    Constraint is a function that takes input n_x, n_y, x, y and returns true / false
    """
    maze_costs = [[0] * len(grid[0]) for _ in grid]  # init maze to 0
    maze_costs[end[1]][end[0]] = 1

    done = False
    more_scan = True
    search_value = 1
    while not done and more_scan:
        more_scan = False
        for y in range(0, len(maze_costs)):
            for x in range(0, len(maze_costs[y])):
                if maze_costs[y][x] == search_value:
                    for dx, dy in util.cardinal:
                        n_x = x + dx
                        n_y = y + dy
                        if not util.out_of_bounds(maze_costs, n_x, n_y) and maze_costs[n_y][n_x] == 0:
                            if grid[n_y][n_x] == '.':
                                maze_costs[n_y][n_x] = search_value + 1
                                more_scan = True
                                if start == (n_x, n_y):
                                    done = True

        search_value += 1
    return maze_costs

def main():
    with open("Day18/day18.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    MAX = 70

    grid = [['.'] * (MAX+1) for _ in range(MAX+1)]

    for index, row in enumerate(lines):
        x, y = map(int, row.split(','))
        grid[y][x] = '#'

        #util.print_grid(grid)
        if index % 100 == 0:
            print(index)
        if cust_wavefront(grid, (0,0), (MAX,MAX))[0][0] == 0:
            break

    print(row)