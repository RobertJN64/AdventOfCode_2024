def out_of_bounds(grid, x, y):
    if y < 0 or y >= len(grid):
        return True
    if x < 0 or x >= len(grid[y]):
        return True
    return False

def fast_in_bounds(x, y, minx, maxx, miny, maxy):
    return minx <= x < maxx and miny <= y < maxy

def print_grid(grid):
    for line in grid:
        print(''.join(map(str, line)))
    print()

def print_grid_spaced(grid, tile_space):
    def str_pad(x):
        s = str(x)
        return ' ' * (tile_space - len(s)) + s

    for line in grid:
        print(''.join(map(str_pad, line)))
    print()

def debug_IO(f):
    def wrap(*args, **kwargs):
        s = f"Calling {f.__name__} with {args=} {kwargs=}"
        print(s)
        retval = f(*args, **kwargs)
        print(s, f"-> {retval}")
        return retval
    return wrap