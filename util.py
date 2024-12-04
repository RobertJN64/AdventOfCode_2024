def out_of_bounds(grid: list[list] | list[str], x: int, y: int):
    """
    Returns true if (x, y) is out of bounds of the grid
    """
    if y < 0 or y >= len(grid):
        return True
    if x < 0 or x >= len(grid[y]):
        return True
    return False

def fast_in_bounds(x: int, y: int, min_x: int, max_x: int, min_y, max_y):
    return min_x <= x < max_x and min_y <= y < max_y

def print_grid(grid: list[list]):
    for line in grid:
        print(''.join(map(str, line)))
    print()

def print_grid_spaced(grid: list[list], tile_space: int):
    """
    Print grid with left-pad on each item
    """
    def str_pad(x):
        s = str(x)
        return ' ' * (tile_space - len(s)) + s

    for line in grid:
        print(''.join(map(str_pad, line)))
    print()

def debug_IO(f):
    """
    Wrapper that prints debug info when function is called
    """
    def wrap(*args, **kwargs):
        s = f"Calling {f.__name__} with {args=} {kwargs=}"
        print(s)
        retval = f(*args, **kwargs)
        print(s, f"-> {retval}")
        return retval
    return wrap

def wavefront(grid: list[list], start: tuple[int, int], end: tuple[int, int], constraint):
    """
    Returns cost grid after running wavefront on grid
    Constraint is a function that takes input n_x, n_y, x, y and returns true / false
    """
    maze_costs = [[0] * len(grid[0]) for _ in grid]  # init maze to 0
    maze_costs[end[1]][end[0]] = 1

    done = False
    search_value = 1
    while not done:
        for y in range(0, len(maze_costs)):
            for x in range(0, len(maze_costs[y])):
                if maze_costs[y][x] == search_value:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        n_x = x + dx
                        n_y = y + dy
                        if not out_of_bounds(maze_costs, n_x, n_y) and maze_costs[n_y][n_x] == 0:
                            if constraint(n_x, n_y, x, y):
                                maze_costs[n_y][n_x] = search_value + 1
                                if start == (n_x, n_y):
                                    done = True
        search_value += 1
    return maze_costs

# PROFILING
# add this line around function
# @line_profiler.profile
# and run this
# kernprof -lv RUN_A.py

# SNAKEVIZ
# run this
# python -m cProfile -o A.prof RUN_A.py
# snakeviz A.prof